#!/bin/bash

arr = $(cat './temp.txt')

for name in $(arr)
do
    echo $name
done
echo All done
