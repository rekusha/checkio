def sun_angle(time):
    hours, minutes = time[:2], time[3:]
    angle_minutes, angle_hours = int(minutes)*0.25, (int(hours)-6)*15
    if 0 <= (angle_hours + angle_minutes) <= 180.0:
        time = angle_hours + angle_minutes
    else:
        time = "I don't see the sun!"
    return time

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("18:01"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert sun_angle("07:00") == 15
    #assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
