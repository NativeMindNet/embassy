#export DISPLAY=:0

URL="https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66585&cd=ff6eaeda&ems=FA20485E"
ID=66585
LOG=log/66585.log
python3 -m monitor_queue $URL $ID

#>> $LOG 2>&1


# | tee $LOG
# 
#2>&1
