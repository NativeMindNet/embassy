#export DISPLAY=:0

URL="https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66586&cd=b682c23e&ems=B4814514"
ID=66586
LOG=log/66586.log
python3 -m monitor_queue $URL $ID

#>> $LOG 2>&1


# | tee $LOG
# 
#2>&1
