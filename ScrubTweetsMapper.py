#!/usr/bin/env python

import json, sys, re

sys.path.append('./')

import TweetsLib as tlib

for line in sys.stdin:
    try:
        # Load Tweets
        parsed_json_tweets = json.loads(line)
        # Extract date created
        this_tweet_timestamp = parsed_json_tweets['created_at'].lstrip().strip()
        # Extract user handle
        this_user_handle = parsed_json_tweets['user']['screen_name'].lstrip().strip()
        # Extract tweet text
        tweet_text = parsed_json_tweets['text'].lstrip().strip()
        if tweet_text != "":
            # Remove new line and carriage return
            tweet_text = tlib.stripNewLineAndReturnCarriage(tweet_text)
            # Remove URL's & User Mentions
            tweet_text = tlib.removeURL(tweet_text)
            tweet_text = tlib.removeUserMentions(tweet_text)
            # Replace sequence of repeated characters by three characters
            tweet_text = tlib.replaceRepeatedCharacters(tweet_text)
            # Convert multiple white spaces to a single white space
            tweet_text = tlib.convertMultipleWhiteSpacesToSingleWhiteSpace(tweet_text)
            # Replace hashtags with words
            tweet_text = tlib.replaceHashTagsWithWords(tweet_text)
            # Remove double quotes
            tweet_text = re.sub(r'([^\s\w]|_)', '', tweet_text)
            # Trim the tweet text
            tweet_text = tweet_text.strip().lstrip().lower()
            if tweet_text.strip().lstrip() != "":
                print "%s\t1" % (tweet_text)
    except ValueError:
        continue
