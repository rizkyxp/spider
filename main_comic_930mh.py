# -*- coding: utf-8 -*-

import os
import sys

from scrapy.cmdline import execute

os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#createProxyByGithub()
execute(['scrapy', 'crawl', '930mh'])