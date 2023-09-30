with open("today.txt", "w",) as file:
    file.write("2023-09-30")

with open("today.txt", "r") as file:
    today_string = file.read().strip()


from datetime import datetime

# Suppose today_string has been previously populated from the file
# today_string = "2023-09-30"

date_object = datetime.strptime(today_string, "%Y-%m-%d")
