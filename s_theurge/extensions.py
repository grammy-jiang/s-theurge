"""
Category Browsed extension
"""
from __future__ import annotations

import logging
import pprint
from collections import defaultdict
from copy import deepcopy
from typing import Dict

from scrapy import signals
from scrapy.extensions.logstats import LogStats
from twisted.internet import task

logger = logging.getLogger(__name__)


class CategoryBrowsedExtension(LogStats):
    """Log category browsed stats periodically"""

    categories: Dict[str, int]
    categories_prev: Dict[str, int]

    @classmethod
    def from_crawler(cls, crawler):
        obj = super(CategoryBrowsedExtension, cls).from_crawler(crawler)
        crawler.signals.connect(obj.item_scraped, signal=signals.item_scraped)
        return obj

    def item_scraped(self, signal, sender, item, response, spider):
        self.categories[item["category"]] += 1

    def spider_opened(self, spider):
        self.categories = defaultdict(int)
        self.categories_prev = deepcopy(self.categories)

        self.task = task.LoopingCall(self.log, spider)
        self.task.start(self.interval)

    def log(self, spider):
        message: Dict[str, str] = dict()

        for category, count in self.categories.items():
            count_prev = self.categories_prev[category]
            irate = (count - count_prev) * self.multiplier
            msg = f"Scraped {count} items (at {irate} items/min)"
            message[category] = msg

        self.categories_prev = deepcopy(self.categories)

        logger.info(pprint.pformat(message), extra={"spider": spider})
