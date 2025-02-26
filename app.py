import streamlit as st

# Page Config
st.set_page_config(page_title="💡Advanced Unit Converter🔁", layout="centered")

# Conversion Factors Dictionary
conversion_factors = {
    "Length": {
        "Millimeter": 0.001, "Centimeter": 0.01, "Meter": 1, "Kilometer": 1000,
        "Inch": 0.0254, "Foot": 0.3048, "Yard": 0.9144, "Mile": 1609.34
    },
    "Weight": {
        "Milligram": 0.000001, "Gram": 0.001, "Kilogram": 1, "Ton": 1000,
        "Ounce": 0.0283495, "Pound": 0.453592
    },
    "Temperature": {
        "Celsius": lambda c: c,
        "Fahrenheit": lambda f: (f - 32) * 5/9,
        "Kelvin": lambda k: k - 273.15
    },
    "Area": {
        "Square Meter": 1, "Square Kilometer": 1000000, "Hectare": 10000,
        "Square Foot": 0.092903, "Square Yard": 0.836127, "Acre": 4046.86
    },
    "Volume": {
        "Milliliter": 0.001, "Liter": 1, "Cubic Meter": 1000,
        "Cubic Inch": 0.0163871, "Cubic Foot": 28.3168, "Gallon": 3.78541
    },
    "Time": {
        "Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400, "Week": 604800
    }
}

# Custom CSS for Button Hover Effect
st.markdown("""
    <style>
        div.stButton > button {
            background-color: #007BFF;  /* Default blue */
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 5px;
            transition: all 0.3s ease-in-out;
        }
        div.stButton > button:hover {
            background-color: #0056b3; /* Darker blue on hover */
            transform: translateY(-3px); /* Moves button up */
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Adds slight shadow */
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<div style='text-align: center; font-size: 60px; font-weight: bold; color: #007BFF;'>Code With Hamza 💻</div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: center; font-size: 30px; font-weight: bold; color: black;'>💡Advanced Unit Converter🔁</div>", unsafe_allow_html=True)

# Converter Selection
category = st.selectbox("Select a Category", list(conversion_factors.keys()))
unit_options = list(conversion_factors[category].keys())
input_value = st.number_input("Enter Value", value=1.0)

col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    input_unit = st.selectbox("From", unit_options)
with col3:
    output_unit = st.selectbox("To", unit_options)

# Convert Button
if st.button("Convert"):
    input_conversion = conversion_factors[category][input_unit]
    output_conversion = conversion_factors[category][output_unit]

    if callable(input_conversion):
        result = output_conversion(input_conversion(input_value))
    else:
        result = (input_value * input_conversion) / output_conversion

    st.markdown(f"<b>{input_value}</b> {input_unit} = <b>{result:.4f}</b> {output_unit}", unsafe_allow_html=True)

# Description Section with Columns
st.markdown("<h3>Available Unit Conversions</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div style='background-color: #eef5ff; border-left: 5px solid #007BFF; padding: 15px; border-radius: 5px; margin: 10px;'>
            <b>Length:</b> Convert between millimeters, centimeters, meters, kilometers, inches, feet, yards, and miles.
        </div>
        <div style='background-color: #eef5ff; border-left: 5px solid #007BFF; padding: 15px; border-radius: 5px; margin: 10px;'>
            <b>Temperature:</b> Convert between Celsius, Fahrenheit, and Kelvin.
        </div>
        <div style='background-color: #eef5ff; border-left: 5px solid #007BFF; padding: 15px; border-radius: 5px; margin: 10px;'>
            <b>Volume:</b> Convert between milliliters, liters, cubic meters, cubic inches, cubic feet, and gallons.
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div style='background-color: #eef5ff; border-left: 5px solid #007BFF; padding: 15px; border-radius: 5px; margin: 10px;'>
            <b>Weight:</b> Convert between milligrams, grams, kilograms, tons, ounces, and pounds.
        </div>
        <div style='background-color: #eef5ff; border-left: 5px solid #007BFF; padding: 15px; border-radius: 5px; margin: 10px;'>
            <b>Area:</b> Convert between square meters, square kilometers, hectares, square feet, square yards, and acres.
        </div>
        <div style='background-color: #eef5ff; border-left: 5px solid #007BFF; padding: 15px; border-radius: 5px; margin: 10px;'>
            <b>Time:</b> Convert between seconds, minutes, hours, days, and weeks.
        </div>
    """, unsafe_allow_html=True)

# Footer Section
st.markdown("""
    <div style='text-align: center; font-size: 20px; color: #666;'>
        📌Created by <span style='color: #007BFF;'>Code With Hamza💻</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style='background-color: #eef5ff; text-align: center; padding: 15px; border-radius: 5px; margin: 10px;'>
        <b>Join Our WhatsApp Community</b><br>
        <a href="https://chat.whatsapp.com/DsgyUPdnNEcLTkvQibJtGk" target="_blank">Community Link</a>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='text-align: center; font-size: 14px; color: #666;'>All rights reserved. © 2025 Hamza Shakoor</div>", unsafe_allow_html=True)
