# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# pipeline需要手动打开
# settings里的67行的下三行
# ITEM_PIPELINES = {
#    'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
# }
import  codecs # 类似于open
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi # 异步
import MySQLdb
import MySQLdb.cursors
class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    # 自定义json温江的导出
    def __init__(self):
        self.file = codecs.open('article.json','w',encoding="utf-8")
    def process_item(self, item, spider):
        lines = json.dumps(dict(item),ensure_ascii=False) + "\n" # False是为了显示中文不报错
        self.file.write(lines)
        return item
    def spider_closed(self,spider):
        self.file.close

class MysqlPipeline(object):
    # 采用同步的机制写入mysql
    def __init__(self):
        # self.conn = MySQLdb.connect('172.18.8.81','root','123456','article_spider',
        #                             charset = 'utf8',use_unicode=True)
        self.conn = MySQLdb.connect('172.18.2.196', 'nocstatis', 'noc^321', 'nocstatis',
                                    charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        insert_sql = """
            insert into jobbole_article(title,url,create_date,fav_nums)
            VALUE (%s,%s,%s,%s)  
        """
        # 数据库密码123456
        self.cursor.execute(insert_sql,(item["title"],item["url"],item["create_date"],item["fav_nums"]))
        self.conn.commit()

class MysqlTwistedPipline(object):
    def __init__(self,dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls,settings):
        dbparms = dict(
            host = settings["MYSQL_HOST"],
            db = settings["MYSQL_DBNAME"],
            user = settings["MYSQL_USER"],
            passwd = settings["MYSQL_PASSWORD"],
            charset='utf8',
            cursorclass = MySQLdb.cursors.DictCursor,
            use_unicode = True,
        )

        dbpool = adbapi.ConnectionPool("MySQLdb",**dbparms)
        return cls(dbpool)

    def process_item(self,item,spider):
        # 使用twisted将mysql插入变成异步执行
        query = self.dbpool.runInteraction(self.do_insert,item)
        query.addErrback(self.handle_error) # 处理异常


    def handle_error(self,failure):
        # 处理异步插入的异常
        print(failure)


    def do_insert(self,cursor,item):
        # 执行具体的插入
        insert_sql = """
                 insert into jobbole_article(title,url,create_date,fav_nums)
                 VALUE (%s,%s,%s,%s)  
             """
        # 数据库密码123456
        cursor.execute(insert_sql, (item["title"], item["url"], item["create_date"], item["fav_nums"]))


class JsonExporterPipleline(object,):
    # 调用scrapy提供的json export 导出json文件
    def __init__(self):
        self.file = open('articleexport.json','wb')
        self.exporter = JsonItemExporter(self.file,encoding="utf-8",ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self,item,spider):
        self.exporter.export_item(item)
        return item


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:

            image_file_path= value["path"]
        item["front_image_path"] = image_file_path
        return item
        pass