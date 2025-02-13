# Crunch_Numbers.py

# Create an empty list and populate it from the file
nums = []
f = open("numbers.txt","r")
for line in f:
    n = float(line)
    nums.append(n)
f.close()

# Calculate the total and the average
total = 0
average = 0

for i in range(0, len(nums)):
    total += nums[i]
average = total / len(nums)

print(f"Total: {total}")
print(f"average: {average}")

# Write the sorted list
f = open("Sorted_Numbers.txt", "w")
for n in sorted(nums):
    f.write(f"{n}\n")
f.close()
