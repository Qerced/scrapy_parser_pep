import os
from scrapy.cmdline import execute

print(os.chdir(os.path.dirname(os.path.realpath(__file__))))

try:
    execute(
        [
            'scrapy',
            'crawl',
            'pep',
        ]
    )
except SystemExit:
    pass
