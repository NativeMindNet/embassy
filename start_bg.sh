DELAY=36
#export DISPLAY=:0

#./inet_mobile.sh


#BANGKOK

nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=68224&cd=ed787cb4&ems=87A1480C;https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=68232&cd=87158c75&ems=1BD34343;https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=68209&cd=876e95d5&ems=770446E6" pasp5 >>logs/bangkok_pasport5.txt 2>>logs/bangkok_pasport5.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=68225&cd=0d2af16f&ems=C5B74FC2;https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=68233&cd=82761009&ems=84AC4EE3;https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=68210&cd=4c949824&ems=7DD74C96" pasp10 >>logs/bangkok_pasport10.txt 2>>logs/bangkok_pasport10.err  &
exit 0
sleep $DELAY


nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67793&cd=efc6eee7&ems=DBDE4999" 67793 >>logs/bangkok_attorney.txt 2>>logs/bangkok_attorney.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67791&cd=037cec88&ems=20C348DA" 67791 >>logs/bangkok_fidelity.txt 2>>logs/bangkok_fidelity.err  &
sleep $DELAY

nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67785&cd=578936fe&ems=FCD94A28" 67785 >>logs/bangkok_citizenship.txt 2>>logs/bangkok_citizenship.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67787&cd=f9e26a40&ems=D87C47D4" 67787 >>logs/bangkok_zags.txt 2>>logs/bangkok_zags.err  &
sleep $DELAY


nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67788&cd=0425ffa6&ems=8470408A" 67788 >>logs/bangkok_drv.txt 2>>logs/bangkok_drv.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67792&cd=13a6cd0c&ems=DA7542FF" 67792 >>logs/bangkok_authencity.txt 2>>logs/bangkok_authencity.err  &
sleep $DELAY
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67794&cd=76abe61f&ems=631443FF" 67794 >>logs/bangkok_other.txt 2>>logs/bangkok_other.err  &
sleep $DELAY


#exit 0


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



#exit 0


#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67053&cd=df568b77&ems=216E47E1
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67054&cd=bc214c88&ems=B7F84791
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67055&cd=21ec3ebd&ems=568E4C2B
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67050&cd=a6cd526a&ems=6041431B
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67051&cd=8e59d8e1&ems=BCEF4C44
#https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67052&cd=25f0d6b0&ems=CF8F4FDE












exit 0


