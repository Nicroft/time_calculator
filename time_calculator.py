def add_time(start, duration, start_day=None):
    # Parse start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    if period == "PM" and start_hour != 12:
        start_hour += 12

    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate total minutes
    total_minutes = start_hour * 60 + start_minute + duration_hour * 60 + duration_minute

    # Calculate days and remaining minutes
    days = total_minutes // (24 * 60)
    remaining_minutes = total_minutes % (24 * 60)

    # Calculate new hour and minute
    new_hour = remaining_minutes // 60
    new_minute = remaining_minutes % 60

    # Determine period (AM/PM)
    if new_hour < 12:
        new_period = "AM"
        if new_hour == 0:
            new_hour = 12
    else:
        new_period = "PM"
        if new_hour > 12:
            new_hour -= 12

    # Calculate day of the week if start_day is provided
    if start_day:
        start_day = start_day.lower().capitalize()
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        start_index = days_of_week.index(start_day)
        new_index = (start_index + days) % 7
        new_day = days_of_week[new_index]

    # Construct the result string
    result = f"{new_hour}:{new_minute:02} {new_period}"
    if start_day:
        if days == 1:
            result += f", {new_day} (next day)"
        elif days > 1:
            result += f", {new_day} ({days} days later)"
        else:
            result += f", {new_day}"
    else:
        if days == 1:
            result += " (next day)"
        elif days > 1:
            result += f" ({days} days later)"

    return result
