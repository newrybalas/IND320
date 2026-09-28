import streamlit as st
import random

# solution 1
# Initialize session state
# if 'number' not in st.session_state:
#     st.session_state.number = None

# # Function to update the number
# def next_number():

#     # First click: generate a random number
#     if st.session_state.number is None:
#         st.session_state.number = random.randint(1, 100)

#     # If the number is even, divide by 2
#     elif st.session_state.number % 2 == 0:
#         st.session_state.number //= 2

#     # If the number is odd, multiply by 3 and add 1
#     else:
#         st.session_state.number = st.session_state.number * 3 + 1


# # Choose button label
# if st.session_state.number is None:
#     label = "Start"

# elif st.session_state.number % 2 == 0:
#     label = "Half it"

# else:
#     label = "Triple and add one"


# # Display button
# st.button(label, on_click=next_number)

# # Display output
# if st.session_state.number is None:
#     st.write("Ready")
# else:
#     st.write(st.session_state.number)

#python -m streamlit run streamlit/Excercise.py

#Solution 2
import streamlit as st
import random

st.title("Collatz conjecture")

# Initialize session state
if "value" not in st.session_state:
    st.session_state.value = None
    st.session_state.started = False
    button_label = "Start"
else:
    if st.session_state.value == 1:
        button_label = "Success!"
    else:
        if st.session_state.value % 2 == 0:
            button_label = "Half it"
        else:
            button_label = "Triple and add one"

# Button label depends on state
st.button(button_label, disabled=st.session_state.value == 1)

if st.session_state.value == 1:
    st.balloons()

# Output
if not st.session_state.started:
    st.write("Ready")
else:
    st.write(st.session_state.value)

if not st.session_state.started:
    # First press: sample random integer and cache it
    st.session_state.value = random.randint(1, 100)
    st.session_state.started = True
else:
    # Subsequent presses: apply Collatz update
    if st.session_state.value % 2 == 0:
        st.session_state.value //= 2
    else:
        st.session_state.value = st.session_state.value * 3 + 1