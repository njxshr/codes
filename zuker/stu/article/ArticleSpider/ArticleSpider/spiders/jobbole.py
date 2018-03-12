# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from scrapy.http import Request
from urllib import parse
from scrapy.loader import ItemLoader

# from ArticleSpider.items import JobBoleArticleItem
# 引入变量名费点事
from zuker.stu.article.ArticleSpider.ArticleSpider.items import JobBoleArticleItem
from zuker.stu.article.ArticleSpider.ArticleSpider.utils.common import get_md5

class JobboleSpider(scrapy.Spider):
    name = "jobbole"
    allowed_domains = ["blog.jobbole.com"]
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1. 获取文章列表页中的文章url并交给scrapy下载后进行的解析
        2. 获取下一页的url并交给scrapy进行下载，下载完成后交给scrapy

        """
        # 解释列表页中所有文章的url并交给scrapy下载后进行解析
        post_nodes = response.css("#archive div.floated-thumb .post-thumb a")
        for post_node in post_nodes:
            image_url = post_node.css("img::attr(src)").extract_first("")
            post_url = post_node.css("::attr(href)").extract_first("")
            yield Request(url=parse.urljoin(response.url,post_url),meta={"front_image_url":image_url},callback=self.parse_detail)
            print(post_url)
        # 提取下一页的url
        next_urls= response.css(".next.page-numbers::attr(href)").extract_first()
        if next_urls:
            yield Request(url=parse.urljoin(response.url,post_url),callback=self.parse)

    def parse_detail(self,response):
        article_item = JobBoleArticleItem()

        # 提取文章的具体字段
        # url = 'http://blog.jobbole.com/110287/'
        # 标题，创建日期，点赞数，喜欢数，评论数，正文 的提取
        front_image_url = response.meta.get("front_image_url","")
        title = response.xpath('//*[@class="entry-header"]/h1/text()').extract_first() # 文章封面图
        create_data = response.xpath("//*[@class='entry-meta']/p/text()").extract()[0].split()[0]
        praise_nums = response.xpath("//span[contains(@class,'vote-post-up')]/h10/text()").extract()[0]
        fav_nums = response.xpath("//span[contains(@class,'bookmark-btn')]/text()").extract_first().split()[0]
        # match_re = re.match(".*?(\d+).*",fav_nums)

        if fav_nums == '收藏':
            fav_nums = 0


        comment_nums = response.xpath("//a[@href='#article-comment']/span/text()").extract()[0]
        comment_re = re.match(".*?(\d+).*",comment_nums)

        if comment_nums == '  评论':
            comment_nums = 0
            a = 111
        content = response.xpath("//div[@class='entry']").extract()[0]
        type_tag = response.xpath("//*[@class='entry-meta']/p/a/text()").extract()[0].split()[0]
        author_type = response.xpath("//div[@class='copyright-area']/text()").extract()[0] # 本文作者： ,原文出处： ;
        if author_type == '本文作者： ':
            author = response.xpath("//div[@class='copyright-area']/a/text()").extract()[1]
        elif author_type == '原文出处： ':
            author = response.xpath("//div[@class='copyright-area']/a/text()").extract()[0]
        tags = type_tag + ',' + author
        article_item["url_object_id"] = get_md5(response.url)
        article_item['title'] = title
        article_item['url'] = response.url
        try:
            create_data = datetime.datetime.strptime(create_data,"%Y/%m/%d").date()
        except Exception as e:
            create_data = datetime.datetime.now().date()
        article_item['create_date'] =create_data
        article_item['front_image_url'] = [front_image_url]
        article_item['praise_nums'] = praise_nums
        article_item['comment_nums'] = comment_nums
        article_item['fav_nums'] = fav_nums
        article_item['tags'] = tags
        article_item['content'] = content

        # 通过 item Loader 可以将css xpath 维护工作变的简单 item loader是个容器
        item_loader = ItemLoader(item=JobBoleArticleItem(),response=response)

        # item_loader.add_css("title","    ")
        item_loader.add_xpath("title","//*[@class='entry-header']/h1/text()")
        item_loader.add_value("url",response.url)
        item_loader.add_value("url_object_id",get_md5(response.url))
        item_loader.add_xpath("create_date","//*[@class='entry-meta']/p/text()")
        item_loader.add_value("front_image_url",[front_image_url])
        item_loader.add_xpath("praise_nums","//span[contains(@class,'vote-post-up')]/h10/text()")
        item_loader.add_xpath("comment_nums","//a[@href='#article-comment']/span/text()")
        item_loader.add_xpath("fav_nums","//span[contains(@class,'bookmark-btn')]/text()")
        item_loader.add_xpath("tags","//*[@class='entry-meta']/p/a/text()")
        item_loader.add_xpath("content","//div[@class='entry']")

        article_item = item_loader.load_item() # 结果为list 还需要对数据做筛选，去掉冗余数据

        yield article_item # 提交 article_item

