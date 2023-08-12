import streamlit as st
import time

def show_fun(age):
    st.write('wow old age ', age)

def get_time():
    return time.time()

def rest_things():
    st.write(get_time())

    age = st.slider('How old are you?', 0, 130, 25)
    st.write("I'm ", age, 'years old')

    if age > 30:
        show_fun(age)

if __name__ == "__main__":
    print('yes ,yes')
    rest_things()
