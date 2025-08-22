i=1
while [ $i -lt 6 ]
do
    j=$i
    while [ $j -gt 0 ]
    do 
        echo -n "$j"
        j=`expr $j+1`
    done
    echo 
    i=`expr $i+1`
done