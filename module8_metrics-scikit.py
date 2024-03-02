import numpy as np
from sklearn.metrics import precision_score, recall_score

class PrecisionRecall:
    """
    The program asks the user for input N (positive integer) and reads it.

    Then the program asks the user to provide N (x, y) points (one by one) and
    reads all of them: first: x value, then: y value for every point one by one.
    X is treated as the ground truth (correct) class label and Y is treated
    as the predicted class. Both X and Y are either 0 or 1.
    
    In the end, the program outputs: the Precision and Recall based on the inputs.
    
    The basic functionality of data processing (data initialization, data insertion),
    should be done using Numpy library while the computation (ML) part should
    be done using Scikit-learn library as much as possible
    (note: you can combine with what you've done from the previous tasks).
    """
    
    def __init__(self) -> None:
        pass
        
    def run(self):
        print("Type the number of inputs N (positive integer):")
        n = self.input_positive_integer()

        print(f"Type {n} pairs of data points (0 or 1) one by one:")
        data = np.asarray(  # Shape (N, 2)
            [[int(input()), int(input())]  # (x, y)
            for _ in range(n)]
        )
        x, y = data[:, 0], data[:, 1]

        precision = precision_score(x, y)
        recall = recall_score(x, y)

        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
    
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
    precision_recall = PrecisionRecall()
    precision_recall.run()
