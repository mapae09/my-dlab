from datetime import datetime, timedelta

def get_base():
    now = datetime.now()
    if now.minute<=40:
        now -= timedelta(hours=1)

    base_date=now.strftime("%Y%m%d")
    base_time=now.strftime("%H00")
    return base_date, base_time


if __name__=='__main__':
    print(get_base())
