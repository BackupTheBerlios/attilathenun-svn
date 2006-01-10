#! /bin/bash

## This script enables $Revision$ and $Date$ subversion's keywords
## for each .py file in the src directory. 
## It make these keywords expands with their related values

find ./src -name "*.py" | xargs svn propset svn:keywords "Date Revision"
