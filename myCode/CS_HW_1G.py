def simplify_algorithm(start_value: int) -> str:
    while len(str(start_value)) < 3:
        start_value **= 2
    return str(start_value)

if __name__ == "__main__":
    result: str = simplify_algorithm(5)
    print(result)
