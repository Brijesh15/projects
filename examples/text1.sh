#!/bin/bash
#num1=10
# sed '/unix/ s/unix/hello/ ' text.txt > text1.txt
#num= sed -n '/unix/=' text.txt
#echo $num

dirlist="$(ls -1)"
#echo $dirlist
for i in $(echo $dirlist | sed "s/\n / /g")
#for i in $(echo $dirlist )
do
echo "$i"
done
