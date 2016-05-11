#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi, cgitb

rad_file = "text_files/test.txt"

for line in open(rad_file, 'r').readlines():
    print line
