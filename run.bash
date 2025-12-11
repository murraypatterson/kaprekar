#!/bin/bash

csv() {
    column -t -s, -n "$@" | less -F -S -X -K
}

generate() {
    for i in $(seq $1)
    do
	echo "n=$i..."
	python3 fixpoints.py $i > $i.csv
    done
}

display() {
    echo
    for i in $(seq $1)
    do
	echo "n=$i"
	csv $i.csv
	echo
    done
}

# Main
#----------------------------------------------------------------------

N=5
generate $N
display $N
