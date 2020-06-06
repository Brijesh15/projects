a=0
j=1
i=2
echo "enter the instances"
read reply
net_a=11
net_b=15
net_f=17
net_d=20
net_dd=80
mgmt=254
while [ $j -lt $reply ]
do 
net_a1=$((net_a+10))
net_b1=$((net_b+10))
net_f1=$((net_f+10))
net_d1=$((net_d+1))
net_dd1=$((net_dd+1))
mgmt1=$((mgmt-1))
#echo $mgmt1
sed  "s/192.168."$net_a".10/192.168."$net_a1".10/g"   /home/brijesh/project/hae/script/a$j.sh > /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_a"::10/fc00:1234:"$net_a1"::10/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_a".120/192.168."$net_a1".10/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_a"::120/fc00:1234:"$net_a1"::120/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_a".210/192.168."$net_a1".210/g"    /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_a"::210/fc00:1234:"$net_a1"::210/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_a".41/192.168."$net_a1".41/g"    /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_b".10/192.168."$net_b1".10/g"    /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_b"::10/fc00:1234:"$net_b1"::10/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_b".210/192.168."$net_b1".210/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_b"::210/fc00:1234:"$net_b1"::210/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_b".20/192.168."$net_b1".20/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_b"::20/fc00:1234:"$net_b1"::20/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_b".220/192.168."$net_b1".220/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_b"::220/fc00:1234:"$net_b1"::220/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_b".21/192.168."$net_b1".21/g"    /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_b"::21/fc00:1234:"$net_b1"::21/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_b".22/192.168."$net_b1".22/g"    /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_b"::22/fc00:1234:"$net_b1"::22/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".11/192.168."$net_f1".11/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::11/fc00:1234:"$net_f1"::11/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".12/192.168."$net_f1".12/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::12/fc00:1234:"$net_f1"::12/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".30/192.168."$net_f1".30/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::30/fc00:1234:"$net_f1"::30/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".31/192.168."$net_f1".31/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::31/fc00:1234:"$net_f1"::31/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".40/192.168."$net_f1".40/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::40/fc00:1234:"$net_f1"::40/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".41/192.168."$net_f1".41/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::41/fc00:1234:"$net_f1"::41/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".42/192.168."$net_f1".42/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::42/fc00:1234:"$net_f1"::42/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".70/192.168."$net_f1".70/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::70/fc00:1234:"$net_f1"::70/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".130/192.168."$net_f1".130/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::130/fc00:1234:"$net_f1"::130/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".200/192.168."$net_f1".200/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::200/fc00:1234:"$net_f1"::200/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".32/192.168."$net_f1".32/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::32/fc00:1234:"$net_f1"::32/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$net_f".40/192.168."$net_f1".40/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:"$net_f"::40/fc00:1234:"$net_f1"::40/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168.4."$net_d"/192.168.4."$net_d1"/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168.4."$net_d"/192.168.4."$net_d1"/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:4::"$net_d"/fc00:1234:4::"$net_d1"/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168.4."$net_dd"/192.168.4."$net_dd1"/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/fc00:1234:4::"$net_dd"/fc00:1234:4::"$net_dd1"/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".40/192.168."$mgmt1".40/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".10/192.168."$mgmt1".10/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".210/192.168."$mgmt1".210/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".30/192.168."$mgmt1".30/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".71/192.168."$mgmt1".71/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".23/192.168."$mgmt1".23/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".31/192.168."$mgmt1".31/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".50/192.168."$mgmt1".50/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".51/192.168."$mgmt1".51/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".52/192.168."$mgmt1".52/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".40/192.168."$mgmt1".40/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".41/192.168."$mgmt1".41/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".42/192.168."$mgmt1".42/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".2/192.168."$mgmt1".2/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".20/192.168."$mgmt1".20/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt"220/192.168."$mgmt1".220/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".80/192.168."$mgmt1".80/g"  /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".120/192.168."$mgmt1".120/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".130/192.168."$mgmt1".130/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".150/192.168."$mgmt1".150/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".110/192.168."$mgmt1".110/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".90/192.168."$mgmt1".90/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".21/192.168."$mgmt1".21/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".22/192.168."$mgmt1".22/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".160/192.168."$mgmt1".160/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".32/192.168."$mgmt1".32/g"   /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".100/192.168."$mgmt1".100/g" /home/brijesh/project/hae/script/a$i.sh
sed -i "s/192.168."$mgmt".101/192.168."$mgmt1".101/g" /home/brijesh/project/hae/script/a$i.sh

j=$((j+1))
i=$((i+1))
#a=$((j-1))
net_a=$((net_a+10))
net_b=$((net_b+10))
net_f=$((net_f+10))
net_d=$((net_d+1))
net_dd=$((net_dd+1))
mgmt=$((mgmt-1))
done

