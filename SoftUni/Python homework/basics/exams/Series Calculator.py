from math import floor

serial_name = input()
seasons_number = int(input())
episodes_number = int(input())
standard_episode_time = float(input())

episode_time = standard_episode_time * 0.20 + standard_episode_time
additional_special_series = seasons_number * 10
total_time = episode_time * episodes_number * seasons_number + additional_special_series

print(f"Total time needed to watch the {serial_name} series is {floor(total_time)} minutes.")
