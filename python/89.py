#!/usr/bin/env python
import re

save=0
while True:
    try: num=raw_input()
    except EOFError: break
    l = len(num)
    num=re.sub('IIII', 'IV', num)
    num=re.sub('VV', 'X', num)
    num=re.sub('VIV', 'IX', num)
    num=re.sub('XXXX', 'XL', num)
    num=re.sub('LL', 'C', num)
    num=re.sub('LXL', 'XC', num)
    num=re.sub('CCCC', 'CD', num)
    num=re.sub('DD', 'M', num)
    num=re.sub('DCD', 'CM', num)
    #print num
    save += l-len(num)
print save
