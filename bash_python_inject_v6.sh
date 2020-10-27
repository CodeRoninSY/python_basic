#!/bin/bash
#
# bash_python_inject_v6.sh
# Inject python code block in bash script
# N.B.: Works only for "titanic_test" csv data
#
# Input & Data:
# function -> titanic(CSV_filename, X, Y, excelfileToWrite)
#-----------------------------------------------------------
# global variables
declare author="CodeRoninSY"
declare version="1.0"
declare verdate="<2020-10-19>"

# usage()
function usage() {
	echo "Usage:"
	echo "$(basename $0) -d <Col#1> <Col#2> <XlFilePrefix>"
	echo ":: <Col#1> = X"
	echo ":: <Col#2> = Y"
	echo ":: <XlFilePrefix> = Excel file prefix"
	echo " "
	echo "Dev: ${author}"
	echo "Coded: ${verdate}"
	echo "Execution: $(date)"
	exit 0
}

# titanic()
function titanic() {
f="$1" x="$2" y="$3" xlf="$4" python3 - <<END
import os
import csv
import pandas as pd
import matplotlib.pyplot as plt
import PySimpleGUI as sg

f = os.environ['f']
x = os.environ['x']
y = os.environ['y']
xlf = os.environ['xlf']

# default args
if xlf == "": xlf = "_test"

xlfx = xlf + ".xlsx"

print(f"f: {f}, x: {x}, y: {y}")
print(f"xlf: {xlf}, xlfx: {xlfx}")

# PySimpleGUI
sg.theme('DarkGrey1')

def table_example():
    filename = sg.popup_get_file('filename to open', \
					no_window=True, file_types=(("CSV Files","*.csv"),))
    # --- populate table with file contents --- #
    if filename == '':
        return
    data = []
    header_list = []
    button = sg.popup_yes_no('Does this file have column names already?')
    if filename is not None:
        with open(filename, "r") as infile:
            reader = csv.reader(infile)
            if button == 'Yes':
                header_list = next(reader)
            try:
                data = list(reader)  # read everything else into a list of rows
                if button == 'No':
                    header_list = ['column' + str(x) for x in range(len(data[0]))]
            except:
                sg.popup_error('Error reading file')
                return
    sg.set_options(element_padding=(0, 0))

    layout = [[sg.Table(values=data,
                            headings=header_list,
                            max_col_width=25,
                            auto_size_columns=True,
                            justification='right',
                            alternating_row_color='darkblue',
                            num_rows=min(len(data), 20))]]

    window = sg.Window('Table', layout, grab_anywhere=False)
    event, values = window.read()

    window.close()

table_example()

# CSV read & plots
layout = [
		[sg.Text('Filename')],
		[sg.Input(), sg.FileBrowse(file_types=
					(("CSV files", "*.csv"),))],
		[sg.OK(), sg.Cancel()]
	]

sg.popup('*** Titanic Data ***', auto_close=True, auto_close_duration=1)

window = sg.Window('Get csv filename', layout)

event, values = window.read()

window.close()

print(f"event: {event}, values: {values}")

# Read csv data and do plots
df = pd.read_csv(values[0])
# exlWrt = pd.ExcelWriter(xlfx)
df.to_excel(xlfx, sheet_name='Titanic', index=False,
			engine='xlsxwriter')

legnd = str(y) + " value"
print(f"legend: {legnd}")

fig = plt.figure(figsize=(10.0,8.0), dpi=100)
plt.xlabel(x)
plt.ylabel(y)
plt.title('Titanic Data')
lgd1 = plt.scatter(df[x], df[y], cmap='hsv', label=legnd)
plt.legend(handles=[lgd1], loc='best')
plt.savefig(xlf+".png")

END
}

# line()
function line {
PYTHON_ARG="$1" python - <<END
import os
line_len = int(os.environ['PYTHON_ARG'])
print('-' * line_len)
END
}

#----- MAIN -----
# getopts
while getopts ":hvd:" opt; do
	case ${opt} in
		h) # process -h
			usage
			exit 0
			;;
		v) # process -v version
			echo " "
			printf "%s Ver=%s\n" $(basename $0) ${version}
			echo " "
			exit 0
			;;
		d) # process -d data
			# check if enough args are input - At least $argv1 required!
			[ $# -lt 2 ] && {
				echo "Not enough args! $ARGV1 required." 1>&2; exit 1;
			}

			shift
			if [[ -z "$1" ]]; then
				K1="0"
				echo "K1: ${K1}"
			else
				K1="$1"
				echo "K1: ${K1}"
			fi

			shift
			if [[ -z "$1" ]]; then
				K2="8"
				echo "K2: ${K2}"
			else
				K2="$1"
				echo "K2: ${K2}"
			fi

			shift
			if [[ -z "$1" ]]; then
				xlFile="_test"
				echo "xlFile: ${xlFile}"
			else
				xlFile="$1"
				echo "xlFile: ${xlFile}"
			fi
			;;
		\?)
			echo "Invalid option: -$OPTARG" 1>&2
			usage
			exit 1
			;;
	esac
done
shift $((OPTIND-1))

echo $(line 80)

# csv data & header names
DATA_URL="test.csv"
argv=("PassengerId" "Pclass" "Name" "Sex" "Age" "SibSp" \
    "Parch" "Ticket" "Fare" "Cabin" "Embarked")

# call titanic
titanic $DATA_URL ${argv[$K1]} ${argv[$K2]} ${xlFile}

echo $(line 80)

exit 0
