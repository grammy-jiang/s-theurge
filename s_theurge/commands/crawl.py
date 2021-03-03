from typing import Dict

import yaml
from scrapy.commands.crawl import Command as CrawlCommand


class Command(CrawlCommand):
    def add_options(self, parser):
        super(Command, self).add_options(parser)
        parser.add_option(
            "--xpath-yaml",
            dest="xpath_yaml",
            help="use a yaml file for xpath scraping",
        )

    def run(self, args, opts):
        if opts.xpath_yaml:
            with open(opts.xpath_yaml) as fh:
                xpath_yaml: Dict = yaml.load(fh, Loader=yaml.SafeLoader)
            opts.spargs["xpath_yaml"] = xpath_yaml

        super(Command, self).run(args, opts)
