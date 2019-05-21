#!/bin/bash

function line {
PYTHON_ARG="$1" python - <<END
import os
line_len = int(os.environ['PYTHON_ARG'])
print('-' * line_len)
END
}

line 80

echo "Handy"

echo $(line 80)
