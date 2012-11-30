#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

import os.path
import zipfile
import conf
import shutil
from django import template
from django.template.loader import get_template
from django.conf import settings

settings.configure( 
    DEBUG=True,
    TEMPLATE_DIRS={
        os.path.join(os.path.dirname(__file__), 'templates'),
    },
)


#epub = zipfile.ZipFile(conf.BOOK_NAME+'.epub', 'w')
#epub.writestr('mimetype', 'application/epub+zip')

html_files = []
chapters = []


if os.path.exists(conf.TMP_DIR):
    shutil.rmtree(conf.TMP_DIR)
shutil.copytree(conf.DATA_DIR, conf.TMP_DIR)

for f in os.listdir(conf.BOOK_DIR):
    html_files.append(f[:f.find('.')]+'.html')
    chapters.append(f[:f.rfind('.')])
    shutil.copy(os.path.join(conf.BOOK_DIR, f),os.path.join(conf.TMP_DIR,'OEBPS' )+'/'+f[:f.find('.')]+'.html')

html_files.sort()
chapters.sort()

opf = get_template('content.opf.xml')
c = template.Context({'title': conf.BOOK_NAME, 'author':conf.BOOK_AUTHOR,
'bookid': conf.BOOK_ID, 'pages': html_files})
fh = open('./tmp/OEBPS/content.opf', 'w')
fh.write(opf.render(c).encode('utf8'))
fh.close()

ncx = get_template('toc.ncx.xml')
c = template.Context({'title': conf.BOOK_NAME, 'bookid': conf.BOOK_ID, 'navs':
    html_files, 'chapters':chapters})
fh = open('./tmp/OEBPS/toc.ncx', 'w')
fh.write(ncx.render(c).encode('utf8'))
fh.close()

cmd = 'cd ./tmp;'
cmd += 'zip -0Xq %s.epub mimetype;' % conf.BOOK_NAME
cmd += 'zip -Xr9Dq %s.epub *' % conf.BOOK_NAME
os.system(cmd.encode('utf8'))
