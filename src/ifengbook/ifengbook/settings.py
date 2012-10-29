# Scrapy settings for ifengbook project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'ifengbook'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['ifengbook.spiders']
NEWSPIDER_MODULE = 'ifengbook.spiders'
DEFAULT_ITEM_CLASS = 'ifengbook.items.ChapterItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

RESULT_PATH = 'songshuigong'
START_URL = 'http://v.book.ifeng.com/read/book/yc/vip/374/3004385.htm'

