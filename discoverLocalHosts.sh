sudo ./pingSweeper.sh $1 |xargs -n1 -I 'ip' sh -c 'printf "================== OS detection for IP: ip\n"; nmap -O --osscan-guess "ip"|grep "MAC\|Running\|OS "; echo "\n"'
