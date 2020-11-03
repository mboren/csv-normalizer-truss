#!/usr/bin/env python3

import sys
import csv

if __name__ == '__main__':
    # read all lines from stdin as binary, so we don't crash on invalid utf8
    data = sys.stdin.buffer.read()
    data = data.decode('utf-8', 'replace')
    reader = csv.DictReader(data.splitlines())

    for line in reader:
        print(line)
