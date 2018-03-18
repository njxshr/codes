# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
from scrapy.loader import ItemLoader
import datetime
import scrapy
from scrapy.loader.processors import MapCompose,TakeFirst # 将我们的值 对他做两次处理

class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # items 类似字典的作用，但是比字典强
    pass


def add_jobbole(value):
    return value+ "-jobbole"


def date_convert(value):
    try:
        create_data = datetime.datetime.strptime(value, "%Y/%m/%d").date()
    except Exception as e:
        create_data = datetime.datetime.now().date()

    return create_data

def get_nums(value):
    import re
    match_re = re.match(".*?(\d+).*",fav_nums)
    if match_re:
        nums = int(match_re.group(1))
    else:
        nums = 0

    return nums

class ArticleItemLoader(ItemLoader):
    # 自定义itemloader
    default_output_processor = TakeFirst()

class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field(
        input_processor = MapCompose(lambda x:x+"-jobbole")  # 加上字段
    )
    create_date = scrapy.Field(
        input_processor=MapCompose(date_convert),  # 加上字段
        # output_processor=TakeFirst() # 取第一个
    )
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    praise_nums = scrapy.Field(
        input_processor = MapCompose(get_nums)
    )
    comment_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    fav_nums = scrapy.Field(
        input_processor=MapCompose(get_nums)
    )
    tags = scrapy.Field()
    content = scrapy.Field()