from .models import RequestList

from datetime import date
from datetime import datetime
from datetime import timedelta

def gen_ticket_number():
    today = date.today()
    year = today.year
    
    last_request = RequestList.objects.latest('request_creation_date')

    if last_request.ticket_number is None:
          return f'{year}-001'

    prev_ticket = last_request.ticket_number.split('-')
    prev_ticket[0] = int(prev_ticket[0])
    prev_ticket[1] = int(prev_ticket[1])

    if year != prev_ticket[0]:
        return f'{year}-001'
    
    ticket_no = str(prev_ticket[1] + 1)
    while len(ticket_no) < 3:
        ticket_no = '0' + ticket_no

    return f'{year}-{ticket_no}'

def calc_ret_date(event_end, report_lifecycle):
    return event_end + timedelta(report_lifecycle)
     
def calc_req_num():
    last_request = RequestList.objects.latest('request_creation_date')
    return last_request.request_number + 1
