#!/usr/bin/env python3

import sys
import csv
import pytz
import datetime
from decimal import Decimal

ZIPCODE_LENGTH = 5


class ParseError(Exception):
    pass


def convert_timestamp(original_timestamp: str) -> str:
    """Parse timestamp from text, convert from US/Pacific to US/Eastern time zone,
    and change to RFC3339 format
    """
    pacific = pytz.timezone('US/Pacific')
    eastern = pytz.timezone('US/Eastern')

    try:
        original_time = datetime.datetime.strptime(original_timestamp, '%m/%d/%y %I:%M:%S %p')
    except ValueError:
        raise ParseError('Unable to parse timestamp: {}'.format(original_timestamp))

    original_time = pacific.localize(original_time)
    return original_time.astimezone(eastern).isoformat()


def pad_zipcode(zipcode: str) -> str:
    return zipcode.zfill(ZIPCODE_LENGTH)


def convert_duration(duration: str) -> str:
    """Change duration from HH:MM:SS.MS to number of seconds"""
    try:
        hours, minutes, seconds = duration.split(':')
        total = float(seconds)
        total += int(minutes) * 60
        total += int(hours) * 60 * 60
    except ValueError:
        raise ParseError('Unable to parse duration: {}'.format(duration))

    return str(total)


def total_duration(foo_duration: str, bar_duration: str) -> str:
    """Add up durations"""
    return str(Decimal(foo_duration) + Decimal(bar_duration))


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
        try:
            row['Timestamp'] = convert_timestamp(row['Timestamp'])
            row['ZIP'] = pad_zipcode(row['ZIP'])
            row['FullName'] = row['FullName'].upper()
            row['FooDuration'] = convert_duration(row['FooDuration'])
            row['BarDuration'] = convert_duration(row['BarDuration'])
            row['TotalDuration'] = total_duration(row['FooDuration'],
                                                  row['BarDuration'])
        except ParseError as err:
            sys.stderr.write(
                'Excluding line {} due to parsing error: {}\n'.format(reader.line_num, err)
            )
        else:
            writer.writerow(row)
