import joblib
import numpy as np
import streamlit as st

st.title('Salary Prediction App')

st.divider()

st.write('with this app, you can estimation for the company employees')

years=st.number_input('Enter the years at company',value=1,min_value=0)
jobrate=st.number_input('Enter the job rate',value=3.5, step=0.5, min_value=0.0)

x=[years,jobrate]

model=joblib.load('linearmodel.pkl')

st.divider()

predict=st.button('Press the button for salary prediction')

st.divider()

if predict:
    st.balloons()

    x1=np.array([x])

    prediction=model.predict(x1)[0]

    st.write(f'Salary prediction is {prediction:,.2f}')

else:
    'please press the button for app to make prediction'