# Scrapy settings for s_theurge project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from .autothrottle import *
from .concurrent import *
from .cookies import *
from .feeds import *
from .headers import *
from .httpcache import *
from .user_agent import *

BOT_NAME = "s_theurge"

SPIDER_MODULES = ["s_theurge.spiders"]
NEWSPIDER_MODULE = "s_theurge.spiders"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    's_theurge.middlewares.STheurgeSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "s_theurge.middlewares.STheurgeDownloaderMiddleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    "s_theurge.extensions.CategoryBrowsedExtension": 0,
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    's_theurge.pipelines.STheurgePipeline': 300,
#}

COMMANDS_MODULE = "s_theurge.commands"
