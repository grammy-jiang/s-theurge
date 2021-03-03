# A spider to scrape theurge

This repository is a spider to scrape theurge.

The environment for this spider is created by pipenv, and `Pipfile` is included
already.

## Part 1

A spider inherited from `CrawlSpider` is created here:

* [s-theurge/theurge.py at master · grammy-jiang/s-theurge](https://github.com/grammy-jiang/s-theurge/blob/master/s_theurge/spiders/theurge.py#L16)

The feeds for the item output by `JsonLinesItemExporter` is configured in the
settings module:

* [s-theurge/feeds.py at master · grammy-jiang/s-theurge](https://github.com/grammy-jiang/s-theurge/blob/master/s_theurge/settings/feeds.py)

And the spider will stop when reached the limitation of product items by raising
an exception of CloseSpider:

* [s-theurge/theurge.py at master · grammy-jiang/s-theurge](https://github.com/grammy-jiang/s-theurge/blob/master/s_theurge/spiders/theurge.py#L70)


## Part 2

A new `crawl` command is created through inherited from the original one, to
accept an additional option `--xpath-yaml`, parse the yaml file and pass it to
the spider:

* [s-theurge/crawl.py at master · grammy-jiang/s-theurge](https://github.com/grammy-jiang/s-theurge/blob/master/s_theurge/commands/crawl.py)

The spider takes this xpath yaml argument in the method of `__init__`, and
created the rules with the xpath in yaml:

* [s-theurge/theurge.py at master · grammy-jiang/s-theurge](https://github.com/grammy-jiang/s-theurge/blob/master/s_theurge/spiders/theurge.py#L33`)

## Part 3

A downloader middleware is created for logging download latency:

* [s-theurge/middlewares.py at master · grammy-jiang/s-theurge](https://github.com/grammy-jiang/s-theurge/blob/master/s_theurge/middlewares.py#L93)

This middleware is enabled in the settings module:

* [s-theurge/__init__.py at master · grammy-jiang/s-theurge](https://github.com/grammy-jiang/s-theurge/blob/master/s_theurge/settings/__init__.py#L37)

## Part 4

An extension for category browsed is created:

* [s-theurge/extensions.py at master · grammy-jiang/s-theurge](https://github.com/grammy-jiang/s-theurge/blob/master/s_theurge/extensions.py#L19)

This extension is enabled in the settings module:

* [s-theurge/__init__.py at master · grammy-jiang/s-theurge](https://github.com/grammy-jiang/s-theurge/blob/master/s_theurge/settings/__init__.py#L43)
