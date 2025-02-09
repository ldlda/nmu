"""give me a 3x3 matrix and a 3 dim vector

i give you the roots back using either gauss-seidel or jacobi"""

import numpy as np


def stupid(A: np.typing.NDArray, b: np.typing.NDArray) -> np.typing.NDArray:
    "they say that in the slides the second method because operator\\ doesnt exist in python"
    return np.linalg.matmul(np.linalg.inv(A), b)  # unbelievable
    # how tf did matlab implement operator\


def real(A: np.typing.NDArray, b: np.typing.NDArray) -> np.typing.NDArray:
    return np.linalg.solve(A, b)  # this uses the lu


# im actually forgetting yall linear algebra is ass
