#!/usr/bin/python
# -*- coding: utf-8 -*-
import cgi
from datetime import datetime, timedelta

args = cgi.FieldStorage()
timezone = args.getvalue("timezone", "0")

new_date = datetime.now() + timedelta(hours=int(timezone))

print "Content-Type:text/html\r\n\r\n"
print format(new_date, '%H:%M:%S')
