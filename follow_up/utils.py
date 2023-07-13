import datetime


def custom_id():
    current_datetime = datetime.datetime.now().strftime('%d%M%S')
    acct_no = current_datetime
    return acct_no
