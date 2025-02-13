# Phone_Number_Cleanup.py

def format_phone_num(messy):
    clean = ""
    # Assume there are 10 digits somewhere in the string
    for i in range(0, len(messy)):
        ch = messy[i]
        if ch.isdigit():
            clean += ch
            if len(clean) == 3 or len(clean) == 7:
                clean += "-"
    return clean

phone_nums = []

f = open("phone_numbers_messy.txt","r")
for line in f:
    phone_nums.append(line)
f.close()

for i in range(0, len(phone_nums)):
    formatted = format_phone_num(phone_nums[i])
    print(formatted)
    phone_nums[i] = formatted

f = open("phone_numbers_clean.txt","w")
for i in range(0, len(phone_nums)):
    f.write(f"{phone_nums[i]}\n")

f.close()
