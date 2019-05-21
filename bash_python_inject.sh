#!/bin/bash

function current_datetime {
python - <<END
import datetime
print(datetime.datetime.now())
END
}

current_datetime

DT=$(current_datetime)
echo "Current date and time: $DT"
