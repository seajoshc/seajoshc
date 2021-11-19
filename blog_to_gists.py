#!/usr/bin/env python3
# Turn a blog into a bunch of gists

import argparse
import os
import sys
from pathlib import Path
from github import Github, Gist, InputFileContent


token = os.environ.get('GISTS_TOKEN')

parser = argparse.ArgumentParser()
parser.add_argument("operation", help="create or update")
parser.add_argument(
    "blog", help="Space delimited list of all files to upload to Gists.")
args = parser.parse_args()
print("Blog posts to process\n {}\n  {}".format(args.operation, args.blog))

g = Github(token)
github_user = g.get_user()

for post in args.blog.split(","):
    print("Processing {}".format(post))
    if args.operation == "create":
        d = {}
        d[post.split("/")[1]] = InputFileContent(Path(post).read_text())
        new_post = github_user.create_gist(True, d, post)
        print(" {}: {}".format(post, new_post.id))
    elif args.operation == "update":
        print("todo")
