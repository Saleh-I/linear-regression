import matplotlib.pyplot as plt

# X and y.
X = [1, 2, 3, 4, 5, 5]
y = [2, 3, 1, 2, 3, 5]


# Initialize parameters.
w = 0
b = 0

iterations = 30
alpha = 0.01

# Number of training examples
m = len(X)

for j in range(iterations):

    fx_column = []
    fx_y_column = []
    fx_y_x_column = []
    for i in range(m):
        fx = w * X[i] + b
        fx_y = fx - y[i]
        fx_y_x = fx_y * X[i]

        fx_column.append(fx)
        fx_y_column.append(fx_y)
        fx_y_x_column.append(fx_y_x)


    dj_dw = (1 / m) * sum(fx_y_x_column)
    dj_db = (1 / m) * sum(fx_y_column)

    w = w - alpha * dj_dw
    b = b - alpha * dj_db

print('w = ', w)
print('b = ', b)


# Calculate the y-values of the line for the range of x-values
line_xs = range(min(X), max(X) + 1)
line_ys = [w * x + b for x in line_xs]

# Plot the points
plt.scatter(X, y, color='blue', label='Data Points')

# Plot the line
plt.plot(line_xs, line_ys, color='red', label=f'Line: y = {w:.2f}x + {b:.2f}')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Points and Fitted Line')
plt.legend()

# Show the plot
plt.show()

