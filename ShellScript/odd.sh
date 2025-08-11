i=2

while [ $i -le 50 ]
do
    t=$(($i%2))
    if [ $t == 1 ]
    then
        echo $i
    fi
    i=$(($i+1))
done