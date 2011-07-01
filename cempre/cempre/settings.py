# Scrapy settings for cempre project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'cempre'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['cempre.spiders']
NEWSPIDER_MODULE = 'cempre.spiders'
DEFAULT_ITEM_CLASS = 'cempre.items.CempreItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
