# HW_5B.py
# Read lat_lon_city_country.txt and answer questions

f = open("lat_lon_city_country.txt","r")
data = f.read()


locations = data.split("\n")
spliced = []
placeholder = ''
more_than_70_less_than_80_west_longitude = 0

for l in locations:
    l = l.strip()
    keep_data = l
    i = 0
    for c in l:
        l = l[1:len(l)-1]
        if c == 'W':
            longitude = int(keep_data.split()[1].split('°')[0])
            if longitude > 70 and longitude < 80:
                more_than_70_less_than_80_west_longitude += 1
                print(keep_data)
        else:
            placeholder += c
        i += 1
    
        
print(more_than_70_less_than_80_west_longitude)



f.close()