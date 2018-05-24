#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
read json5 sample code
"""

import json5


JSONFILE = './sampleData/sample.json5'


# -----------------------------------------------------------------------------
def main():
	"""
	main function
	"""

	file = open(JSONFILE)
	buf = file.read()
	file.close()

	conf = json5.loads(buf)
	print(conf)

	return
