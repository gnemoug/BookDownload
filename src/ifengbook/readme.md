使用方法：
========
1、修改 ifengbook/ifengbook/settings.py
RESULT_PATH = 'songshuigong'  下载后的文件保存在哪个目录下。
START_URL = 'http://v.book.ifeng.com/read/book/yc/vip/374/3004385.htm'  图书目
录所在页

2、在scrapy.cfg所在目录运行scrapy crawl common就可以开始下载。


项目简单介绍：
============
1、使用了scrapy做爬虫，可以从ifeng.com上爬小说，将小说按照章节保存为txt文件类型。
2、可以下载需要付费的章节。


TODO:
=====
考虑将下载到的txt做做成epub类型。
