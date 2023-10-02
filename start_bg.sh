#export DISPLAY=:0

#./inet_mobile.sh

#BANGKOK

nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67053&cd=df568b77&ems=216E47E1" 67053 >>logs/bangkok_pasport5.txt 2>>logs/bangkok_pasport5.err  &
sleep 6
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67054&cd=bc214c88&ems=B7F84791" 67054 >>logs/bangkok_pasport10.txt 2>>logs/bangkok_pasport10.err  &
sleep 6

#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67053&cd=df568b77&ems=216E47E1
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67054&cd=bc214c88&ems=B7F84791
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67055&cd=21ec3ebd&ems=568E4C2B
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67050&cd=a6cd526a&ems=6041431B
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67051&cd=8e59d8e1&ems=BCEF4C44
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67052&cd=25f0d6b0&ems=CF8F4FDE

nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67470&cd=3a41a16c&ems=B52C4132" 67470 >>logs/bangkok_citizenship.txt 2>>logs/bangkok_citizenship.err  &
sleep 6
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67469&cd=2043f63c&ems=A4D642C0" 67469 >>logs/bangkok_zags.txt 2>>logs/bangkok_zags.err  &
sleep 6
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67472&cd=ef84a764&ems=823942AE" 67472 >>logs/bangkok_drv.txt 2>>logs/bangkok_drv.err  &
sleep 6
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67473&cd=4193547b&ems=64FD4F5A" 67473 >>logs/bangkok_fidelity.txt 2>>logs/bangkok_fidelity.err  &
sleep 6
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67476&cd=487c3362&ems=C4664A24" 67476 >>logs/bangkok_authencity.txt 2>>logs/bangkok_authencity.err  &
sleep 6
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67475&cd=5952092d&ems=DA854072" 67475 >>logs/bangkok_attorney.txt 2>>logs/bangkok_attorney.err  &
sleep 6
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67474&cd=298e183f&ems=DAD24AF0" 67474 >>logs/bangkok_other.txt 2>>logs/bangkok_other.err  &
sleep 6




#PHUKET
#NOTARY/PHUKET
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=1284&cd=9c838d60&ems=94504ED1" 1284 >>logs/phuket_notary.txt 2>>logs/phuket_notary.err &
sleep 6
#PASPORT/PHUKET
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=1283&cd=202d8241&ems=B76D4F0E" 1283 >>logs/phuket_pasport.txt 2>>logs/phuket_pasport.err &
sleep 6
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=765&cd=79fd11d2&ems=F5B642CE" 765  >>logs/phuket_conviction.txt 2>>logs/phuket_conviction.err &
sleep 6
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=667&cd=13a8e90a&ems=19864095" 667  >>logs/phuket_legalization.txt 2>>logs/phuket_legalization.err &
sleep 6






exit 0


