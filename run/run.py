"""
Run this s-theurge spider
"""

import sys
from pathlib import Path
from typing import List

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from scrapy.utils.project import get_project_settings

sys.path.append(str(Path("/").joinpath(*Path(__file__).parts[:-2])))

MODULES: List[str] = [
    "s_theurge.settings",
]

if __name__ == "__main__":
    settings: Settings = get_project_settings()

    for module in MODULES:
        settings.setmodule(module)

    process: CrawlerProcess = CrawlerProcess(settings)
    process.crawl("theurge")
    process.start()
