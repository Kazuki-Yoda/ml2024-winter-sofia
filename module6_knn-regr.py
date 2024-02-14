import numpy as np

class kNNRegression:
    """
    The program asks the user for input N (positive integer) and reads it.

    Then the program asks the user for input k (positive integer) and reads it.

    Then the program asks the user to provide N (x, y) points (one by one) and
    reads all of them: first: x value, then: y value for every point one by one.
    X and Y are the real numbers.

    In the end, the program asks the user for input X and outputs:
    the result (Y) of k-NN Regression if k <= N, or any error message otherwise.

    The basic functionality of data processing
    (data initialization,data insertion, data calculation)
    should be done using Numpy library as much as possible
    (note: you can combine with OOP from the previous task).
    """
    
    def __init__(self) -> None:
        pass
        
    def main(self):
        print("Type the number of inputs N (positive integer):")
        n = self.input_positive_integer()

        print("Type the number of nearest neighbors k (positive integer):")
        k = self.input_positive_integer()

        print(f"Type {n} pairs of data points (real numbers) one by one:")
        data = np.asarray(  # Shape (N, 2)
            [[float(input()), float(input())]  # (x, y)
            for _ in range(n)]
        )
        
        print("Type X (a real number):")
        x_fit = float(input())

        if k > n:
            raise ValueError("The number of nearest neighbors k must be smaller"
                             + "than the number of inputs N.")

        y_fit = self.fit(data, x_fit, k)
        print(f"Result of k-NN regression Y: {y_fit}")
    
    def fit(self, data: np.ndarray, x_fit: np.ndarray, k: int) -> float:
        data = data.T  # Shape (N, 2) to (2, N)
        x_data = data[0]
        y_data = data[1]

        distance = np.abs(x_data - x_fit)
        nearest_indices = np.argsort(distance)
        k_nearest_indices = nearest_indices[:k]
        k_nearest_y = y_data[k_nearest_indices]

        y_fit = np.mean(k_nearest_y)

        return y_fit        

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
    search_list = kNNRegression()
    search_list.main()
