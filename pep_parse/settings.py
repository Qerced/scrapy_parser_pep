from pathlib import Path


BASE_DIR = Path().cwd()
RESULTS_FOLDER = 'results'

DATETIME_FORMAT = '%Y-%m-%dT%H-%M-%S'

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEEDS = {
    f'{RESULTS_FOLDER}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
