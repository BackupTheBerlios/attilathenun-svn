#! /bin/bash

## This script enables $Revision$ and $Date$ subversion's keywords
## for each .py file in the repository. 
## It make these keywords expands with their related values

find ./ -name "*.py" | xargs svn propset svn:keywords "Date Revision"
