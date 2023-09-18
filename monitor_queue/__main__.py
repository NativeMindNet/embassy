#import logging
from monitor_queue.browser import open_browser
from monitor_queue.args import get_args

#logging.basicConfig(filename='log/test.log', level=logging.INFO)


args=get_args()
print(args)



query = args.url
if len(query)<=0:
    query = f"about:blank"

id = args.id
if len(id)<=0:
    id = f"1"

#query = f"https://bangkok.kdmid.ru/queue/orderinfo.aspx?id=66583&cd=4ee5160d&ems=9AF34A78"

open_browser(query, id)