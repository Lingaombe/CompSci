
i=2
j=50

while [ $i -le $j ]
do  
    t=$(($i%2))
    if [ $t == 0 ]
    then
        echo $i
    fi
    i=$(($i+1))
done