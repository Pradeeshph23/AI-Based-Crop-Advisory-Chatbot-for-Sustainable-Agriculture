import streamlit as st

# App Title
st.title("🌱 AI Crop Advisory Chatbot")
st.subheader("Promoting Sustainable Agriculture using AI")

st.write(
    "This chatbot provides eco-friendly crop advisory to farmers "
    "using AI-based logic and sustainable farming principles."
)

# Input from user
user_input = st.text_input("Enter your crop or farming issue:")

def crop_advisory_chatbot(user_input):
    user_input = user_input.lower()

    if "rice" in user_input:
        return (
            "🌾 Rice Advisory:\n"
            "- Use water efficiently.\n"
            "- Apply organic fertilizers.\n"
            "- Monitor pests and use eco-friendly pesticides."
        )

    elif "wheat" in user_input:
        return (
            "🌾 Wheat Advisory:\n"
            "- Ensure proper soil drainage.\n"
            "- Follow crop rotation.\n"
            "- Avoid excessive chemical fertilizers."
        )

    elif "pest" in user_input:
        return (
            "🐛 Pest Management Advisory:\n"
            "- Identify pests early.\n"
            "- Use biological pest control.\n"
            "- Minimize chemical pesticide usage."
        )

    elif "fertilizer" in user_input:
        return (
            "🧪 Fertilizer Advisory:\n"
            "- Prefer organic compost.\n"
            "- Avoid overuse of nitrogen fertilizers.\n"
            "- Follow recommended dosage."
        )

    elif "soil" in user_input:
        return (
            "🌱 Soil Health Advisory:\n"
            "- Test soil regularly.\n"
            "- Use green manure.\n"
            "- Avoid monocropping."
        )

    else:
        return (
            "🌍 General Sustainable Farming Tips:\n"
            "- Save water.\n"
            "- Reduce chemical usage.\n"
            "- Practice eco-friendly farming."
        )

# Button
if st.button("Get Advisory"):
    if user_input:
        response = crop_advisory_chatbot(user_input)
        st.success(response)
    else:
        st.warning("Please enter a crop or issue.")
