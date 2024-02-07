def check_coupon(entered_code, correct_code, current_date, expiration_date):
    
    month1, day1, year1 = current_date.split()
    month2, day2, year2 = expiration_date.split()
    
    months1 = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
        "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    
    month_number1 = months1[month1]
    
    months2 = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
        "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    
    month_number2 = months2[month2]
    
    day1 = int(day1.strip(","))
    year1= int(year1)
    
    day2 = int(day2.strip(","))
    year2= int(year2)
    
    if entered_code is correct_code:
        if year1 == year2:
            if month_number1 < month_number2 or (month_number1 == month_number2 and day1 <= day2):
                return True
            else:
                return False
        elif year1 < year2:
            return True
        else:
            return False
    else:
        return False
