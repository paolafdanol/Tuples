filename = input("Introduce el nombre del archivo a analizar: ")

hour_count = {}

with open(filename, "r") as file:
    for line in file:
        if line.startswith("From "):
            words = line.split()
            time = words[5]
            hour = time.split(":")[0]
            if hour in hour_count:
                hour_count[hour] += 1
            else:
                hour_count[hour] = 1

for hour in sorted(hour_count.keys()):
    print(hour, hour_count[hour])
