#!/usr/bin/env python
#coding:utf8
#author:xdsecret1@gmail.com

import md5

BOOK_DIR='bookishere'
BOOK_NAME=u'书名'
BOOK_ID=md5.new('book_name').hexdigest()
BOOK_AUTHOR='xd'

OUTPUT_DIR='./'
TMP_DIR='./tmp'
DATA_DIR='./data'
