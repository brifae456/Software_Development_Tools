import pandas as pd
import streamlit as st
import plotly.express as px

# Read the cleaned up data file
df= pd.read_csv

# cleaning up 'model_year' column
# filling in the missing values in 'model_year' with a median
median_model_year = df.groupby('model')['model_year'].median()

def fill_missing_model_year(row):
    if pd.isnull(row['model_year']):
        return median_model_year[row['model']]
    else:
        return row['model_year']

df['model_year'] = df.apply(fill_missing_model_year, axis=1)

# Make sure the model years are in int values
car_data['model_year'] = car_data['model_year'].astype(int)

# cleaning up 'cylinders' column
# filling in the missing values in 'cylinders' with a median for a group based on 'model'
df['cylinders'] = df['cylinders'].fillna(df.groupby(['model'])['cylinders'].transform('median'))
df['cylinders'] = df['cylinders'].astype(int)

# cleaning up 'odometer' column
# filling in the missing values in 'odometer' with a median for a group based on 'model'
df['odometer'] = df['odometer'].fillna(df.groupby(['model'])['odometer'].transform('median'))

# cleaning up 'paint_color' column
df['paint_color'].fillna('unknown', inplace=True)

# cleaning up 'is_4wd' column
df['is_4wd'].fillna('no', inplace=True)
df['is_4wd'].replace(1.0, 'yes', inplace=True)

st.header("Data Viewer")
st.write("""
###### Check out car listings here!
""")

# Display car listings
st.dataframe(df, height=300)

st.header("Condition vs Model Year")
st.write("""
###### Check the distribution of car conditions across model years.
""")

# Filter out model years equal to 0
filtered_df = df[df['model_year'] != '0']

# Group by manufacturer and vehicle type, and count the number of vehicles
grouped_df = filtered_df.groupby(['model_year', 'condition']).size().reset_index(name='count')

# Create bar chart
fig1 = px.histogram(grouped_df, x="model_year", y="count", color="condition")

st.plotly_chart(fig1)

# defining age category of car
df['age']= 2024 - (pd.to_numeric(filtered_df['model_year'], errors='coerce'))
def age_category(x):
    if x < 10: return '<10 yrs old'
    elif 10 <= x < 20: return '10-20 yrs old'
    else: return '20+ yrs old'

df['age_category'] = df['age'].apply(age_category)

st.header('Price vs Mileage')
st.write("""
###### Check how price is affected by a car's mileage.
""")

# Checkbox to enable/disable visual distinction between ages
show_age_category = st.checkbox("Show Age Categories")

# Distribution of price depending on odometer_value, engine_capacity, number_of_photos
if show_age_category:
    fig2 = px.scatter(df, x="price", y="odometer", color="age_category")
else:
    fig2 = px.scatter(df, x="price", y="odometer")

st.plotly_chart(fig2)