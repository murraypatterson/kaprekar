#!/bin/bash

for i in $(seq 5)
do
    echo "n=$i..."
    python3 fixpoints.py $i > $i.csv
done
