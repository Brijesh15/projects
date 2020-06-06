#export 192.168.1.10/24
#export 192.168.1.10/24
#export 192.168.1.10/24
list="$(ls -lR | grep ^d |grep tempjhdjhd | wc -l )"
echo $list
path="/opt/"
echo $path
j=3
count=5
i=$((17 + $((10*$((count -1))))))
echo $i
#list1="$(ls -lR | grep ^d )"
#echo $list1
#for i in 
#if [ $list1 -eq hh ]
#then 
#echo "h"
#else
#echo"nh"
#fi
while [ $count -gt 0 ]
do
#echo " mila"
if [ $j -eq $count ]
then
echo " mil gya"
d=$count
count=0
#last
fi
#echo "nh mila"
count=`expr $count - 1`
done
count=$d
echo $count
