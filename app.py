import streamlit as st

# Page Config with Wide Layout for Better Responsiveness
st.set_page_config(page_title="📏📏Professional Unit Converter🔁", layout="wide")

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

# Custom CSS for Responsive UI
st.markdown("""
    <style>
        @media screen and (max-width: 768px) {
            div.stButton > button {
                font-size: 14px !important;
                padding: 8px 16px !important;
            }
            div.stSelectbox, div.stNumberInput input {
                font-size: 14px !important;
            }
        }
        div.stButton > button {
            background-color: #007BFF; 
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 10px 20px;
            border-radius: 5px;
            transition: all 0.3s ease-in-out;
        }
        div.stButton > button:hover {
            background-color: #0056b3;
            transform: translateY(-3px);
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("<h1 style='text-align: center; color: #007BFF;'>Code With Hamza 💻</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>📏📏Professional Unit Converter🔁</h2>", unsafe_allow_html=True)

# Converter Selection
category = st.selectbox("Select a Category", list(conversion_factors.keys()))
unit_options = list(conversion_factors[category].keys())
input_value = st.number_input("Enter Value", value=1.0)

# Responsive Layout for Inputs
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

# Available Conversions - Collapsible for Mobile
with st.expander("ℹ️ Available Unit Conversions"):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            - **Length**: Millimeter, Centimeter, Meter, Kilometer, Inch, Foot, Yard, Mile.
            - **Temperature**: Celsius, Fahrenheit, Kelvin.
            - **Volume**: Milliliter, Liter, Cubic Meter, Cubic Inch, Cubic Foot, Gallon.
        """)
    with col2:
        st.markdown("""
            - **Weight**: Milligram, Gram, Kilogram, Ton, Ounce, Pound.
            - **Area**: Square Meter, Square Kilometer, Hectare, Square Foot, Square Yard, Acre.
            - **Time**: Second, Minute, Hour, Day, Week.
        """)

# Footer Section
st.markdown("""
    <div style='text-align: center; font-size: 20px; color: #666;'>
        📌Created by <span style='color: #007BFF;'>Code With Hamza💻</span>
    </div>
    <div style='background-color: #eef5ff; text-align: center; padding: 15px; border-radius: 5px; margin: 10px;'>
        <b>Join Our WhatsApp Community</b><br>
        <a href="https://chat.whatsapp.com/DsgyUPdnNEcLTkvQibJtGk" target="_blank">Community Link</a>
    </div>
    <div style='text-align: center; font-size: 14px; color: #666;'>All rights reserved. © 2025 Hamza Shakoor</div>
""", unsafe_allow_html=True)
