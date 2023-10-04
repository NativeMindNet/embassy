DELAY=36
#export DISPLAY=:0

#./inet_mobile.sh

#BANGKOK

nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67060&cd=70925fa4&ems=95BF4990" 67060 >>logs/bangkok_pasport5.txt 2>>logs/bangkok_pasport5.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67062&cd=93d02716&ems=9B0F4BE7" 67062 >>logs/bangkok_pasport10.txt 2>>logs/bangkok_pasport10.err  &
sleep $DELAY

#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67053&cd=df568b77&ems=216E47E1
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67054&cd=bc214c88&ems=B7F84791
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67055&cd=21ec3ebd&ems=568E4C2B
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67050&cd=a6cd526a&ems=6041431B
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67051&cd=8e59d8e1&ems=BCEF4C44
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67052&cd=25f0d6b0&ems=CF8F4FDE

nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67461&cd=3dc1b2bc&ems=F0CC42F9" 67461 >>logs/bangkok_citizenship.txt 2>>logs/bangkok_citizenship.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67462&cd=9d0358c3&ems=8CC044FE" 67462 >>logs/bangkok_zags.txt 2>>logs/bangkok_zags.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67463&cd=b1e59396&ems=902E4C5C" 67463 >>logs/bangkok_drv.txt 2>>logs/bangkok_drv.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67464&cd=d6d3cd09&ems=885D43DE" 67464 >>logs/bangkok_fidelity.txt 2>>logs/bangkok_fidelity.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67466&cd=add71cfa&ems=53154A16" 67466 >>logs/bangkok_authencity.txt 2>>logs/bangkok_authencity.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67484&cd=e6e397b1&ems=52E64FED" 67484 >>logs/bangkok_attorney.txt 2>>logs/bangkok_attorney.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67486&cd=de829581&ems=93CD4843" 67486 >>logs/bangkok_other.txt 2>>logs/bangkok_other.err  &
sleep $DELAY




#PHUKET
#NOTARY/PHUKET
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=1284&cd=9c838d60&ems=94504ED1" 1284 >>logs/phuket_notary.txt 2>>logs/phuket_notary.err &
sleep $DELAY
#PASPORT/PHUKET
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=1283&cd=202d8241&ems=B76D4F0E" 1283 >>logs/phuket_pasport.txt 2>>logs/phuket_pasport.err &
sleep $DELAY
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=765&cd=79fd11d2&ems=F5B642CE" 765  >>logs/phuket_conviction.txt 2>>logs/phuket_conviction.err &
sleep $DELAY
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=667&cd=13a8e90a&ems=19864095" 667  >>logs/phuket_legalization.txt 2>>logs/phuket_legalization.err &
sleep $DELAY






exit 0


