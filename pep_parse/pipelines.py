import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULTS_FOLDER


class PepParsePipeline:
    def __init__(self):
        self.result_dir = BASE_DIR / RESULTS_FOLDER
        self.filename = 'status_summary_{time_of_creation}.csv'
        self.result_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.statuses = defaultdict(int)

    def process_item(self, item, spider):
        self.statuses[item['status']] += 1
        return item

    def close_spider(self, spider):
        result_csv = self.result_dir / self.filename.format(
            time_of_creation=datetime.now().strftime(DATETIME_FORMAT)
        )
        with open(result_csv, 'w', encoding='utf-8') as file:
            csv.writer(
                file, csv.unix_dialect, quoting=csv.QUOTE_NONE
            ).writerows(
                (
                    ('Статус', 'Количество'),
                    *self.statuses.items(),
                    ('Всего', sum(self.statuses.values()))
                )
            )
