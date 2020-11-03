#!/usr/bin/env python3

import sys
import csv
import pytz
import datetime


def convert_timestamp(original_timestamp: str) -> str:
    """Parse timestamp from text, convert from US/Pacific to US/Eastern time zone,
    and change to RFC3339 format
    """
    pacific = pytz.timezone('US/Pacific')
    eastern = pytz.timezone('US/Eastern')
    original_time = datetime.datetime.strptime(original_timestamp, '%m/%d/%y %I:%M:%S %p')
    original_time = pacific.localize(original_time)
    return original_time.astimezone(eastern).isoformat()


if __name__ == '__main__':
    # read all lines from stdin as binary, so we don't crash on invalid utf8
    data = sys.stdin.buffer.read()
    data = data.decode('utf-8', 'replace')

    reader = csv.DictReader(data.splitlines())
    writer = csv.DictWriter(sys.stdout,
                            reader.fieldnames,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL)

    writer.writeheader()
    for row in reader:
        row['Timestamp'] = convert_timestamp(row['Timestamp'])
        writer.writerow(row)
