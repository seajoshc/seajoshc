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
        # Create a dict with file name and content
        d = {}
        d[post.split("/")[1]] = InputFileContent(Path(post).read_text())

        # Create a new gist
        new_post = github_user.create_gist(True, d, post)

        # Parse Title out of blog post by searching for first "#"
        new_post_title = "Blog Post"  # Default title
        with open(post) as file:
            for line in file:
                if "#" in line:
                    new_post_title = line.split("#")[1].strip()
                    break

        # Write the new post details to our blog table
        with open("gists.md", "a") as gists:
            gists.write("| [{}]({}) | {} | {} |".format(
                new_post_title,
                new_post.html_url,
                new_post.created_at.strftime("%Y-%m-%d"),
                post)
            )

        print(" {}: {}".format(post, new_post.id))
    elif args.operation == "update":
        gist_id = ""
        # Read the gist URL from the blog table based on id (post)
        with open("gists.md") as gists:
            for line in gists:
                # parse out the gist ID
                if post in line:
                    gist_id = line.split(
                        "gist.github.com/")[1].split(")")[0]
                    break

        # Update the gist with the new content
        gist = g.get_gist(gist_id)
        gist.edit(description=post, files={post.split(
            "/")[1]: InputFileContent(Path(post).read_text())})

        print(" Updated Gist with ID {}".format(gist_id))
