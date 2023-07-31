from datetime import datetime

from collections import defaultdict
import csv

from pep_parse.constants import RESULTS_DIR


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        RESULTS_DIR.mkdir(exist_ok=True)
        file_path = RESULTS_DIR / f'status_summary_{datetime.now()}.csv'
        with open(file_path, 'w', encoding='utf-8') as file:
            csv.writer(file, csv.unix_dialect).writerow(
                [
                    ('Статус', 'Количество'),
                    *self.statuses.items(),
                    ('Всего', sum(self.statuses.values()))
                ]
            )
