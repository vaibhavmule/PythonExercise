

def calculate_angle(hour, minute):
    """
    Assuming 12 hours is 360 degree which is
    (720 minutes) or 0.5 degree per minute
    and 60 minutes = 360* which 6 degree per minutes.
    """
    if hour == 12 and minute == 60:
        hour, minute = 0, 0
    angle_of_hour_hand = (60 * hour + minute) / 2
    angle_of_minute_hand = 6 * minute
    angle = angle_of_hour_hand - angle_of_minute_hand
    if angle > 180:
        return abs(360 - angle)
    else:
        return angle


print(calculate_angle(12, 60))
