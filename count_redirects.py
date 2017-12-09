#!/usr/bin/python -tt

import sys
import re

def find_date(filename):
  date_dict = {}
  f = open(filename)
  for line in f:
    match = re.search(r'\d\d/\w\w\w/\d\d\d\d', line)
    if match:
      date = match.group()
      date_dict[date] =1
  f.close()
  return sorted(date_dict.keys())

def count_dict(filename):
  dates = find_date(filename)
  word_count = {}
  f = open(filename, 'rU')
  for line in f:
    for date in dates:
      if date in line:
        if "GET" in line and "301" in line and "_escaped_fragment_" not in line:
            if date not in word_count:
              word_count[date] = 1
            else:
              word_count[date] = word_count[date] + 1
  f.close()
  return word_count

def count_redirects(filename):
  word_count = count_dict(filename)
  words = sorted(word_count.keys())
  for word in words:
    print word, word_count[word]

def main():
  count_redirects(sys.argv[1])

if __name__ == '__main__':
  main()