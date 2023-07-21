filename = input("Introduce el nombre del archivo a analizar: ")

senders = {}

with open(filename, "r") as file:
    for line in file:
        if line.startswith("From:"):
            sender_email = line.split()[1]
            if sender_email in senders:
                senders[sender_email] += 1
            else:
                senders[sender_email] = 1

senders_list = [(count, email) for email, count in senders.items()]
senders_list.sort(reverse=True)

most_frequent_sender = senders_list[0]

print("La persona con más envíos es:", most_frequent_sender[1], "con", most_frequent_sender[0], "envíos.")
