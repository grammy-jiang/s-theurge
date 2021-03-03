"""
The spider of theurge
"""
from typing import List
from urllib.parse import parse_qs, urlparse

from scrapy.exceptions import CloseSpider
from scrapy.http import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.spiders import CrawlSpider, Rule

from s_theurge.items import STheurgeItem


class TheUrgeSpider(CrawlSpider):
    """
    The spider of theurge
    """

    name: str = "theurge"

    start_urls: List[str] = [
        "https://theurge.com/",
    ]

    rules: List[str] = [
        Rule(
            LinkExtractor(restrict_xpaths="//*[@id='uid2']/div[1]"),
            callback="parse_item",
        )
    ]

    limit_product_number: int = 0

    def parse_item(self, response: Response):
        """

        :param response:
        :type response:
        :return:
        :rtype:

        @url https://theurge.com/women/search/?cat=bags
        @returns items 20
        @returns requests 0
        @scrapes brand category description price
        """
        try:
            category = parse_qs(urlparse(response.url).query)["cat"][0]
        except KeyError as exc:
            return

        for product in response.xpath(
            "//div[@class='_2f_jY']/article[@class='_2Mqpk']"
        ):
            loader = ItemLoader(STheurgeItem(), selector=product)
            loader.add_xpath("brand", ".//a/p/span/text()")
            loader.add_xpath("description", ".//a/p/text()")
            loader.add_xpath("price", ".//a/div[@class='eP0wn _2xJnS']/text()")
            loader.add_value("category", category)
            yield loader.load_item()

            self.limit_product_number += 1

            if self.limit_product_number == 300:
                raise CloseSpider("Product number limitation reached.")
