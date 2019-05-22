#!/bin/bash

function line {
PYTHON_ARG="$1" python - <<END
import os
line_len = int(os.environ['PYTHON_ARG'])
print('-' * line_len)
END
}

function to_upper() {
P1="$1" P2="$2" python - <<EOF
import os
p1 = os.environ['P1'].upper()
p2 = os.environ['P2'].upper()
print(f"{p1} {p2}")
EOF
}

to_upper lensman kim

st=$(date +%s.%N)

line 80

echo "Handy"

echo $(line 80)

sleep 3
end=$(date +%s.%N)
ds=$(echo "$end - $st" | bc -l)

# var
awk -v d="$ds" 'BEGIN {print "delta_s: " d/60.0 " min."}'
# here-doc
awk '{print "delta_ds: " $0 " sec."}' <<< "$ds"
# ARGV
awk 'BEGIN {print ARGV[1]}' "$ds"
# ENVIRON
export ds
awk 'BEGIN{print ENVIRON["ds"]}'