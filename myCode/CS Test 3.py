import math
from datetime import date
import random
import time
from typing import List

def sqr_root() -> None:
    number: int = int(input("This function prints a square root. Enter a number (1-9999): "))
    square_root: float = round(math.sqrt(number), 1)
    print(f"The square root of {number} is {square_root}.")
    time.sleep(1)

def test_score() -> None:
    scores: str = input("Enter any number of test scores (0-100). Separate each by a space: ")
    scores_list: List[float] = [float(score) for score in scores.split()]
    total: float = sum(scores_list)
    average: float = round(total / len(scores_list), 1)
    print(f"The test average is {average}.")
    time.sleep(1)

def sales_tax() -> None:
    money: int = int(input("This function shows your sales tax, calculated at 7.5%. Enter the purchase amount (up to $10,000): "))
    tax: float = round(money * 0.075, 2)
    print(f"The sales tax of 7.5% on ${money} is ${tax}.")
    time.sleep(1)

def random_number() -> None:
    range_input: str = input("Enter two integers, separated by a space: ")
    range_list: List[int] = [int(x) for x in range_input.split()]
    random_num: int = random.randint(range_list[0], range_list[1])
    print(f"The random integer between {range_list[0]} and {range_list[1]} is {random_num}.")

def date_calculator() -> None:
    input_date: str = input("This function shows how many days there are between today and a date you enter. Enter a date in this format (mm dd yy): ")
    date_list: List[int] = [int(x) for x in input_date.split()]
    formatted_date: date = date(int(f"20{date_list[2]}"), date_list[0], date_list[1])
    days_diff: int = abs((formatted_date - date.today()).days)
    print(f"The number of days between {date_list[0]:02}/{date_list[1]:02}/{date_list[2]} and today is {days_diff}.")
    time.sleep(1)

def unit_converter() -> None:
    print("This function allows you to convert a metric unit to an imperial one. Choose a conversion method:")
    print("1. Kilometers to Miles")
    print("2. Kilograms to Pounds")
    print("3. Celsius to Fahrenheit")
    conversion_choice: str = input("> ")

    match conversion_choice:
        case '1':
            kilometers: float = float(input("Enter a number in Kilometers: "))
            miles: float = round(kilometers * 0.62137, 4)
            print(f"{kilometers} kilometer(s) is {miles} miles.")
        case '2':
            kilograms: float = float(input("Enter a number in Kilograms: "))
            pounds: float = round(kilograms * 2.20462, 4)
            print(f"{kilograms} kilogram(s) is {pounds} pounds.")
        case '3':
            celsius: float = float(input("Enter a number in °C: "))
            fahrenheit: float = round((celsius * 9/5) + 32, 4)
            print(f"{celsius}°C is {fahrenheit}°F.")
        case _:
            print("Invalid choice.")
    time.sleep(1)

def rps() -> None:
    print("This function allows you to play Rock Paper Scissors with a bot, as well as being able to track your score.")
    wins: int = 0
    losses: int = 0
    ties: int = 0
    total_games_played: int = 0
    playing_rps: bool = True

    while playing_rps:
        rps_input: str = input("Type in your choice r/p/s: ").lower()

        match rps_input:
            case 'r':
                rps_input = "rock"
            case 'p':
                rps_input = "paper"
            case 's':
                rps_input = "scissors"
            case _:
                print("Invalid input.")
                continue

        cpu_choice: str = random.choice(["rock", "paper", "scissors"])

        match (rps_input, cpu_choice):
            case (player, cpu) if player == cpu:
                print("It's a tie!")
                ties += 1
            case ("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
                print(f"You win! {rps_input} beats {cpu_choice}.")
                wins += 1
            case _:
                print(f"You lost. {cpu_choice} beats {rps_input}.")
                losses += 1

        total_games_played += 1
        play_again: str = input("Do you want to play again? Enter y/n: ").lower()
        if play_again == 'n':
            playing_rps = False

    win_rate: float = round(wins / total_games_played, 2) if total_games_played > 0 else 0.0
    print(f"After playing {total_games_played} games, you won {wins} time(s), lost {losses} time(s), and tied {ties} time(s). Your win rate is {win_rate}.")
    time.sleep(1)

def main_menu() -> None:
    menu_open: bool = True
    start_time: float = time.time()

    while menu_open:
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
        option: str = input("> ")

        match option:
            case '1':
                sqr_root()
            case '2':
                test_score()
            case '3':
                sales_tax()
            case '4':
                random_number()
            case '5':
                date_calculator()
            case '6':
                unit_converter()
            case '7':
                rps()
            case '8':
                menu_open = False
                end_time: float = time.time()
                time_elapsed: float = round(end_time - start_time, 0)
                minutes_elapsed: int = int(time_elapsed // 60)
                seconds_elapsed: int = int(time_elapsed % 60)
                charge: float = round((minutes_elapsed * 0.25 * 60) + (seconds_elapsed * 0.25), 2)
                print(f"Thank you. You used the system for {minutes_elapsed} minutes and {seconds_elapsed} seconds. You will be charged ${charge}.")
            case _:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()
