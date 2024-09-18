days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def min(time):
    tod = time.split(' ')[1]
    hour = int(time.split(' ')[0].split(':')[0])
    minute = int(time.split(' ')[0].split(':')[1])
    if tod == 'AM':
        if hour != 12:
            return (hour*60 + minute)
        else:
            return minute
    if tod == 'PM':
        if hour != 12:
            return hour*60+minute+12*60
        else:
            return minute+12*60
        
def timestr(minutes):
        tod = ''
        hour = (minutes//60)%24
        minute = (minutes%60)

        if hour < 12:
            tod = 'AM'
        else:
            tod = 'PM'
            hour %= 12
        if hour == 0:
            hour = 12
        
        string = str(hour) + ':' + "{:02}".format(minute) + ' ' + tod
        return string

def add_time(start, duration, day = ''):
    new_time = ''
    start_minutes = min(start)
    duration_minutes = int(duration.split(':')[0])*60 + int(duration.split(':')[1])
    final_minutes = start_minutes + duration_minutes
    new_time = timestr(final_minutes)
    no_of_days = (final_minutes//60//24)%24
    if day:
        index = days.index(day.lower())
        if no_of_days != 0:
            index = (index+no_of_days)%7
        new_time += f', {days[index].capitalize()}'
    if no_of_days == 1:
        new_time += ' (next day)'
    elif no_of_days > 1:
        new_time += f' ({no_of_days} days later)'

    print(new_time)
    return new_time

add_time('2:59 AM', '24:00', 'saturDay')

add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# # Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# # Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# # Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# # Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# # Returns: 7:42 AM (9 days later)