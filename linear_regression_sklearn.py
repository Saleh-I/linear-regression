import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
df = pd.read_csv('data/lemonade_dataset_c.csv')

X = df['Temperature (°C)'].values.reshape(-1, 1)
y = df['Lemonade (Liters)']

# Create linear regression object
model = LinearRegression()

# Train the model using the training sets
model.fit(X, y)

# The coefficients
print(f'Coefficients: {model.coef_}')
print(f'Intercept: {model.intercept_}')


# Plot the data points
plt.scatter(X, y, color='blue', label='Data points')

# Plot the best fit line
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Best fit line')

# Adding title and labels
plt.title('Temperature vs Lemonade Sales')
plt.xlabel('Temperature (°C)')
plt.ylabel('Lemonade (Liters)')
plt.legend()

# Show the plot
plt.show()
