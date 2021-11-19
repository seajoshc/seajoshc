#!/usr/bin/env python3
import sys
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("blog", help="List of all files in ./blogs to upload to Gists.")
args = parser.parse_args()
print("Ok we gotttt\n ", args.blog)
