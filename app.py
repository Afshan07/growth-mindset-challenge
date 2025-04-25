import streamlit as st
import random

# Page config
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱")

# Title
st.title("🌱 Growth Mindset Challenge")
st.subheader("Fuel your mind with a daily dose of motivation!")

# Quotes list
quotes = [
    "Mistakes are proof you are trying.",
    "Every expert was once a beginner.",
    "Difficult roads often lead to beautiful destinations.",
    "Your only limit is your mind.",
    "Small progress is still progress.",
    "Failure is the opportunity to begin again more intelligently.",
    "You can do hard things.",
    "Believe in yourself and all that you are."
]

# Show random quote
if st.button("🌟 New Quote"):
    st.success(random.choice(quotes))
else:
    st.info("Click the button to get your motivational quote!")

# Footer
st.markdown("---")
st.caption(st.caption("Made with 💚 by [Afshan](https://github.com/Afshan07)")
)
