import os
import sys

# Add the directory containing the myproject package to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../myproject')))

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

# Load the Django apps
import django
django.setup()

# Import your Django models
from myapp.models import Product, Category

import streamlit as st
import pandas as pd

# Add a header to the page
st.header("Product List")

# Load data from your database using your Django models
products = Product.objects.all()
categories = Category.objects.all()

# Convert the data to a Pandas DataFrame
df_products = pd.DataFrame(list(products.values()))
df_categories = pd.DataFrame(list(categories.values()))

# Rename columns for better readability
df_products = df_products.rename(columns={"name": "Product Name", "description": "Description", "price": "Price ($)"})
df_categories = df_categories.rename(columns={"name": "Category Name"})

# Format price as currency
df_products["Price ($)"] = df_products["Price ($)"].map("${:,.2f}".format)

# Style the tables with custom CSS
st.write("""
    <style>
        table.dataframe {
            font-size: 14px;
            border: 1px solid #ccc;
            border-collapse: collapse;
            margin: 10px 0;
            max-width: 100%;
            overflow-x: auto;
            display: block;
        }
        table.dataframe th {
            background-color: #4285F4;
            color: white;
            font-weight: bold;
            padding: 8px;
            text-align: center;
            border: 1px solid #ccc;
        }
        table.dataframe td {
            padding: 8px;
            text-align: center;
            border: 1px solid #ccc;
        }
        table.dataframe tr:nth-child(even) {
            background-color: #F5F5F5;
        }
        table.dataframe tr:hover {
            background-color: #EEE8AA;
        }
    </style>
""", unsafe_allow_html=True)

st.write("<h2>Products</h2>", unsafe_allow_html=True)
st.write(df_products)

st.write("<h2>Categories</h2>", unsafe_allow_html=True)
st.write(df_categories)

# Print the Python path for debugging
import sys
print(sys.path)
