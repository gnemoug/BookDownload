#coding:utf8
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import urllib2
import json
import os

from ifengbook import settings as st
from ifengbook.items import ChapterItem
import re

class ChapterSpider(BaseSpider):
    name='common'
    allowed_domains = ['ifeng.com']
    start_urls = [st.START_URL]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        chapters = hxs.select('html/body/div[4]/div/div[3]/div[2]/div[1]/div/h3/ul/li')
        for i in chapters:
            cp = ChapterItem()
            org_title = i.select('a/text()').extract()[0]
            #chapter_order = re.findall(u'第(\d+)章', org_title)[0]
            dot_position = org_title.find('.')
            if dot_position != -1:
                #cp['order'] = chapter_order
                cp['title'] = org_title.encode('utf8').strip()
                cp['url'] = i.select('a/@href').extract()[0]
                post_data = re.search('/(\d+)/(\d+)\.htm', cp['url']).groups()

                content = json.loads(urllib2.urlopen('http://v.book.ifeng.com/read/book/remc.htm', 'b=%s&c=%s' % (post_data[0], post_data[1])).read())
                cp ['content'] = content['content'].encode('utf8').replace('<br/>', '\n')

#                filepath = u'%s/%s.txt' % (st.RESULT_PATH, cp['title'])
                filepath = os.path.join(st.RESULT_PATH, cp['title']+'.txt')

                if not os.path.exists(st.RESULT_PATH):
                    os.mkdir(st.RESULT_PATH)

                fh = open(filepath, 'w')

                if fh:
                    fh.write(cp['content'])
                    fh.close()
                else:
                    print cp['title']
