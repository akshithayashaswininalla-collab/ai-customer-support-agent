import streamlit as st

# -------------------- PAGE CONFIG --------------------
st.set_page_config(page_title="Tiny Tots Doll Shop Support", page_icon="🧸", layout="centered")

# -------------------- CUSTOM THEME --------------------
st.markdown(
    """
    <style>
        :root {
            --bg: #fffdf8;
            --card: #ffffff;
            --primary: #4f46e5;
            --secondary: #ec4899;
            --accent: #84cc16;
            --accent2: #8b5cf6;
            --accent3: #f59e0b;
            --accent4: #a16207;
            --text: #000000;
            --muted: #1f2937;
        }

        .stApp {
            background: linear-gradient(135deg, #dff7ff 0%, #ffe8f3 50%, #fff4cf 100%);
            color: var(--text);
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(135deg, #4338ca 0%, #7c3aed 45%, #ec4899 100%);
            color: #000000;
            border-right: none;
        }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            position: relative;
        }

        .block-container::before {
            content: "";
            position: absolute;
            inset: 0;
            background-image: radial-gradient(circle, #ffd166 8px, transparent 9px), radial-gradient(circle, #8ec5ff 7px, transparent 8px), radial-gradient(circle, #f7b6d2 7px, transparent 8px);
            background-size: 34px 34px, 46px 46px, 38px 38px;
            animation: driftBubbles 9s linear infinite;
            opacity: 0.22;
            pointer-events: none;
            z-index: 0;
        }

        .block-container > * {
            position: relative;
            z-index: 1;
        }

        .stChatInput {
            background: linear-gradient(135deg, rgba(255,255,255,0.98), rgba(255,242,214,0.98));
            border: 2px solid #4b2e1f;
            border-radius: 24px;
            padding: 0.7rem;
            box-shadow: 0 8px 24px rgba(75, 46, 31, 0.16);
        }

        @keyframes driftBubbles {
            0% { transform: translateY(0px) translateX(0px); }
            50% { transform: translateY(-10px) translateX(6px); }
            100% { transform: translateY(0px) translateX(0px); }
        }

        .hero-card {
            background: linear-gradient(135deg, #4f46e5 0%, #ec4899 45%, #f59e0b 100%);
            border-radius: 24px;
            padding: 1.2rem 1.3rem;
            margin-bottom: 1rem;
            box-shadow: 0 14px 32px rgba(0, 0, 0, 0.14);
            border: 2px solid #ffffff;
        }

        .hero-title {
            font-size: 1.7rem;
            font-weight: 900;
            color: #ffffff;
            margin-bottom: 0.2rem;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
        }

        .hero-subtitle {
            color: #fff7ed;
            font-size: 1rem;
            font-weight: 700;
        }

        .kid-badge {
            display: inline-block;
            margin-top: 0.55rem;
            padding: 0.35rem 0.7rem;
            border-radius: 999px;
            background: rgba(255,255,255,0.9);
            font-weight: 800;
            color: #111827;
        }

        .stChatMessage {
            border-radius: 16px;
            padding: 0.55rem 0.8rem;
            border: 2px solid #4b2e1f;
            background: linear-gradient(135deg, rgba(255,255,255,0.97), rgba(255,242,214,0.97));
            color: #1f1a13;
            position: relative;
            overflow: hidden;
        }

        .stChatMessage::before {
            content: "";
            position: absolute;
            inset: 0;
            background-image: radial-gradient(circle, #ffcc80 8px, transparent 9px), radial-gradient(circle, #8ec5ff 7px, transparent 8px), radial-gradient(circle, #f7b6d2 7px, transparent 8px);
            background-size: 30px 30px, 40px 40px, 35px 35px;
            animation: floatDots 6s linear infinite;
            opacity: 0.22;
            pointer-events: none;
        }

        .stChatMessage [data-testid="stMarkdownContainer"] p,
        .stChatMessage [data-testid="stMarkdownContainer"] div {
            color: #1f1a13 !important;
            font-weight: 700;
            position: relative;
            z-index: 1;
        }

        @keyframes floatDots {
            0% { transform: translateY(0px) translateX(0px); }
            50% { transform: translateY(-8px) translateX(6px); }
            100% { transform: translateY(0px) translateX(0px); }
        }

        .stTextInput > div > div > input {
            border-radius: 999px;
            border: 2px solid #2e1a6b;
            padding: 0.8rem 1rem;
            box-shadow: 0 4px 14px rgba(67, 56, 202, 0.16);
            color: #1f1a13;
            background: #ffffff;
            font-weight: 700;
        }

        .stButton > button {
            border-radius: 999px;
            background: linear-gradient(90deg, #4338ca, #ec4899);
            color: #ffffff;
            border: none;
            font-weight: 800;
            box-shadow: 0 4px 12px rgba(0,0,0,0.16);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------- SIDEBAR --------------------
st.sidebar.title("🧸 Tiny Tots Support")
st.sidebar.write("Happy help for little shoppers")
st.sidebar.info("Friendly support for dolls, toys, and gifts")

st.sidebar.write("### 🌈 What we help with")
st.sidebar.write("- Dolls and plush toys")
st.sidebar.write("- Age suggestions")
st.sidebar.write("- Delivery and returns")
st.sidebar.write("- Safe toy advice")

# -------------------- TITLE --------------------
st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">🧸🌈 Tiny Tots Doll Shop Support</div>
        <div class="hero-subtitle">Cheerful help for kids' toys, dolls, gifts, and happy shopping moments.</div>
        <div class="kid-badge">💖 Ask me anything about our toy shop</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.divider()

# -------------------- SESSION STATE (CHAT HISTORY) --------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi there, parent! Welcome to Tiny Tots Doll Shop 🌈🧸 I’m here to help you with your toy order and any questions about your little one’s surprise.",
        }
    ]

# -------------------- USER INPUT --------------------
user_input = st.chat_input("Ask about toys, age, delivery, safety, or gifts...")

# -------------------- RESPONSE LOGIC --------------------
def generate_response(user_text):
    text = user_text.lower()

    if any(word in text for word in ["hello", "hi", "hey", "hola"]):
        return "Hello, parent! 🌈 I’m here to help with your toy order, gift ideas, safe choices, delivery, and returns."

    if any(word in text for word in ["refund", "return", "exchange", "damaged"]):
        return "Absolutely! If your toy or doll arrives damaged or isn’t quite right for your child, we can help with a return or exchange. Please share your order number so I can guide you."

    if any(word in text for word in ["delivery", "ship", "arrive", "when", "reach"]):
        return "We usually deliver within 2–4 working days, so your little one’s toy surprise should arrive soon and safely."

    if any(word in text for word in ["price", "cost", "budget", "cheap", "offer", "discount"]):
        return "We have lovely toys and dolls for many budgets, and we also offer special deals for bundles and birthday gifts."

    if any(word in text for word in ["age", "years old", "years", "suitable", "for age"]):
        return "I can help you choose the best toy by age. Soft plush toys are lovely for ages 1–3, while building toys and puzzles are great for ages 4+."

    if any(word in text for word in ["safe", "safety", "non-toxic", "soft", "material", "baby"]):
        return "Yes! Our toys are made with child-safe materials and soft finishes, so they are gentle and safe for little hands."

    if any(word in text for word in ["doll", "toy", "plush", "bear", "puzzle", "car", "gift"]):
        return "We have many lovely options such as dolls, plush bears, puzzles, ride-ons, and gift sets. Tell me your child’s age or favorite theme and I’ll help you pick the perfect one!"

    if any(word in text for word in ["payment", "card", "cash", "upi", "online", "pay"]):
        return "We accept secure online payments through card, UPI, and other trusted methods."

    if any(word in text for word in ["custom", "name", "personal", "birthday"]):
        return "We can help with birthday gift ideas and personalized toy options. Tell me your child’s age and favorite color, and I’ll help you choose."

    if any(word in text for word in ["help", "support", "question", "need"]):
        return "I’m happy to help! Ask me about your toy order, dolls, age recommendations, safety, delivery, returns, or gift ideas."

    return "Thanks for asking! I can help with your toy order, dolls, age suggestions, safety, delivery, payment, and returns. 😊"

# -------------------- DISPLAY CHAT --------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# -------------------- HANDLE INPUT --------------------
text_to_send = user_input

if text_to_send:
    st.session_state.messages.append({"role": "user", "content": text_to_send})

    bot_reply = generate_response(text_to_send)
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    st.rerun()