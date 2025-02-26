import streamlit as st

# Set up page config
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="✮")

# Title of the app
st.title("Growth Mindset Challenge: Web App With Streamlit")

# Header section
st.header("✨ Welcome to The Growth Journey!")
st.write("╰┈➤ Welcome challenges, grow through your experiences, and unleash your true potential. This AI-powered app is designed to help you cultivate a growth mindset through reflection and celebrating your achievements! ❤️️")

# Quote Section
st.header("✔️ Today's Growth Mindset Quote!")
st.write("Achievement is not the end, and setbacks are not the end either; what truly matters is the determination to keep moving forward.")

# Challenge Section
st.header("⌛ What's Your Growth Challenge?")
user_input = st.text_input("Describe a challenge you're facing:")

# Condition for user input
if user_input:
    st.success(f"🙌 You are facing: {user_input}. Keep pushing forward towards your goal! 😊")
else:
    st.warning("Tell us about your challenge to get started!")

# Reflection Section
st.header("Reflect on Your Learning")
reflection = st.text_area("Write your outcome here:")

if reflection:
    st.success(f"✨ Great insight! Your reflection: {reflection}")
else:
    st.info("Reflect on past experiences that helped you grow! Share your thoughts here.")

# Achievements Section
st.header("✨ Rejoice in Your Victories.")
achievement = st.text_input("Tell me about something you've achieved recently:")

if achievement:
    st.success(f"🙌 Amazing! You achieved: {achievement}")
else:
    st.info("Whether big or small, every win matters! Share one with me 😊")

# Footer Section
st.write("- - - -")
st.write("Growth is a journey, not a destination 🌱. Keep moving forward, one step at a time 🚶‍♂️.")
st.markdown('<p style="text-align: center;"><strong>© Created By Abdullah Naeem!</strong></p>', unsafe_allow_html=True)
