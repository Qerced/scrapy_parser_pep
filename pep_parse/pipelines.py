from collections import defaultdict
import csv

from constants import RESULTS_DIR


class PepParsePipeline:
    def open_spider(self, item):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses = item['status']
        return item

    def close_spider(self, item):
        RESULTS_DIR.mkdir(exist_ok=True)
        file_path = ...
        with open(file_path, 'w', encoding='utf-8') as file:
            csv.writer(file, csv.unix_dialect).writerow(
                [
                    ('Статус', 'Количество'),
                    *self.statuses.items(),
                    ('Всего', sum(self.statuses.values()))
                ]
            )
