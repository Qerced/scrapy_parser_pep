import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULTS_FOLDER


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        filename = BASE_DIR / RESULTS_FOLDER / (
            f'status_summary_{datetime.now().strftime(DATETIME_FORMAT)}.csv'
        )
        with open(filename, 'w', encoding='utf-8') as file:
            csv.writer(
                file, csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows(
                (
                    ('Статус', 'Количество'),
                    *self.statuses.items(),
                    ('Всего', sum(self.statuses.values()))
                )
            )
