#export DISPLAY=:0

URL="https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66583&cd=4ee5160d&ems=9AF34A78"
#URL="https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66587&cd=3be13f2c&ems=E5084559"
LOG=log/583.log

python3 -m monitor_queue $URL 

#>> $LOG 2>&1


# | tee $LOG
# 
#2>&1
