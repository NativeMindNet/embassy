#export DISPLAY=:0

URL="https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66588&cd=c0056fab&ems=B590445F"
ID=66588
LOG=log/66588.log
python3 -m monitor_queue $URL $ID

#>> $LOG 2>&1


# | tee $LOG
# 
#2>&1
