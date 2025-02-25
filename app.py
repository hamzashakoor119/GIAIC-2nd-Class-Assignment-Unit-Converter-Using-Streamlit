import streamlit as st

# Configure the Streamlit page settings
st.set_page_config(page_title="Unit Converter", page_icon="🔢", layout="wide")

# Apply custom CSS for an enhanced UI experience
st.markdown("""
    <style>
        /* Main Title Styling */
        .title {
            text-align: center;
            color: #0056b3;
            font-size: 42px;
            font-weight: bold;
            margin-bottom: -10px;
        }
        /* Subtitle Styling */
        .subtitle {
            text-align: center;
            font-size: 20px;
            color: #6c757d;
            font-weight: 500;
        }
        /* Button Styling */
        .stButton>button {
            background-color: #007BFF;
            color: white;
            border-radius: 8px;
            width: 100%;
            padding: 12px;
            font-size: 18px;
            font-weight: bold;
        }
        /* Sidebar Title Styling */
        .sidebar-title {
            font-size: 22px;
            font-weight: bold;
            color: #0056b3;
        }
        /* Dropdown Cursor Effect */
        div[data-baseweb="select"] > div {
            cursor: pointer !important;
        }
        /* Footer Styling */
        .footer {
            text-align: center;
            color: grey;
            font-size: 14px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Page header
st.markdown("<h1 class='title'>Code With Hamza 💻</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>A Professional Unit Converter</h2>", unsafe_allow_html=True)
st.write("")

# Sidebar settings
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Streamlit-logo-primary-colormark-darktext.png", width=200)
st.sidebar.markdown("<p class='sidebar-title'>⚙️ Settings</p>", unsafe_allow_html=True)
st.sidebar.write("Adjust settings and select units.")
st.sidebar.markdown("---")  # Adds a separator line for better UI

# Dictionary containing conversion factors for different unit categories
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

# User selects the unit category they want to convert
category = st.selectbox("📌 Select a Category", list(conversion_factors.keys()))

# Get the list of units available for the selected category
unit_options = list(conversion_factors[category].keys())

# User selects input and output units
input_unit = st.selectbox("🛠 Select Input Unit", unit_options)
output_unit = st.selectbox("🎯 Select Output Unit", unit_options)

# User inputs the numerical value they want to convert
value = st.number_input("🔢 Enter Value", value=0.0, step=0.1)

# Perform conversion when the user clicks the "Convert" button
if st.button("🚀 Convert"):
    input_conversion = conversion_factors[category][input_unit]
    output_conversion = conversion_factors[category][output_unit]

    # Special handling for temperature conversion (using functions)
    if callable(input_conversion):
        result = output_conversion(input_conversion(value))
    else:
        result = (value * input_conversion) / output_conversion

    # Display the conversion result
    st.success(f"✅ {value} {input_unit} = {result:.4f} {output_unit}")

# Footer
st.markdown("---")
st.markdown("<p class='footer'>📌 Created By <b style='color:#0056b3;'>Code With Hamza 💻</b> using Streamlit</p>", unsafe_allow_html=True)
