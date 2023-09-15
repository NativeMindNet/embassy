#export DISPLAY=:0

URL="https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66583&cd=4ee5160d&ems=9AF34A78"
#URL="https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66587&cd=3be13f2c&ems=E5084559"
LOG=log/583.log
<<<<<<< HEAD

python3 -m monitor_queue $URL 

#>> $LOG 2>&1
=======
python3 -m monitor_queue $URL >> $LOG 2>&1
>>>>>>> e32707539d0acbad641a28614d8ad1b2202c1629


# | tee $LOG
# 
#2>&1
