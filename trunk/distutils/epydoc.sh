#! /bin/bash

find ./attila/ -name "*.py" | xargs epydoc --output doc/api --html
