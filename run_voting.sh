#!/bin/bash

for i in 1 10 100 1000
do
    echo "Running $i voting"
    ./main.py "$i" > vote_"$i".dat
done
