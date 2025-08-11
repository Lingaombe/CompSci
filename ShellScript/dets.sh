echo enter number of students
read n

while [ $n -ge 1 ]
do
    echo enter name
    read name
    echo enter email
    read email

    echo "$name|$email">>student.1st
    n=$(($n-1))
done
cat student.1st