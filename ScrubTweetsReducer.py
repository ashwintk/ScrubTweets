#!/usr/bin/env python

import sys

current_tweet = None
tweet = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    strArray= line.split("\t")
    tweet = strArray[0]
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_tweet == tweet:
        continue
    else:
        if current_tweet is not None:
            # write result to STDOUT
            print '%s' % (current_tweet)
        current_tweet = tweet

# do not forget to output the last word if needed!
if current_tweet == tweet:
    print '%s' % (current_tweet)
