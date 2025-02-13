# Create_JSON_File.py

import json
f = open("track_meet.txt", "r")

# Create an empty list to hold the participants
# Each participant will be a dictionary object

participants = []

for line in f:
    items = line.split(',')
    # Get the last name, first name, age, and the events, and strip any whitespaces
    last_name = items[0].strip()
    first_name = items[1].strip()
    age = int(items[2].strip())

    # Create an empty list to hold the events
    events = []
    for i in range(3, len(items)):
        event = items[i].strip()
        events.append(event)

    # Put all of these into a dictionary
    d = { "Last Name" : last_name,
          "First Name" : first_name,
          "Age" : age,
          "Events" : events }

    # Add this dictionary to the list of participants
    participants.append(d)

f.close()

# Now write this data to a JSON file
f = open("track_meet.json", "w")
json.dump(participants, f, indent=2)
f.close()
print("Done!")
