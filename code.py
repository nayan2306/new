import streamlit as st

# Remove Streamlit branding and header/footer
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Title of the app
st.title("Teacher's Day Celebration Invitation")

# Check if the poem visibility state is set, otherwise initialize it
if 'show_poem' not in st.session_state:
    st.session_state.show_poem = False

# Button for the invitation
if st.button('Click for a Surprise!'):
    st.balloons()  # Adds a fun animation
    
    # Display the invitation message
    st.image('8ec853bf-21c9-4ea0-96e4-bcbe3ed29101.webp', caption='Join me for dinner at Neice\'s place!')
    
    st.write("**You're Invited!**")
    st.write("I would be honored if you could join me for dinner to celebrate this special occasion.")
    st.write("📅 **Date**: 5th September")
    st.write("🕕 **Time**: Post 6:00 PM")
    st.write("📍 **Venue**: Neice's Place")

    # Button to reveal the poem
    if st.button('Click to Reveal the Poem'):
        st.session_state.show_poem = True

# Display the poem only if the poem button was clicked
if st.session_state.show_poem:
    poem = """
    From lessons in class to lessons in life,  
    You’ve guided me through every strife.  
    From listening to tantrums, wiping my tears,  
    To showing me the path when it wasn't clear.  

    From a stranger at first, to my teacher so true,  
    Then Masi, the bond between us grew.  
    Thank you for all, for being so kind,  
    For shaping my heart, my soul, and my mind.
    """
    st.markdown(poem)
