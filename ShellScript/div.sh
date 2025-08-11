echo enter number
read n
t=$(($n%5))
if [ $t == 0 ]
then
    echo $n is divisible by 5
else
    echo $n is not divisible by 5
fi