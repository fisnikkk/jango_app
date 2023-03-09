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
from myapp.models import Product

import streamlit as st
import pandas as pd

# Set page title and favicon
st.set_page_config(page_title="My Product List", page_icon=":clipboard:")

# Add a header to the page
st.header("Product List")

# Load data from your database using your Django models
products = Product.objects.all()

# Convert the data to a Pandas DataFrame
df = pd.DataFrame(list(products.values()))

# Rename columns for better readability
df = df.rename(columns={"name": "Product Name", "price": "Price ($)"})

# Format price as currency
df["Price ($)"] = df["Price ($)"].map("${:,.2f}".format)

# Style the table with custom CSS
st.write("<style>div.row-widget.stRadio > div{flex-direction:row;}</style>", unsafe_allow_html=True)
st.dataframe(df.style.set_properties(**{'text-align': 'center'}).set_table_styles([{'selector': 'th', 'props': [('background', '#4285F4'), ('color', 'white'), ('font-weight', 'bold'), ('padding', '10px')]}, {'selector': 'td', 'props': [('padding', '10px')]}, {'selector': '.row-index', 'props': [('font-weight', 'bold'), ('background', '#F5F5F5')]}, {'selector': ':hover', 'props': [('background-color', '#EEE8AA')]}]).set_precision(2))

# Print the Python path for debugging
import sys
print(sys.path)
