#! /bin/bash
find ./ -name "*.pyc" | xargs rm -f
find ./ -name "*~" | xargs rm -f

rm -rf doc/api/*
