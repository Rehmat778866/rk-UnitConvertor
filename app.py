#  Project Unit convertor :
# Build a Google Unit Convertor Using Python and Streamlit:


import streamlit as st
from pint import UnitRegistry

# Initialize unit registry
ureg = UnitRegistry()

# Streamlit UI Enhancements
st.set_page_config(page_title="Unit Converter", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        color:orange;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
        color:Black;
        text-align: center;
    }
    .subheader {
        font-size: 24px;
        font-weight: bold;
        color:black;
        text-align: center;
    }
    .stButton>button {
        background-color: pink;
        color: black;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = st.sidebar.radio("Go to:", ["Home", "Unit Converter", "About", "Contact"])

if menu == "Home":
    st.markdown("<div class='title'>Unit Converter - Easy to Use!!</div>", unsafe_allow_html=True)
    st.markdown("<div class='subheader'>Convert Any unit</div>", unsafe_allow_html=True)
    st.write("Unit Converter allows you to seamlessly convert units for various categories including length, weight, time, volume, and area.")
    st.image("UnitConvertor.jpg", use_container_width=True)

elif menu == "Unit Converter":
    st.markdown("<div class='title'>Unit Converter</div>", unsafe_allow_html=True)
    
    categories = ["Length", "Weight", "Time", "Volume", "Area"]
    category = st.selectbox("Choose conversion type:", categories)

    def convert_units(value, from_unit, to_unit):
        try:
            return (value * ureg(from_unit)).to(to_unit).magnitude
        except Exception as e:
            return f"Error: {e}"

    units_dict = {
        "Length": ["meter", "kilometer", "mile", "foot", "inch", "centimeter", "yard"],
        "Weight": ["gram", "kilogram", "pound", "ounce", "ton"],
        "Time": ["second", "minute", "hour", "day"],
        "Volume": ["liter", "milliliter", "gallon"],
        "Area": ["square_meter", "square_foot", "acre"]
    }
    
    col1, col2 = st.columns(2)
    from_unit = col1.selectbox("From:", units_dict[category])
    to_unit = col2.selectbox("To:", units_dict[category])
    
    value = st.number_input("Enter value:", min_value=0.0, format="%f")
    
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result} {to_unit}")

elif menu == "About":
    st.markdown("<div class='title'>About Unit Converter</div>", unsafe_allow_html=True)
    st.write("Unit Converter is a comprehensive unit conversion tool designed to assist professionals, students, and general users in their daily calculations.")
    
    st.subheader("Why We Created This App")
    st.write("- *Efficiency*: Eliminates the hassle of manual unit conversion.")
    st.write("- *Accuracy*: Ensures precise calculations using reliable conversion data.")
    st.write("- *Convenience*: A single platform for all unit conversions.")
    
    st.subheader("How It Works")
    st.write("- Select the type of conversion.")
    st.write("- Input the value and choose the units.")
    st.write("- Click 'Convert' and get instant results!")

elif menu == "Contact":
    st.markdown("<div class='title'>Contact Information</div>", unsafe_allow_html=True)
    st.write("*Name:*  Rehmat Khalid")
    st.write("*Education:*  Graduation")
    st.write("*City:*  Karachi pakistan")
    st.write("*Slot:*  Giaic Q3 Wednesday (7 - 10 pm)")
    st.write("*Email:* rehmatkhalid11@gmail.com ")
    st.write("*LinkedIn:* [Rehmat Khalid LinkedIn](https://www.linkedin.com/in/rehmatkhalid?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
    st.write("*GitHub:* [Rehmat Khalid GitHub](https://github.com/Rehmat778866?tab=repositories)")

# Footer
st.markdown("---")
st.caption("Copyright © 2025 Unit Converter | Built by Rehmat khalid - Q3 GIAIC Student")
