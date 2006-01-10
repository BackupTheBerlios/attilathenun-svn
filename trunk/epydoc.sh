#! /bin/bash

find ./src/ -name "*.py" | xargs epydoc --output doc/api --html
