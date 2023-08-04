import logging

from scrapy import signals
from scrapy.exceptions import NotConfigured

from pep_parse.settings import BASE_DIR, RESULTS_FOLDER


LOG_MESSAGE = '"{dir_name}" directory has been created!'

logger = logging.getLogger(__name__)


class SpiderCreateDownloadDir:
    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool("MYEXT_ENABLED"):
            raise NotConfigured
        ext = cls()
        crawler.signals.connect(
            ext.spider_opened, signal=signals.spider_opened
        )
        return ext

    def spider_opened(self, spider):
        (BASE_DIR / RESULTS_FOLDER).mkdir(exist_ok=True)
        logger.info(LOG_MESSAGE.format(dir_name=RESULTS_FOLDER))
