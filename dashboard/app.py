import faicons as fa
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import asyncio  
from shiny import render, req
from shiny.express import input, ui

# Load fitness data
fitness_data = px.data.gapminder()

# Add page title and sidebar
ui.page_opts(title="Fitness Tracker", fillable=True)

# Sidebar
with ui.sidebar(open="desktop", style="background-color: lightblue"):
    ui.input_slider("n", "Number of Bins", 1, 100, 20)

    # Date input
    ui.input_date("date", "Date")

    # Text area input
    ui.input_text_area("textarea", "Text input", "Hello World")

    # Integrated UI elements
    ui.h6("Links:", style="color: #fff;")
    ui.a("GitHub Source", href="https://github.com/don4ye/cintel-06-custom", target="_blank", style="color: #fff; text-decoration: none; display: block; margin-bottom: 10px;")
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank", style="color: #fff; text-decoration: none; display: block; margin-bottom: 10px;")

# Main content with layout_columns
with ui.layout_columns(col_widths=[12, 6, 6]):
    with ui.card(height="400px"):
        # Define function to render histogram
        @render.plot(alt="Histogram of life expectancy.")
        def plot():
            ax = sns.histplot(data=fitness_data, x="lifeExp", bins=input.n())  
            ax.set_title("Fitness Data")
            ax.set_xlabel("Life Expectancy")
            ax.set_ylabel("Count")
            return ax

# Main content
ui.input_action_button("do_compute", "Analyze Fitness Data")

# Text area input value
@render.text
def value():
    return input.textarea()

# Machine Learning Integration
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Select features and target variable
X = fitness_data[['year', 'gdpPercap']]  # Example features
y = fitness_data['lifeExp']  # Target variable

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
print("Sample Predictions:")
for i in range(5):
    print(f"Actual: {y_test.iloc[i]:.2f}, Predicted: {y_pred[i]:.2f}")
