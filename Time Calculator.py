# FCC Project - Time Calculator
# Instructions found at:
# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/time-calculator 

# - Write a function named add_time that takes in two required parameters and one 
#   optional parameter:

#     - a start time in the 12-hour clock format (ending in AM or PM)
#     - a duration time that indicates the number of hours and minutes
#     - (optional) a starting day of the week, case insensitive

# - The function should add the duration time to the start time and return the result.

# - If the result will be the next day, it should show (next day) after the time. 
# - If the result will be more than one day later, it should show (n days later) 
#   after the time, where "n" is the number of days later.

# - If the function is given the optional starting day of the week parameter, 
#   then the output should display the day of the week of the result. The day of 
#   the week in the output should appear after the time and before the number of days later.

# - Below are some examples of different cases the function should handle. Pay 
#   close attention to the spacing and punctuation of the results.

# add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

# add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

# add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

# add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

# add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

# add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)



def add_time(start, duration, day=None):

    # List of days of the week
    week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday')

    # Split hours and minutes 
    start = start.split()
    midday = start[1]
    time = start[0].split(':')
    duration = duration.split(':')

    # Convert to integers
    start_hours = int(time[0])
    start_minutes = int(time[1])

    add_hours = int(duration[0])
    add_minutes = int(duration[1])

    # Calculate time
    final_minutes = start_minutes + add_minutes
    final_hours = start_hours + add_hours + (add_minutes - (add_minutes % 60)) // 60

    # Carry over hours if minutes >= 60
    if final_minutes >= 60:
        final_hours += final_minutes // 60
        final_minutes = final_minutes % 60

    # Count days
    count_days = 0 + (add_hours + (add_minutes - (add_minutes % 60)) // 60) // 24

    # Calculate AM/PM
    if final_hours >= 12:
        final_hours = final_hours % 12
        if final_hours == 0:
            final_hours = 12
        if add_hours == 24 and add_minutes == 0:
            pass
        elif midday == 'AM':
            midday = 'PM'
        else: 
            midday = 'AM'
            count_days += 1
    
    # Format for minutes < 10
    if final_minutes < 10:
        final_minutes = "0" + str(final_minutes)

    # Format Output | 12:03 AM, Thursday (2 days later)     
    output = str(final_hours) + ':' + str(final_minutes) + ' ' + midday

    # Format days if needed
    if count_days == 1 and day == None:
        count_days = ' (next day)'
        output += count_days
    elif count_days == 0 and day != None:
        output += ', ' + day
    elif count_days > 1 and day == None:
        output += ' (' + str(count_days) + ' days later)'
    
    # Find day of the week
    elif count_days >= 1 and day != None:
        i = 0
        for days in week:
            if day.title() == days:
                temp = (i + count_days) % 7
                index = week[temp]
                if 7 - abs(temp - i) == 1:
                    output += ', ' + index + ' (next day)'
                else:
                    output += ', ' + index + ' (' + str(count_days) + ' days later)'
            else: 
                i += 1

    print(output)
    return output

print('Test 1 starting...')
assert(add_time("3:00 PM", "3:10") == "6:10 PM")
assert(add_time("11:30 AM", "2:32", "Monday") == "2:02 PM, Monday")
assert(add_time("11:43 AM", "00:20") == "12:03 PM")
assert(add_time("10:10 PM", "3:30") == "1:40 AM (next day)")
assert(add_time("11:43 PM", "24:20", "tueSday") == "12:03 AM, Thursday (2 days later)")
assert(add_time("6:30 PM", "205:12") == "7:42 AM (9 days later)")
print('Test 1 passed!\n---------')

print('Test 2 starting...')
assert(add_time("8:16 PM", "466:02", "tuesday") == "6:18 AM, Monday (20 days later)")
assert(add_time("2:59 AM", "24:00", "saturDay") == "2:59 AM, Sunday (next day)")
assert(add_time("2:59 AM", "24:00") == "2:59 AM (next day)")
print('Test 2 passed!')