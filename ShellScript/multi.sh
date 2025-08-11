#!/bin/bash

echo enter number 
read num
i=1
m=13
while [ $i -lt $m ]
do
    res=$(($num*$i))
    echo "$num * $i = $res"
    i=$((1+$i))
done