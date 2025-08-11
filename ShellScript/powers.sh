i=1
n=1

while [ $n -le 1000 ]
do
    echo $n
    n=$((3**$i))
    i=$(($i+1))
done
