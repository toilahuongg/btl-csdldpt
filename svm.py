import numpy as np


class SVM:
    def __init__(self, learning_rate=0.001, lambda_param=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.lambda_param = lambda_param
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        n_samples, n_features = X.shape

        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.num_iterations):
            scores = np.dot(X, self.weights) + self.bias
            predictions = self._predict(scores)

            dw = (1 / n_samples) * (np.dot(X.T, (predictions - y)) + self.lambda_param * self.weights)
            db = (1 / n_samples) * np.sum(predictions - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def _predict(self, scores):
        return np.where(scores >= 0, 1, -1)

    def predict(self, X):
        scores = np.dot(X, self.weights) + self.bias
        return self._predict(scores)

