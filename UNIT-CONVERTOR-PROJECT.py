# PROJECT 01: UNIT CONVERTOR
# A GOOGLE UNIT CONVERTOR WITH USING PYTHON AND STREAMLIT

import streamlit as st 
st.markdown(
    """
    <style>
    body{
        background-color: grey;
        color: white;
    }
    .stApp{
        background: linear-gradient(135deg,rgb(213, 169, 250),rgb(198, 214, 238));
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1{
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton>button{
        background: linear-gradient(45deg, blue, purple);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15ps rgba(133, 39, 211, 0);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg,rgb(78, 247, 247),rgb(19, 99, 190));
        color: black;
    }
    .result-box{
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background:rgba(245, 242, 242, 0.11);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(215, 67, 252, 0.96);
    }
    .footer{
        text-align: center;
        margin-top: 50px;
        font-size: 18px;
        color: black;
        background:rgba(245, 242, 242, 0.11);
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(215, 67, 252, 0.96);
    }
    </style>
    """,
    unsafe_allow_html = True
)

# TITLE AND DESCRIPTION
st.markdown("<h1>🚀Unit Convertor using Python and Streamlit</h1>", unsafe_allow_html = True)
st.write("Easily convert between different units of length, weight and Temperature.")

# SIDEBAR MENU
conversion_type = st.sidebar.selectbox("Choose Conversion Type",["Length", "Weight", "Temperature"])
value = st.number_input("Enter Value", value= 0.0, min_value= 0.0, step=0.1)
col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters","Milimeters", "Miles","Yards", "Inches", "Feets"])
    with col2:
        to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters","Milimeters", "Miles","Yards", "Inches", "Feets"] ) 
elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["Kilogram", "Grams", "Miligrams", "Pounds", "Ounces"])
    with col2:
        to_unit = st.selectbox("To", ["Kilogram", "Grams", "Miligrams", "Pounds", "Ounces"])
elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["Celsius" , "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["Celsius" , "Fahrenheit", "Kelvin"])

# CONVERTED FUNCTION
def length_convertor(value, from_unit, to_unit):
    length_units ={
        'Meters': 1, 'Kilometers':0.001, 'Centimeters': 100, 'Milimeters': 1000,
        'Miles': 0.000621371, 'Yards': 1.09361, 'Feets':3.28084, 'Inches':39.3701
    }
    return (value / length_units[from_unit])*length_units[to_unit]

def weight_convertor(value, from_unit, to_unit):
    weight_units ={
        'Kilogram': 1, 'Grams': 1000, 'Miligrams' : 1000000, 'Pounds': 2.20462, 'Ounces': 35.274
    }
    return (value / weight_units[from_unit])*weight_units[to_unit]

def temp_convertor(value, from_unit, to_unit):
    if from_unit =="Celsius" :
        return(value*9/5+32) if to_unit == "Fahrenheit" else value + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else(value - 32)* 5/9 + 273.15 if to_unit == "Kelvin" else value
    elif from_unit == "Kelvin" :
        return value - 274.15 if to_unit == "Celsius" else (value-273.15) * 9/5+32 if to_unit == "Fahrenheit" else value
    return value 

# BUTTON FOR CONVERSION
if st.button("Convert🤖"):
    if conversion_type == "Length":
        result = length_convertor(value, from_unit, to_unit)
    elif conversion_type == "Weight":
         result = weight_convertor(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
         result = temp_convertor(value, from_unit, to_unit)
    
    st.markdown(f"<div class='result-box'>{value} {from_unit} = {result:.4f} {to_unit}</div>", unsafe_allow_html = True)

# FOOTER
st.markdown("<div class = 'footer'>Created By Khazra Ayub 💖</div>" , unsafe_allow_html = True)


        






