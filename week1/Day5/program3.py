#Program 3: Seconds to hours, minutes, seconds
#Plan: use // and %. Show as 01:02:05.

seconds = int(input("Enter the number of seconds:"))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60

print(f"{hours:02}:{minutes:02}:{remaining_seconds:02}")