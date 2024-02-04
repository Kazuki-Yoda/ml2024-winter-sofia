def main():
    print("Type the number of inputs (positive integer):")
    n = input_positive_integer()

    print(f"provide {n} numbers one by one:")
    numbers = [input_integer() for _ in range(n)]

    print("Type an integer to search, and the index will be given:")
    x = input_integer()

    index = search_index(numbers, x)
    print(index)

def search_index(numbers, x):
    try:
        return numbers.index(x) + 1 # 1-indexed
    except ValueError:
        return -1

def input_integer() -> int:
    while True:
        input_str = input()
        
        try:
            n = int(input_str)
            return n
        except ValueError: # Cast failed
            print(f"Input must be an integer but was '{input_str}'. Try again.")
            continue

def input_positive_integer() -> int:
    while True:
        n = input_integer()

        if n > 0:
            return n
        else:
            print(f"Input integer must be positive but was {n}. Try again.")

if __name__ == "__main__":
    main()
