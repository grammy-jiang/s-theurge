"""
The spider of theurge
"""
from typing import List

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


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
