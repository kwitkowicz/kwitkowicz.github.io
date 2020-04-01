#!/bin/bash
set -e
pelican content -o output -s pelicanconf.py
ghp-import -m "Update site" output
git push origin gh-pages:master
git push origin dev:dev
