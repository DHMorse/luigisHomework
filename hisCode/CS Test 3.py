# CS Test 3
# Luke Norvell


import math
from datetime import date
import random
import time

start_time = time.time()

def sqr_root():
    number = int(input("This function prints a square root. Enter a number (1-9999): "))
    sqr_root = round(math.sqrt(number),1)
    print("The square root of "+str(number)+" is "+str(sqr_root)+".")
    time.sleep(1)

def test_score():
    scores = input("Enter any number of test scores (0-100). Separate each by a space: ")
    scores_list = scores.split()
    total = 0
    for score in scores_list:
        total += float(score)
    average = round(total / len(scores_list),1)
    print("The test average is "+str(average)+".")
    time.sleep(1)


def sales_tax():
    money = int(input("This function shows your sales tax, calculated at 7.5%. Enter the purchase amount (up to $10,000): "))
    tax = round(money * 0.075, 2)
    print("The sales tax of 7.5% on $"+str(money)+" is $"+str(tax)+".")
    time.sleep(1)


def random_number():
    range = input("Enter two integers, separated by a space: ")
    range_list = range.split()
    random_number = str(random.randint(int(range_list[0]), int(range_list[1])))
    print("The random integer between "+(range_list[0])+" and "+(range_list[1])+" is "+(random_number)+".")


def date_caculator():
    input_date = input("This function shows how many days there are between today and a date you enter. Enter a date in this format (mm dd yy): ")
    date_list = input_date.split()
    formatted_date = date(int("20" + date_list[2]),int(date_list[0]),int(date_list[1]))
    if date.today() > formatted_date:
        days_diff = date.today() - formatted_date
    else:
        days_diff = formatted_date - date.today()
    print("The number of days between "+str((date_list[0]))+"/"+str((date_list[1]))+"/"+str((date_list[2]))+" and today is "+str(days_diff.days)+".")
    time.sleep(1)


def unit_converter():
    print("This function allows you to convert a metric unit to a imperial one. Choose an conversion method: ")
    print("1. Kilometers to Miles")
    print("2. Kilograms to Pounds")
    print("3. Celsius to Fahrenheit")
    conversion_choice = input("> ")
    if conversion_choice == '1':
        kilometers = int(input("Enter a number in Kilometers: "))
        miles = round(kilometers * 0.62137,4)
        print(str(kilometers)+"kilometer(s) is "+str(miles)+" miles.")
    if conversion_choice == '2':
        kilograms = int(input("Enter a number in Kilograms: "))
        pounds = round(kilograms * 0.453592,4)
        print(str(kilograms)+" kilogram(s) is "+str(pounds)+" pounds.")
    if conversion_choice == '3':
        celcius = int(input("Enter a number in °C: "))
        fahrenheit = round((celcius * 9/5) + 32,4)
        print(str(celcius)+"°C is "+str(fahrenheit)+"°F.")
    time.sleep(1)


def rps():
    print("This function allows you to play Rock Paper Scissors with a bot, as well as being able to track your score.")
    wins = 0
    losses = 0
    ties = 0
    total_games_played = 0
    playing_rps = True
    while (playing_rps):
        rps_input = input("Type in your choice r/p/s: ")
        if rps_input == 'r':
            rps_input = "rock"
        if rps_input == 'p':
            rps_input = "paper"
        if rps_input == 's':
            rps_input = "scissors"
        cpu_choice = random.randint(1, 3)
        if cpu_choice == 1:
            cpu_choice = "rock"
        if cpu_choice == 2:
            cpu_choice = "paper"
        if cpu_choice == 3:
            cpu_choice = "scissors"
        if cpu_choice == rps_input:
            print("It's a tie!")
            ties += 1
            total_games_played += 1
        elif (rps_input == "rock" and cpu_choice == "scissors") or (rps_input == "paper" and cpu_choice == "rock") or (rps_input == "scissors" and cpu_choice == "paper"):
            print("You win! "+rps_input+" beats "+cpu_choice+".")
            wins += 1
            total_games_played += 1
        else:
            print("You lost. "+cpu_choice+" beats "+rps_input+".")
            losses += 1
            total_games_played += 1

        play_again = input("Do you want to play again? Enter y/n: ")
        if play_again == 'n':
            playing_rps = False
            print("After playing "+str(total_games_played)+" games, you won "+str(wins)+" time(s), lost "+str(losses)+" time(s), and tied "+str(ties)+" time(s). You had an average win rate of "+str(round(wins/total_games_played, 1))+".")
            time.sleep(1)



menu_open = True

# Main menu controlled by "menu_open" boolean
while (menu_open):
    print('''
===============MENU==============
1. Square root calculator
2. Average test scores
3. Sales tax calculator
4. Random number
5. How many days?
6. Unit Converter
7. Rock Paper Scissors
8. Exit
Please choose an option.''')
    option = input("> ")
    if option == '1':
        sqr_root()
    if option == '2':
        test_score()
    if option == '3':
        sales_tax()
    if option == '4':
        random_number()
    if option == '5':
        date_caculator()
    if option == '6':
        unit_converter()
    if option == '7':
        rps()
    if option == '8':
        menu_open = False
        end_time = time.time()
        time_elapsed = round(end_time - start_time, 0)
        minutes_elapsed = int(time_elapsed / 60)
        seconds_elapsed = int(time_elapsed - (minutes_elapsed * 60))
        charge = (minutes_elapsed * (0.25 * 60)) + (seconds_elapsed * 0.25)
        print("Thank you. You used the system for "+str(minutes_elapsed)+" minutes and "+str(seconds_elapsed)+" seconds. You will be charged $"+str(charge)+".")
