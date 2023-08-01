from collections import defaultdict
import csv
from datetime import datetime

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT, RESULTS_FOLDER


class PepParsePipeline:
    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_path = BASE_DIR / RESULTS_FOLDER
        results_path.mkdir(exist_ok=True)
        filename = results_path / (
            f'status_summary_{datetime.now().strftime(DATETIME_FORMAT)}.csv'
        )
        with open(filename, 'w', encoding='utf-8') as file:
            csv.writer(file, csv.unix_dialect).writerows(
                [
                    ('Статус', 'Количество'),
                    *self.statuses.items(),
                    ('Всего', sum(self.statuses.values()))
                ]
            )
