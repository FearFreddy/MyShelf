from datetime import datetime

def get_remaining_days_from_datetime(time):
    A = time.replace(hour = 0, minute = 0, second = 0, microsecond = 0)
    timezone_info = time.tzinfo
    B = datetime.now(timezone_info)
    if((A - B).days < 0):
        return -1
    return (A - B).days