import streamlit as st
import math

st.set_page_config(page_title="Calculator", layout ="centered")
st.title("Calculator with BMI and GST")

option = st.sidebar.selectbox(
    "Choose Calculator",
    ("Calculator", "BMI Calculator", "GST Calculator")
)

# =============================== SCIENTIFIC CALCULATOR =============================== #

if option == "Calculator":
    st.header("Scientific Calculator")
    
    num1 = st.number_input('Enter first number:', value=0.0)
    num2 = st.number_input('Enter second number:', value=0.0)
    operation = st.selectbox('Select operation:', ['Add', 'Subtract', 'Multiply', 'Divide',
                                                'Square', 'Power (a^b)', 'Cube', 'Square Root',
                                                'Cube Root', 'Log10', 'Log2', 'Exponential',
                                                'Sine', 'Cosine', 'Tangent', 'Factorial'])
    
    if st.button('Calculate'):
        try:
            if operation == "Add":
                st.success(f'Result: {num1 + num2}')
            elif operation == "Subtract":
                st.success(f'Result: {num1 - num2}')
            elif operation == "Multiply":
                st.success(f'Result: {num1 * num2}')
            elif operation == "Divide":
                st.success(f'Result: {num1 / num2}' if num2 != 0 else 'Cannot divide by zero')
            elif operation == "Square":
                st.success(f'Result: {num1 ** 2}')
            elif operation == "Power (a^b)":
                st.success(f'Result: {num1 ** num2}')
            elif operation == "Cube":
                st.success(f'Result: {num1 ** 3}')
            elif operation == "Square Root":
                st.success(f'Result: {math.sqrt(num1)}')
            elif operation == "Cube Root":
                st.success(f'Result: {num1 ** (1/3)}')
            elif operation == "Log10":
                st.success(f'Result: {math.log10(num1)}')
            elif operation == "Log2":
                st.success(f'Result: {math.log2(num1)}')
            elif operation == "Exponential":
                st.success(f'Result: {math.exp(num1)}')
            elif operation == "Sine":
                st.success(f'Result: {math.sin(math.radians(num1))}')
            elif operation == "Cosine":
                st.success(f'Result: {math.cos(math.radians(num1))}')
            elif operation == "Tangent":
                st.success(f'Result: {math.tan(math.radians(num1))}')
            elif operation == "Factorial":
                if num1 >= 0 and num1 == int(num1):
                    st.success(f'Result: {math.factorial(int(num1))}')
                else:
                    st.error('Factorial is only defined for non-negative integers.')
        except Exception as e:
            st.error(f'Error: {e}')

# =============================== BMI CALCULATOR =============================== #

elif option == "BMI Calculator":
    st.header(" Body Mass Index (BMI) Calculator")

    weight = st.number_input('Enter your weight (kg):', value=0.0)
    height = st.number_input('Enter your height (m):', value=0.0)

    if st.button('Calculate BMI'):
        try:
            bmi = weight /(height ** 2)
            st.success(f'Your BMI is: {bmi:.2f}')
        except ZeroDivisionError:
            st.error('Height cannot be zero.')

# =============================== GST CALCULATOR =============================== #

elif option == "GST Calculator":
    st.subheader("GST Calculator")

    amount = st.number_input("Enter Amount(₹):", value=0.0)
    gst_rate = st.number_input("Enter GST Rate (%):", value=0.0)

    if st.button("Calculate GST"):
        gst = (amount * gst_rate) / 100
        total_amount = amount + gst
        st.success(f"GST Amount: ₹{gst:.2f}")
        st.success(f"Total Amount (including GST): ₹{total_amount:.2f}")