# wordlethon #
Simple commandline wordle clone written in Python (3.9.6)
Using `colorama` for command line coloring.

The dictionaries are scraped using [this tool](https://github.com/benjihillard/English-Dictionary-Database/blob/main/english%20Dictionary.csv) and are in no way filtered, except by word length and alphabetical-ness.

## Execution ##
Install python3 and make sure the library `colorama` is installed.

Then run from commandline (assuming PATH is setup for `python`):

`$ python wordlethon.py`

The recommended word length is 5, but you may try the harder ones at your own risk.

## Future ideas ##

 - Better dictionary (obviously)
 - Different options for how hints are shown
 - Scoring options
 - Different play styles