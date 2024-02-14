class SearchList:
    """
    The program asks the user for input N (positive integer) and reads it.

    Then the program asks the user to provide N numbers (one by one)
    and reads all of them (again, one by one).

    In the end, the program asks the user for input X (integer)
    and outputs: "-1" if there were no such X among N read numbers,
    or the index (from 1 to N) of this X if the user inputted it before.

    The basic functionality of data processing
    (data initialization,data insertion, data search) should be done
    via Object-Oriented Programming Paradigm (i.e. using Classes).
    """
    
    def __init__(self) -> None:
        pass
        
    def main(self):
        print("Type the number of inputs (positive integer):")
        n = self.input_positive_integer()

        print(f"provide {n} numbers one by one:")
        numbers = [self.input_integer() for _ in range(n)]

        print("Type an integer to search, and the index will be given:")
        x = self.input_integer()

        index = self.search_index(numbers, x)
        print(index)

    def search_index(self, numbers, x):
        try:
            return numbers.index(x) + 1 # 1-indexed
        except ValueError:
            return -1

    def input_integer(self) -> int:
        while True:
            input_str = input()
            
            try:
                n = int(input_str)
                return n
            except ValueError: # Cast failed
                print(f"Input must be an integer but was '{input_str}'. Try again.")
                continue

    def input_positive_integer(self) -> int:
        while True:
            n = self.input_integer()

            if n > 0:
                return n
            else:
                print(f"Input integer must be positive but was {n}. Try again.")

if __name__ == "__main__":
    search_list = SearchList()
    search_list.main()
