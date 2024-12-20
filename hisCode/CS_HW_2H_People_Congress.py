# CS_HW_2H_People_Congress
# Luke Norvell

# Open the file
f = open("usaconst.txt")

# Puts the file in a list
congress_list = f.read().split()

# Count the number of times "people" appears
# and the number of times "congress" appears
p = 0
c = 0

for line in congress_list:
    for word in line.split():
        if word.lower() == "people":
            p += 1
        elif word.lower() == "congress":
            c += 1    

# Display the results
print("The word 'People' appears ",p, " times.")
print("The word 'Congress' appears ",c, " times.")

# Close the file
f.close()