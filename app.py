import pandas as pd
import streamlit as st
import plotly.express as px

# Read the cleaned up data file
df= pd.read_csv

# Create one st. header with text
st.title("Vehicles App with Pandas and Plotly")

# Create at least one Plotly Express histogram using st.write or st.plotly_chart
# histogram = px.histogram(vehicles, x='price', title='Vehicle Price Distribution')
# st.write("##Vehicle Price Distribution")
# st.plotly_chart(histogram)

# Create at least one checkbox using st.checkbox that changes the behavior of any of the above components
show_odometer = st.checkbox('Show Odometer Distribution')

if show_odometer:
    histogram = px.histogram(df, x='odometer', title='Vehicle Odometer Distribution')
    st.write("## Vehicle Odometer Distribution")
else: 
    histogram = px.histogram(df, x='price', title='Vehicle Price Distribution')
    st.write("## Vehicle Price Distribution")
   
st.plotly_chart(histogram)

if show_odometer:
    st.write("The histogram is designed to visualize the distribution of vehicle odometer readings(mileage) in the dataset. This provides insights into how mileage varies across listed vehicles, helping users understand patterns like typical mileage range or whether a vehicle has high or low mileage.")
else: 
    st.write("The Vehicle Price histogram provides insights into how vehicles prices are spread, helping users understand key trends such as, most common price ranges for vehicles, whether their selection contains more expensive or affordable vehicles as it pertains to their own budget, or determining the pricing strategy of vehicles based on market trends. Understanding which price points are most common helps identify where the demand or supply of vehicles lies. Users looking to sell vehicles can use this data to competitively price their vehicles. Buyers can use the data to quickly spot potential bargains.")

scatter_plot = px.scatter(df, x='odometer', y='price', title='Price vs Odometer', labels={'odometer': 'Odometer (Mileage)', 'price': 'Price (USD)'}, color='condition') # hover_data=['model', 'year']
st.write("## Scatter Plot: Price vs Odometer")
st.plotly_chart(scatter_plot)

st.write(" The scatter plot shows the relationship between price and odometer. Points are colored by vehicle condition to provide more context on the condition of each vehicle. Additional information, such as model and year can be displayed by hovering over points")