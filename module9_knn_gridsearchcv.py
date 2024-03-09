from typing import Tuple

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class kNNGridSearch:
    """
    The program asks the user for input N (positive integer) and reads it.

    Then the program asks the user to provide N (x, y) pairs (one by one) and
    reads all of them: first: x value, then: y value for every pair one by one.
    X is treated as the input feature and Y is treated as the class label.
    X is a real number, Y is a non-negative integer.

    This set of pairs constitutes the training set TrainS = {(x, y)_i}, i = 1..N.

    Then the program asks the user for input M (positive integer) and reads it.

    Then the program asks the user to provide M (x, y) pairs (one by one) and
    reads all of them: first: x value, then: y value for every pair one by one.
    X is treated as the input feature and Y is treated as the class label.
    X is a real number, Y is a non-negative integer.

    This set of pairs constitutes the test set TestS = {(x, y)_i}, i = 1..M.

    In the end, the program outputs: the best k for the kNN Classification
    method and the corresponding test accuracy. kNN Classifier should be
    trained on pairs from TrainS, tested on x values from TestS and
    compared with y values from TestS.

    The basic functionality of data processing (data initialization, data insertion),
    should be done using Numpy library while the computation (ML) part
    should be done using Scikit-learn library as much as possible
    (note: you can combine with what you've done from the previous tasks). 

    Note: you can try the following range of k: 1 <= k <= 10.
    """
    
    def __init__(self) -> None:
        pass
        
    def run(self):
        print("Type the number of inputs N (positive integer):")
        n = self.input_positive_integer()

        print(f"Type {n} pairs of data points (x, y) one by one:")
        train = self.input_pair_real_nonnegative(n)

        print("Type the number of inputs M (positive integer):")
        m = self.input_positive_integer()

        print(f"Type {m} pairs of data points (x, y) one by one:")
        test = self.input_pair_real_nonnegative(m)

        best_k, best_accuracy = self.grid_search(train, test)

        print(f"Best k: {best_k}")
        print(f"Best test accuracy: {best_accuracy}")
    
    def grid_search(self, train, test, k_min=1, k_max=10) -> Tuple[float, float]:
        k_max = min(k_max, len(train))
        best_accuracy = 0
        best_k = None

        for k in range(k_min, k_max + 1):
            accuracy = self.fit_and_get_test_accuracy(train=train, test=test, k=k)

            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_k = k
        
        return best_k, best_accuracy

    def fit_and_get_test_accuracy(self, train: np.ndarray, test: np.ndarray, k: int
            ) -> float:
        
        train = train.T  # Shape (N, 2) to (2, N)
        x_train = train[0]
        x_train = x_train[:, None] # Shape (n_samples, n_features = 1)
        y_train = train[1]


        test = test.T  # Shape (N, 2) to (2, N)
        x_test = test[0]
        x_test = x_test[:, None] # Shape (n_samples, n_features = 1)
        y_test = test[1]

        knn_regressor = KNeighborsClassifier(n_neighbors=k)
        knn_regressor.fit(x_train, y_train)

        y_pred = knn_regressor.predict(x_test)

        return accuracy_score(y_test, y_pred)

    def input_pair_real_nonnegative(self, n: int) -> np.ndarray:
        assert isinstance(n, int)
        assert n >= 1

        return np.asarray(  # Shape (N, 2)
            [[float(input()), int(input())]  # (x, y)
            for _ in range(n)]
        )
    
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
    precision_recall = kNNGridSearch()
    precision_recall.run()
