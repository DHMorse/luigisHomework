from typing import Tuple

def getUserAge() -> int:
    while True:
        try:
            userInputAge: int = int((input("Enter your age: ")))
            if userInputAge <= 0:
                raise ValueError("Age must be greater than 0.")
            break
        except Exception as e:
            print(e)
    return userInputAge

def getUserWeight() -> int:
    while True:
        try:
            userInputWeight: int = int((input("Enter your weight in lbs: ")))
            if userInputWeight <= 0:
                raise ValueError("Weight must be greater than 0.")
            break
        except Exception as e:
            print(e)
    return userInputWeight

def canRideRollerCoaster(age: int, weight: int) -> bool:
    if age >= 10 or weight >= 70:
        return True
    else:
        return False

def canEnist(age) -> Tuple[bool, str]:
    if age >=17 and age <= 39:
        return (True, "You may enlist.")
    elif age < 17:
        return (False, f"You are too young to enlist. Please try again in {str(17-age)} years.")
    elif age >39:
        return (False, "You are too old to enlist")

def main() -> None:
    userAge: int = getUserAge()
    userweight: int = getUserWeight()
    
    canRide: bool = canRideRollerCoaster(userAge, userweight)
    if canRide:
        print("You may ride this roller coaster")
    else:
        print("Please find a more suitable ride.")

    userCanEnlist: Tuple[bool, str] = canEnist(userAge)
    print(userCanEnlist[1])

if __name__ == '__main__':
    main()