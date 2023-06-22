# https://www.codewars.com/kata/52742f58faf5485cae000b9a
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way. The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds. It is much easier to understand with an example:
# For the purpose of this Kata, a year is 365 days and a day is 24 hours. Note that spaces are important.
# Detailed rules: 

""" The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time. """

# Example: 
""" * For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds" """

def form_duration(seconds):
    form = ''
    year = 31536000 #seg
    day = 86400 #seg
    hour = 3600 #seg
    min = 60 #seg
    
    def year_constructor(seconds,form,year,day,hour,min):
        years = seconds//year
        exc = seconds-(year*years)
        form = f'{years} year' if years == 1 else f'{years} years' 
        
        if exc >= day:
            form += f', {day_constructor(exc, form, day,hour,min)}'
        elif exc >= hour and exc < day:
            form += f', {hour_constructor(exc,form, hour,min)}'
        elif exc >= min and exc < hour:
            form += f', {minute_constructor(exc,form,min)}'
        elif exc < 60:
            form += f' and {second_constructor(exc,form)}'
        return form
    
    def day_constructor(seconds,form,day,hour,min):
        days = seconds//day
        exc = seconds-(days*day)
        form = f'{days} day' if days == 1 else f'{days} days'
        
        if exc >= hour:
            form += f', {hour_constructor(exc, form, hour,min)}'
        elif exc >= min and exc < hour:
            form += f', {minute_constructor(exc,form,min)}'
        elif exc < 60:
            form += f' and {second_constructor(exc,form)}'
        return form
    
    def hour_constructor(seconds,form,hour,min):
        hours = seconds//hour
        exc = seconds-(hours*hour)
        form = f'{hours} hour' if hours == 1 else f'{hours} hours'

        if exc >= min:
            form += f', {minute_constructor(exc, form, min)}'
        elif exc > 0:
            form += f' and {second_constructor(exc,form)}'
        return form

    def minute_constructor(seconds,form, min):
        mins = seconds//min
        exc = seconds-(mins*min)
        form = f'{mins} minute' if mins == 1 else f'{mins} minutes'

        if exc < 60:
            form += f' and {second_constructor(exc, form)}'
        return form
    
    def second_constructor(seconds,form):
        form = f'{seconds} second' if seconds == 1 else f'{seconds} seconds' 
        return form  
    
       
    if seconds >= year:
        return year_constructor(seconds,form, year,day,hour,min)     
    elif seconds >= day and seconds < year:        
        return day_constructor(seconds,form, day,hour,min) 
    elif seconds >= hour and seconds < day:        
        return hour_constructor(seconds,form,hour,min)
    elif seconds >= min and seconds < hour:        
        return minute_constructor(seconds,form,min)
    else:
        return second_constructor(seconds,form)

# Pruebas en consola / Test cases
print(form_duration(101956166))
print(form_duration(3662))
print(form_duration(3600))
print(form_duration(62))
print(form_duration(1))