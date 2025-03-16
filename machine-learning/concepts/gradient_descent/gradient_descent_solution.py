class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init

        for _ in range(iterations):
            df_dx = 2 * x  # Derivative of f(x) = x^2
            x = x - learning_rate * df_dx  # Gradient descent step
        
        return round(x, 5)  # Round to 5 

sol = Solution()
print(sol.get_minimizer(0, 0.01, 5))  # Output: 5
print(sol.get_minimizer(10, 0.01, 5))  # Output: 4.08536
