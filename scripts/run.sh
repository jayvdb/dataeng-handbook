#!/bin/bash

set -euo pipefail

cp scripts/Gemfile docs

cd docs

bundle install 
bundler exec jekyll serve --host 0.0.0.0