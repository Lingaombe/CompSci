echo enter a number
read n
d=$n
c=0
i=1
while [ $n -ge $i ]
do
    b=$(($n%$i))
    if [ $b == 0 ]
    then   
        c=$(($c+1))
    fi
    i=$(($i+1))
done

if [ $c -le 2 ]
then 
    echo $d is a prime number
else
    echo $d is not a prime number
fi