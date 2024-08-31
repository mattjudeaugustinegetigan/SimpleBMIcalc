import streamlit as st
from bmiCalc import calculate_bmi, determine_bmi_level, calculate_dial_rotation, create_gauge_svg

st.markdown("<h1 style='text-align: center;'> 🤜🏼CSIT342 BMI CALCULATOR🤛🏼</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>by Matt Jude Augustine Uy Getigan BSIT-4</p>", unsafe_allow_html=True)

# Input fields
weight_input = st.number_input('Enter weight (kg)', 1.0, 300.0, 70.0, 0.5)
feet_input = st.number_input('Enter height (feet)', 1, 8, 5)
inches_input = st.number_input('Enter height (inches)', 0, 11, 7)

# Convert height to meters
height_meters = (feet_input * 0.3048) + (inches_input * 0.0254)

# Calculate BMI and related data
BMI = calculate_bmi(weight_input, height_meters)
level = determine_bmi_level(BMI)
dial_rotation = calculate_dial_rotation(BMI)

# Generate the SVG gauge
gauge_svg = create_gauge_svg(BMI, dial_rotation)

# Display the gauge and BMI level
st.markdown(f"<div style='text-align: center;'>{gauge_svg}</div>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align: center;'>BMI level is {level} ({BMI})</h3>", unsafe_allow_html=True)

# Display BMI reference ranges
st.markdown("### BMI Reference Ranges")
st.markdown("""
- **Severe Underweight:** BMI < 13
- **Underweight:** BMI 13 - 18.5
- **Normal:** BMI 18.5 - 25
- **Overweight:** BMI 25 - 30
- **Obesity:** BMI 30 - 43
- **Severe Obesity:** BMI > 43
""")
