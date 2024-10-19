# Software_Development_Tools
Software Development Tools Project
Project description
This project is an interactive web application built with Streamlit, designed for analyzing a car advertisement dataset. It provides users with a platform to explore various attributes of cars, including condition, model year, price, and mileage. There are histograms and scatter plots that would help users to visualize better on how certain attributes relate to each other. For example how the mileage of a car and car conditions.

# Features of Application
A histogram of car conditions in order to visualize the distribution of car conditions across different model years.
Scatter Plot of Price in relation to the Mileage. The scatter plot will examine how the price of a car is influenced by its mileage.
An interactive checkbox feature that will allow users to toggle the distribution of different ages of cars in the scatter plot.

# Libraries Used
Pandas: For data manipulation and analysis.
Streamlit: Building the interactive web application.
Plotly Express: Creating interactive visualizations.
Altair: Optionally used for additional visualizations.

# Repository Files

app.py: This is the main application file for the Streamlit app.

vehicles_us.csv: The dataset file (to be downloaded separately).

EDA.ipynb: Jupyter notebook for exploratory data analysis.

requirements.txt: Lists the dependencies required by the project.

.streamlit/config.toml: Configuration file for Streamlit deployment.

.gitignore: Specifies files and directories to be ignored by git.

README.md: Explanation of project

# Building Application
Run through Streamlit application:

streamlit run app.py
Open the provided URL (usually http://localhost:10000) in your web browser.

Access the Application
Can access the application with the following link https://car-advertisement-lists.onrender.com
