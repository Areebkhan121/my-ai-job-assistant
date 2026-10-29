import streamlit as st
from urllib.parse import quote_plus

st.set_page_config(
    page_title="My AI Job Assistant",
    page_icon="💼"
)

st.title("💼 My AI Job Assistant")
st.write("Find fresher job opportunities and prepare to apply.")

st.header("Your preferences")

city = st.text_input("Preferred city", "Bengaluru")

qualification = st.selectbox(
    "Qualification",
    ["BBM", "BBA", "B.Com", "MBA", "Other"]
)

experience = st.selectbox(
    "Experience",
    ["Fresher", "Less than 1 year", "1–2 years"]
)

salary = st.number_input(
    "Minimum monthly salary (₹)",
    min_value=0,
    value=35000,
    step=5000
)

roles = st.multiselect(
    "Choose job roles",
    [
        "Logistics Executive",
        "Supply Chain Executive",
        "Procurement Assistant",
        "Purchase Executive",
        "Sales Operations Executive",
        "Marketing Executive",
        "International Sales Support",
        "Business Development Executive"
    ],
    default=["Logistics Executive", "Procurement Assistant"]
)

if st.button("Find Jobs"):
    if not city.strip():
        st.error("Enter your preferred city.")
    elif not roles:
        st.warning("Select at least one job role.")
    else:
        st.subheader("Job search links")

        for role in roles:
            query = (
                f"{role} {city} fresher full-time "
                f"salary at least {salary} INR monthly"
            )

            st.markdown(f"### {role}")

            google_url = (
                "https://www.google.com/search?q="
                + quote_plus(query + " jobs")
            )

            linkedin_url = (
                "https://www.linkedin.com/jobs/search/?keywords="
                + quote_plus(role + " fresher")
                + "&location="
                + quote_plus(city)
            )

            st.link_button("Search Google", google_url)
            st.link_button("Search LinkedIn", linkedin_url)

st.caption(
    "Starter version: verify salary, eligibility, and vacancy "
    "details with the employer before applying."
)
