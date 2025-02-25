# import streamlit as st

# # Apply custom styling
# st.set_page_config(page_title="Unit Converter", page_icon="🔢", layout="centered")

# # CSS for professional UI/UX
# st.markdown("""
#     <style>
#         /* Main Title */
#         .title {
#             text-align: center;
#             color: #007BFF;
#             font-size: 40px;
#             font-weight: bold;
#         }
#         /* Subtitle */
#         .subtitle {
#             text-align: center;
#             font-size: 18px;
#             color: #6c757d;
#         }
#         /* Input Boxes */
#         .stTextInput, .stSelectbox, .stNumberInput {
#             border-radius: 10px;
#             padding: 5px;
#         }
#         /* Button Styling */
#         .stButton>button {
#             background-color: #007BFF;
#             color: white;
#             border-radius: 8px;
#             width: 100%;
#             padding: 10px;
#             font-size: 16px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown("<h1 class='title'>Code With Hamza 💻</h1>", unsafe_allow_html=True)
# st.markdown("<h2 class='subtitle'>A Professional Unit Converter</h2>", unsafe_allow_html=True)
# st.write("")

# # Dictionary for unit conversion
# conversion_factors = {
#     "Length": {
#         "Millimeter": 0.001, "Centimeter": 0.01, "Meter": 1, "Kilometer": 1000,
#         "Inch": 0.0254, "Foot": 0.3048, "Yard": 0.9144, "Mile": 1609.34
#     },
#     "Weight": {
#         "Milligram": 0.000001, "Gram": 0.001, "Kilogram": 1, "Ton": 1000,
#         "Ounce": 0.0283495, "Pound": 0.453592
#     },
#     "Temperature": {
#         "Celsius": lambda c: c, "Fahrenheit": lambda f: (f - 32) * 5/9, "Kelvin": lambda k: k - 273.15
#     },
#     "Area": {
#         "Square Meter": 1, "Square Kilometer": 1000000, "Hectare": 10000,
#         "Square Foot": 0.092903, "Square Yard": 0.836127, "Acre": 4046.86
#     },
#     "Volume": {
#         "Milliliter": 0.001, "Liter": 1, "Cubic Meter": 1000,
#         "Cubic Inch": 0.0163871, "Cubic Foot": 28.3168, "Gallon": 3.78541
#     },
#     "Time": {
#         "Second": 1, "Minute": 60, "Hour": 3600, "Day": 86400, "Week": 604800
#     }
# }

# # Sidebar Navigation
# st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Streamlit-logo-primary-colormark-darktext.png", width=200)
# st.sidebar.title("⚙️ Settings")
# st.sidebar.write("Adjust settings and select units.")

# # Select category
# category = st.selectbox("📌 Select a Category", list(conversion_factors.keys()))

# # Select input & output unit
# unit_options = list(conversion_factors[category].keys())
# input_unit = st.selectbox("🛠 Select Input Unit", unit_options)
# output_unit = st.selectbox("🎯 Select Output Unit", unit_options)

# # Input value
# value = st.number_input("🔢 Enter Value", value=0.0, step=0.1)

# # Convert button
# if st.button("🚀 Convert"):
#     # Get conversion factor or function
#     input_conversion = conversion_factors[category][input_unit]
#     output_conversion = conversion_factors[category][output_unit]

#     if callable(input_conversion):  # Temperature conversion
#         result = output_conversion(input_conversion(value))
#     else:
#         result = (value * input_conversion) / output_conversion

#     st.success(f"✅ {value} {input_unit} = {result:.4f} {output_unit}")

# # Footer
# st.markdown("---")
# st.markdown("<p style='text-align:center; color:grey;'>📌 Created By Code With Hamza 💻 using Streamlit</p>", unsafe_allow_html=True)




import streamlit as st

# Set up the page
st.set_page_config(page_title="Unit Converter", page_icon="🔢", layout="wide")

# CSS for professional UI/UX
st.markdown("""
    <style>
        /* Main Title */
        .title {
            text-align: center;
            color: #0056b3; /* Brighter Blue */
            font-size: 42px;
            font-weight: bold;
            margin-bottom: -10px;
        }
        /* Subtitle */
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
        /* Sidebar */
        .sidebar-title {
            font-size: 22px;
            font-weight: bold;
            color: #0056b3;
        }
        .footer {
            text-align: center;
            color: grey;
            font-size: 14px;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='title'>Code With Hamza 💻</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='subtitle'>A Professional Unit Converter</h2>", unsafe_allow_html=True)
st.write("")

# Sidebar Navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/1/17/Streamlit-logo-primary-colormark-darktext.png", width=200)
st.sidebar.markdown("<p class='sidebar-title'>⚙️ Settings</p>", unsafe_allow_html=True)
st.sidebar.write("Adjust settings and select units.")
st.sidebar.markdown("---")  # Add a separator line for better UI

# Dictionary for unit conversion
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
        "Celsius": lambda c: c, "Fahrenheit": lambda f: (f - 32) * 5/9, "Kelvin": lambda k: k - 273.15
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

# Select category
category = st.selectbox("📌 Select a Category", list(conversion_factors.keys()))

# Select input & output unit
unit_options = list(conversion_factors[category].keys())
input_unit = st.selectbox("🛠 Select Input Unit", unit_options)
output_unit = st.selectbox("🎯 Select Output Unit", unit_options)

# Input value
value = st.number_input("🔢 Enter Value", value=0.0, step=0.1)

# Convert button
if st.button("🚀 Convert"):
    # Get conversion factor or function
    input_conversion = conversion_factors[category][input_unit]
    output_conversion = conversion_factors[category][output_unit]

    if callable(input_conversion):  # Temperature conversion
        result = output_conversion(input_conversion(value))
    else:
        result = (value * input_conversion) / output_conversion

    st.success(f"✅ {value} {input_unit} = {result:.4f} {output_unit}")

# Footer
st.markdown("---")
st.markdown("<p class='footer'>📌 Created By <b style='color:#0056b3;'>Code With Hamza 💻</b> using Streamlit</p>", unsafe_allow_html=True)
