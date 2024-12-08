import calendar
from datetime import date, timedelta

def get_all_mondays(year):
    result = []

    for month_num in range(1, 13):
        # количество дней в месяце
        d_count = list(calendar.monthrange(year, month_num))[-1]
        
        result.append([date(year, month_num, day) for day in range(1, d_count+1) if calendar.weekday(year, month_num, day) == 3][2])
    return result        
        
    
    
print(*get_all_mondays(2021), sep='\n')