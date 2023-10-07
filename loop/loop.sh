#!/bin/bash

URL="https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=67051&cd=8e59d8e1&ems=BCEF4C44"
LOG_FILE="load_times.log"
INTERVAL_SECONDS=5  # Интервал между запросами в секундах

while true; do
  start_time=$(date +"%Y-%m-%d %H:%M:%S")
  response_time=$(curl -o /dev/null -s -w "%{time_total}\n" "$URL")
  end_time=$(date +"%Y-%m-%d %H:%M:%S")

  echo "$start_time ; $response_time"
  echo "$start_time ; $response_time"  >> "$LOG_FILE"
  
  sleep $INTERVAL_SECONDS
done