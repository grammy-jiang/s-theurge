# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst


class Strip:
    def __call__(self, values):
        _values = []
        for value in values:
            if isinstance(value, str):
                _values.append(value.strip())
            else:
                _values.append(value)
        return _values


class STheurgeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field(input_processor=Strip(), output_processor=TakeFirst())
    sale_price = scrapy.Field(output_processor=TakeFirst())
    description = scrapy.Field(output_processor=TakeFirst())
    brand = scrapy.Field(output_processor=TakeFirst())
    category = scrapy.Field(output_processor=TakeFirst())
