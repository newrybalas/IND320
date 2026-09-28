import streamlit as st

if 'counter' not in st.session_state:
    st.session_state.counter = 0

# if 'second_counter' not in st.session_state:
#     st.session_state.second_counter = 0
# st.session_state.second_counter += 1

def increment():
    st.session_state.counter += 1

st.button("Increment", on_click=increment)
st.write(f"Button clicked {st.session_state.counter} times")
# st.write(f"Second counter: {st.session_state.second_counter} times")


#python -m streamlit run streamlit/session_state.py 
#st.session_state-counter = Den gjor at telleren husker verdien sin selv om Streamlit kjører koden på nytt etter hvert klikk.
# strl+r = rerun

#Streamlit kjører hele skriptet på nytt ved hver interaksjon, men st.session_state husker verdiene fra forrige kjøring.
#Derfor får læreren 2 på second_counter etter én vanlig rerun i samme sesjon, mens counter fortsatt er 0.

# Funksjonen increment() kjøres, og counter øker med 1.
# Streamlit kjører hele skriptet på nytt, slik at second_counter også øker med 1.

#counter øker bare når du klikker på Increment, mens second_counter øker hver gang skriptet kjøres, uansett årsak.