from typing import Dict

import yaml
from scrapy.commands import BaseRunSpiderCommand
from scrapy.exceptions import UsageError


class Command(BaseRunSpiderCommand):

    requires_project = True

    def syntax(self):
        return "[options] <spider>"

    def short_desc(self):
        return "Run a spider"

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

        if len(args) < 1:
            raise UsageError()
        elif len(args) > 1:
            raise UsageError(
                "running 'scrapy crawl' with more than one spider is no longer supported"
            )
        spname = args[0]

        crawl_defer = self.crawler_process.crawl(spname, **opts.spargs)

        if getattr(crawl_defer, "result", None) is not None and issubclass(
            crawl_defer.result.type, Exception
        ):
            self.exitcode = 1
        else:
            self.crawler_process.start()

            if (
                self.crawler_process.bootstrap_failed
                or hasattr(self.crawler_process, "has_exception")
                and self.crawler_process.has_exception
            ):
                self.exitcode = 1