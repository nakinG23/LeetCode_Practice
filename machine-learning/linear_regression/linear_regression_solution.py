import numpy as np
from numpy.typing import NDArray


# Helpful functions:
# https://numpy.org/doc/stable/reference/generated/numpy.matmul.html
# https://numpy.org/doc/stable/reference/generated/numpy.mean.html
# https://numpy.org/doc/stable/reference/generated/numpy.square.html

class Solution:
    
    def get_model_prediction(self, X: NDArray[np.float64], weights: NDArray[np.float64]) -> NDArray[np.float64]:
        # X is an Nx3 NumPy array
        # weights is a 3x1 NumPy array
        # HINT: np.matmul() will be useful
        # return np.round(your_answer, 5)
        prediction = np.dot(X, weights)
        return round(prediction[0], 5)


    def get_error(self, model_prediction: NDArray[np.float64], ground_truth: NDArray[np.float64]) -> float:
        # Compute Mean Squared Error (MSE)
        mse = np.mean(np.square(ground_truth - model_prediction))
        return round(np.sqrt(mse), 5)

sol = Solution()
X=[[0.3745401188473625, 0.9507143064099162, 0.7319939418114051]]
ground_truth=[[0.59865848],[0.15601864],[0.15599452]]
weights=[1.0, 2.0, 3.0]
model_prediction = sol.get_model_prediction( X, weights)
print("model prediction = ", model_prediction)
error = sol.get_error(model_prediction, ground_truth)
print("error = ", error)