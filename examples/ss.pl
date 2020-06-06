$path = "/home/brijesh/Python/";
#$exist = `ls  $path  | grep  temp `;
$exist=`ls -lR $path | grep ^d| grep templ| wc -l`;
#ls -l  | grep -c ^d
#$e = 50;
#$exist = 30;
print  "exit = $exist\n";
#print  "e = $e\n";
$dd =12;
$cc =13;
$ff =$dd+$cc;
print "$ff";
