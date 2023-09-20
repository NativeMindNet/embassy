#export DISPLAY=:0

#phuket
#NOTARY/PHUKET
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=1259&cd=83fc0856&ems=77564E7C" 1259 >>logs/phuket_notary.txt 2>>logs/phuket_notary.err &
sleep 61
#PASPORT/PHUKET
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=1258&cd=baff6793&ems=0C47474F" 1258 >>logs/phuket_pasport.txt 2>>logs/phuket_pasport.err &
sleep 61
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=765&cd=79fd11d2&ems=F5B642CE" 765  >>logs/phuket_conviction.txt 2>>logs/phuket_conviction.err &
sleep 61
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=667&cd=13a8e90a&ems=19864095" 667  >>logs/phuket_legalization.txt 2>>logs/phuket_legalization.err &
sleep 61



nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66585&cd=ff6eaeda&ems=FA20485E" 66585 &
sleep 61
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66587&cd=3be13f2c&ems=E5084559" 66587 &
sleep 61
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66586&cd=b682c23e&ems=B4814514" 66586 &
sleep 61
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66588&cd=c0056fab&ems=B590445F" 66588 &
sleep 61
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66589&cd=dbc1a5f3&ems=F62F41E1" 66589 &
sleep 61
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66584&cd=7d380255&ems=1C384C9B" 66584 &
sleep 61
nohup python3 -m monitor_queue "https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66582&cd=3da54122&ems=4FA54340" 66582 &
sleep 61
