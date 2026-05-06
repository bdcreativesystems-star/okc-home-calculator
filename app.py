import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="OKC Home Affordability Calculator",
    page_icon="🏡",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("🏡 Oklahoma Rent vs Buy Calculator")

st.write(
    "Find out what home price you may be able to afford based on your current rent."
)

st.divider()

# ---------------- LEAD INFO ----------------
st.subheader("Your Information")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")

st.divider()

# ---------------- INPUTS ----------------
st.subheader("Monthly Housing Information")

rent = st.slider(
    "Current Monthly Rent ($)",
    min_value=800,
    max_value=4000,
    value=1500,
    step=50
)

interest_rate = st.slider(
    "Estimated Interest Rate (%)",
    min_value=5.0,
    max_value=8.0,
    value=6.5,
    step=0.1
)

down_payment = st.slider(
    "Down Payment (%)",
    min_value=3.0,
    max_value=20.0,
    value=5.0,
    step=0.5
)

st.divider()

# ---------------- CALCULATION ----------------
if st.button("Calculate My Buying Power"):

    if not name or not email:
        st.warning("Please enter your name and email.")
    else:

        # Oklahoma affordability estimate
        factor = 0.0072

        estimated_price = rent / factor

        st.success(
            f"🎯 Estimated Home Price: ${estimated_price:,.0f}"
        )

        st.subheader("What This Means")

        st.write(
            f"If you're currently paying **${rent:,}/month in rent**, "
            f"you may be able to afford a home around "
            f"**${estimated_price:,.0f}** in Oklahoma."
        )

        st.info(
            "Down payment assistance and FHA programs may help reduce upfront costs."
        )

        st.write("📩 I'll reach out with personalized options in OKC!")

        # ---------------- SAVE LEAD ----------------
        with open("leads.txt", "a") as f:
            f.write(
                f"{name}, {email}, {phone}, "
                f"Rent: {rent}, "
                f"Rate: {interest_rate}, "
                f"Down: {down_payment}, "
                f"Estimated Price: {estimated_price}\n"
            )