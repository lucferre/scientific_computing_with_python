def add_time(start_time, duration, day=False):
    # Create start time list [hh, mm, AM/PM]
    s_time = [int(x) for x in start_time[:-3].split(':')]
    # AM is False && PM is True
    if start_time[-2:] == 'AM':
        s_time.append(False)
    else:
        s_time.append(True)
    
    # Assign numeric value to day of week: 0-6 --> Mon - Sun    
    s_day_of_week = 0
    week_days_passed = 0
    if day:
        week_days_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        try:
            s_day_of_week = week_days_list.index(day.lower())
        except ValueError:
            print('Error: You entered an invalid day.')
                
    # Create duration list [hh, mm]
    d_time = [int(x) for x in duration.split(':')]
    
    # While there are hours or minutes left to add
    # s_time[0]: starting hours
    # s_time[1]: starting minutes
    # s_time[2]: AM / PM -- False / True
    # d_time[0]: duartion hours
    # d_time[1]: duration minutes
    while d_time[0] > 0 or d_time[1] > 0:
        if d_time[1] > 0:
            if s_time[1] < 59:
                s_time[1] += 1
                d_time[1] -= 1
            elif s_time[1] == 59:
                s_time[0] += 1
                s_time[1] = 0
                d_time[1] -= 1
        if d_time[1] == 0 and d_time[0] > 0:
            d_time[0] -= 1
            d_time[1] = 60
        # If we cross MIDNIGHT
        if s_time[0] == 12 and s_time[1] == 0 and s_time[2]:
            # Switch PM to AM
            s_time[2] = not s_time[2]
            # If it is NOT Sunday
            if s_day_of_week < 6:
                s_day_of_week += 1
            else:
                s_day_of_week = 0
            # Increse days passed count by 1
            week_days_passed += 1
        # If we cross MIDDAY
        elif s_time[0] == 12 and s_time[1] == 0 and not s_time[2]:
            # Switch AM to PM       
            s_time[2] = not s_time[2]
        # Change hour to 1 after hour 12 passes
        if s_time[0] == 13:
            s_time[0] = 1
                
    # Make string to return
    answer = ''
    # Append hour and :
    answer += str(s_time[0]) + ':'
    # Append minutes
    if s_time[1] > 9:
        answer += str(s_time[1])
    else:
        answer += '0' + str(s_time[1])
    # Append AM/PM
    if s_time[2]:
        answer += ' PM'
    else:
        answer += ' AM'
    # Append day of week
    if day:
        answer += ', ' + week_days_list[s_day_of_week].capitalize()
    if week_days_passed == 1:
        answer += ' (next day)'
    elif week_days_passed > 1:
        answer += " ({} days later)".format(week_days_passed)
        
    return answer
 
 
 
 
 
 
 
 
 
    
print(add_time('11:59 PM', '0:02'))