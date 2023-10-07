#export DISPLAY=:0

#nohup
python3 -m monitor_queue "https://phuket.kdmid.ru/queue/orderinfo.aspx?id=1284&cd=9c838d60&ems=94504ED1" 1284 
#>>logs/phuket_notary.txt 2>>logs/phuket_notary.err &
