from datetime import date, timedelta

def today(num=0):
    '''今日を中心に日付を取得する。'''
    today = date.today()
    day = timedelta(days=num)
    
    if num == 0:
        result = '今日'
    elif num == 1:
        result = '明日'
    elif num == -1:
        result = '昨日'
    else:
        result_date = today + day
        result = result_date.strftime('%Y年%m月%d日')

    return result
