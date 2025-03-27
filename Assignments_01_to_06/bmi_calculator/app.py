import streamlit as st

st.title("BMI CALCULATOR")
st.subheader("Calculate your body mass index!")

mass=st.number_input("Enter your mass in kg",min_value=1)
height_cm=st.number_input("Enter your height in cm",min_value=1)

height_metres=(height_cm/100)**2

BMI= round((mass/height_metres),2)

if st.button("Calculate BMI:"):
 if BMI < 18.5:
    st.error(F"Your BMI  is {BMI} underweight")
 elif BMI > 18.5 and BMI < 24.9:
    st.warning(F"Your BMI  is {BMI} normal")
 else:
    st.success(F"Your BMI  is {BMI} healthy")






