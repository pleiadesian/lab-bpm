#!/bin/python3

import csv
import copy
from datetime import datetime

with open("ProData2020 (3).csv", 'rb') as f:
    lines = f.readlines()

lines_bak = copy.deepcopy(lines)
for line in lines[1:]:
    items = line.decode('UTF-8', errors='ignore').strip('\n').strip('\r').split(',')
    assert items[0].isdigit()
    if not items[1].encode('UTF-8').isalnum():
        lines_bak.remove(line)
    act_st = datetime.strptime(items[2], "%Y-%m-%d %H:%M:%S")
    act_en = datetime.strptime(items[3], "%Y-%m-%d %H:%M:%S")
    assert act_en > act_st
    assert items[4] == str((act_en - act_st).seconds)

with open("output.csv", 'wb') as f:
    f.writelines(lines_bak)
