#export DISPLAY=:0

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
#phuket
#pasp
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=766&cd=ed9af65d&ems=2F864BE9" 766 &
sleep 61
#dover
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=669&cd=d4e39dae&ems=33D54E3B" 669 &
sleep 61
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=765&cd=79fd11d2&ems=F5B642CE" 765 &
sleep 61
nohup python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=667&cd=13a8e90a&ems=19864095" 667 &


