photos_time = int(input())
scenes_number = int(input())
scenes_time = int(input())

preparation = photos_time * 0.15
scenes_capture_time =scenes_number * scenes_time
time_need = preparation + scenes_capture_time

difference = abs(time_need - photos_time)
if time_need <= photos_time:
    print(f"You managed to finish the movie on time! You have {round(difference)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(difference)} minutes.")