# -*- coding: utf-8 -*-
from __future__ import print_function

import csv, sys
from datetime import datetime


print('<pre>')
print('Mouvements des députés de la XVéme legislature - mis à jour le', datetime.today().strftime('%Y-%m-%d'))
prev_line = None
for line in csv.DictReader(open(sys.argv[1])):
	for dep in line:
		if dep not in ('date_debut', 'date_fin', 'total'):
			prev_line_dep = ''
			if prev_line:
				prev_line_dep = prev_line[dep]
			if prev_line_dep != line[dep]:
				print(dep, ':', prev_line_dep, '->', line[dep], '(', line['date_debut'], ')')
	prev_line = line