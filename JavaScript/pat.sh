#!/bin/bash

i=0

while [ $i -lt 5 ]
do
    b=$i
    while [ $b -ge 0 ]
    do  
        echo -n "*"
        b=$(($b-1))
    done
    echo
    i=$(($i+1))
done