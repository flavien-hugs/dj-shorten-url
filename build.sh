#!/usr/bin/env bash
# exit on error
set -o errexit

make deps
./manage.py collectstatic --no-input
make migrate