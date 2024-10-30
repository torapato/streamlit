import streamlit as st
import time

st.title("WPM (Words Per Minute) Reader")

# Initialize session state for timer and status tracking
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "elapsed_time" not in st.session_state:
    st.session_state.elapsed_time = 0
if "timer_running" not in st.session_state:
    st.session_state.timer_running = False

# Text input for the passage
text = st.text_area("Paste the text you want to read here:")

# Timer display
st.write(f"Elapsed time: {st.session_state.elapsed_time:.2f} seconds")

# Start and Stop button functionality
if st.button("Start"):
    st.session_state.start_time = time.time()
    st.session_state.timer_running = True

if st.button("Stop"):
    if st.session_state.timer_running:
        st.session_state.elapsed_time = time.time() - st.session_state.start_time
        st.session_state.timer_running = False

# Calculate WPM and display result when timer is stopped
if not st.session_state.timer_running and st.session_state.elapsed_time > 0:
    # Calculate the number of words
    word_count = len(text.split())
    # Calculate WPM
    wpm = word_count / (st.session_state.elapsed_time / 60)
    st.write(f"Your reading speed is: {wpm:.2f} WPM")

# Update timer while it's running
if st.session_state.timer_running:
    st.session_state.elapsed_time = time.time() - st.session_state.start_time
    time.sleep(0.1)  # slight delay for smoother display updates
    st.experimental_rerun()
