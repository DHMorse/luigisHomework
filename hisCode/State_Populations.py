# dictionary of state populations from the year 2000

populations = {
"Alabama":4452000,
"Alaska":627000,
"Arizona":5167000,
"Arkansas":2678000,
"California":33995000,
"Colorado":4328000,
"Connecticut":3412000,
"Delaware":786000,
"District of Columbia":572000,
"Florida":16047000,
"Georgia":8230000,
"Hawaii":1212000,
"Idaho":1300000,
"Illinois":12438000,
"Indiana":6092000,
"Iowa":2928000,
"Kansas":2693000,
"Kentucky":4049000,
"Louisiana":4469000,
"Maine":1277000,
"Maryland":5311000,
"Massachusetts":6363000,
"Michigan":9955000,
"Minnesota":4934000,
"Mississippi":2848000,
"Missouri":5606000,
"Montana":903000,
"Nebraska":1713000,
"Nevada":2018000,
"New Hampshire":1240000,
"New Jersey":8431000,
"New Mexico":1821000,
"New York":18998000,
"North Carolina":8079000,
"North Dakota":641000,
"Ohio":11364000,
"Oklahoma":3454000,
"Oregon":3431000,
"Pennsylvania":12286000,
"Rhode Island":1051000,
"South Carolina":4024000,
"South Dakota":756000,
"Tennessee":5703000,
"Texas":20946000,
"Utah":2244000,
"Vermont":610000,
"Virginia":7105000,
"Washington":5911000,
"West Virginia":1800007,
"Wisconsin":5374000,
"Wyoming":494000 }

highest_value = 0;
state_name = "";

for key in populations:
    if populations[key] > highest_value:
        highest_value = populations[key]
        state_name = key

print(state_name, highest_value)
