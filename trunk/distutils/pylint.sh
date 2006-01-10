# /bin/bash

pylint --color=y \
  --comment=y \
  --enable-basic=y \
  --enable-classes=y \
  --enable-design=y \
  --enable-exceptions=y \
  --enable-format=y \
  --enable-imports=y \
  --enable-miscellaneous=y \
  --enable-metrics=y \
  --enable-similarities=y \
  --enable-variables=y \
  --indent-string="\t" \
  --required-attributes=__revision__,__date__,__authors__ \
  --method-rgx=[a-z_][a-zA-Z0-9_]*$ \
  --variable-rgx=[a-z_][a-zA-Z0-9]*$ \
  --function-rgx=[a-z_][a-zA-Z0-9]*$ \
  --argument-rgx=[a-z][a-zA-Z0-9]*$ \
  --max-public-methods=25 \
  src.core.MOF
