#!/usr/bin/env python3
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("operation", help="create or update")
parser.add_argument(
    "blog", help="Space delimited list of all files to upload to Gists.")
args = parser.parse_args()
print("Ok we gotttt\n {}\n {}".format(args.operation, args.blog))
