import streamlit as st

st.set_page_config(page_title="💡Advanced Unit Converter🔁", layout="centered")

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

st.markdown("""
    <style>
        .header-title {
            text-align: center;
            font-size: 60px;
            font-weight: bold;
            color: #007BFF;
        }
        .sub-header {
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            color: black;
        }
        .description-box {
            background-color: #eef5ff;
            border-left: 5px solid #007BFF;
            padding: 15px;
            border-radius: 5px;
            margin: 10px;
        }
        .footer-text {
            text-align: center;
            font-size: 14px;
            color: #666;
        }
        .footer-created-by {
            text-align: center;
            font-size: 20px;
            color: #666;
        }
        .footer-code-with-hamza {
            color: #007BFF;
        }
        .selectbox-label, .stSelectbox {
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='header-title'>Code With Hamza 💻</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>💡Advanced Unit Converter🔁</div>", unsafe_allow_html=True)

# Converter Selection
category = st.selectbox("Select a Category", list(conversion_factors.keys()))
unit_options = list(conversion_factors[category].keys())
input_value = st.number_input("Enter Value", value=1.0)
col1, col2, col3 = st.columns([2, 1, 2])

with col1:
    input_unit = st.selectbox("From", unit_options)
with col3:
    output_unit = st.selectbox("To", unit_options)

if st.button("Convert"):
    input_conversion = conversion_factors[category][input_unit]
    output_conversion = conversion_factors[category][output_unit]

    if callable(input_conversion):
        result = output_conversion(input_conversion(input_value))
    else:
        result = (input_value * input_conversion) / output_conversion

    st.markdown(f"<b>{input_value}</b> {input_unit} = <b>{result:.4f}</b> {output_unit}", unsafe_allow_html=True)

# Description Section with 2 columns
st.markdown("<h3>Available Unit Conversions</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class='description-box'>
            <b>Length:</b> Convert between millimeters, centimeters, meters, kilometers, inches, feet, yards, and miles.
        </div>
        <div class='description-box'>
            <b>Temperature:</b> Convert between Celsius, Fahrenheit, and Kelvin.
        </div>
        <div class='description-box'>
            <b>Volume:</b> Convert between milliliters, liters, cubic meters, cubic inches, cubic feet, and gallons.
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='description-box'>
            <b>Weight:</b> Convert between milligrams, grams, kilograms, tons, ounces, and pounds.
        </div>
        <div class='description-box'>
            <b>Area:</b> Convert between square meters, square kilometers, hectares, square feet, square yards, and acres.
        </div>
        <div class='description-box'>
            <b>Time:</b> Convert between seconds, minutes, hours, days, and weeks.
        </div>
    """, unsafe_allow_html=True)

# Footer & Community Links
st.markdown("""
    <div class='footer-created-by'>
        📌Created by <span class='footer-code-with-hamza'>Code With Hamza💻</span>
    </div>
""", unsafe_allow_html=True)
st.markdown("""
    <div class='description-box' style='text-align: center;'>
        <b>Join Our WhatsApp Community</b><br>
        <a href="https://chat.whatsapp.com/DsgyUPdnNEcLTkvQibJtGk" target="_blank">Community Link</a>
    </div>
""", unsafe_allow_html=True)
st.markdown("<div class='footer-text'>All rights reserved. © 2025 Hamza Shakoor</div>", unsafe_allow_html=True)
