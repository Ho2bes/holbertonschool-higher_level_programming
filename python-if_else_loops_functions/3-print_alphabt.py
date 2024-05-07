#!/usr/bin/python3
i = 97
while i < 123:
    if chr(i) not in ['q', 'e']:
    print("{}".format(chr(i)), end='')
    i += 1
