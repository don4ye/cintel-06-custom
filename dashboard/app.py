import faicons as fa
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import asyncio  # Add asyncio import
from shiny import render, req
from shiny.express import input, ui

# Load fitness data
fitness_data = px.data.gapminder()

# Add page title and sidebar
ui.page_opts(title="Fitness Tracker", fillable=True)

# Sidebar
with ui.sidebar(open="desktop", style="background-color: lightblue"):
    ui.input_slider("n", "Number of Bins", 1, 100, 20)

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
            ax = sns.histplot(data=fitness_data, x="lifeExp", bins=input.n())  # Assuming "lifeExp" is the column of interest
            ax.set_title("Fitness Data")
            ax.set_xlabel("Life Expectancy")
            ax.set_ylabel("Count")
            return ax

# Main content
ui.input_action_button("do_compute", "Analyze Fitness Data")
