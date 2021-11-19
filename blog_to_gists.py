#!/usr/bin/env python3
# Turn a blog into a bunch of gists

import argparse
import os
import requests
import sys


token = os.environ.get('GISTS_TOKEN')

parser = argparse.ArgumentParser()
parser.add_argument("operation", help="create or update")
parser.add_argument(
    "blog", help="Space delimited list of all files to upload to Gists.")
args = parser.parse_args()
print("Ok we gotttt\n {}\n {}".format(args.operation, args.blog))

r = requests.post('https://api.github.com/gists',
                  data={'key': 'value'})
