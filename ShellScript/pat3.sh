i=6

while [ $i -gt 0 ]
do
    j=1
    while [ $j -lt $i ]
    do
        echo -n "$j "
        j=$(($j+1))
    done
    echo
    i=$(($i-1))
done