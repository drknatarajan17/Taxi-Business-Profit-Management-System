import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# PAGE CONFIGURATION
# ----------------------------------------------------

st.set_page_config(
    page_title="Taxi Business Profit Management System",
    page_icon="🚖",
    layout="wide"
)

# ----------------------------------------------------
# LOAD DATA
# ----------------------------------------------------

try:
    df = pd.read_csv("taxi_business.csv")
except:
    df = pd.DataFrame()

# ----------------------------------------------------
# SIDEBAR
# ----------------------------------------------------

st.sidebar.title("🚖 Taxi Business System")

menu = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Dashboard",
        "💰 Profit Calculator",
        "📊 Business Analytics",
        "🚕 Taxi Details",
        "👨 Driver Details",
        "⛽ Fuel Analysis",
        "📅 Reports",
        "ℹ About"
    ]
)

# ----------------------------------------------------
# DASHBOARD
# ----------------------------------------------------

if menu == "🏠 Dashboard":

    st.title("🚖 Taxi Business Profit Management System")

    st.markdown(
        "### Smart Financial Dashboard for Taxi Owners"
    )

    if len(df) == 0:

        st.warning("Dataset not found.")

    else:

        total_revenue = df["Revenue"].sum()

        total_profit = df["Net_Profit"].sum()

        total_trips = df["Trips"].sum()

        total_fuel = df["Fuel_Cost"].sum()

        c1, c2, c3, c4 = st.columns(4)

        c1.metric(
            "💰 Revenue",
            f"₹{total_revenue:,.0f}"
        )

        c2.metric(
            "📈 Profit",
            f"₹{total_profit:,.0f}"
        )

        c3.metric(
            "🚖 Trips",
            f"{total_trips}"
        )

        c4.metric(
            "⛽ Fuel Cost",
            f"₹{total_fuel:,.0f}"
        )

        st.markdown("---")

        st.subheader("Business Dataset")

        st.dataframe(df)

        st.markdown("---")

        st.subheader("Quick Statistics")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Average Daily Revenue",
            f"₹{df['Revenue'].mean():.0f}"
        )

        c2.metric(
            "Average Daily Profit",
            f"₹{df['Net_Profit'].mean():.0f}"
        )

        c3.metric(
            "Average Trips",
            round(df["Trips"].mean(),1)
        )

        st.markdown("---")

        st.subheader("Revenue vs Profit")

        fig, ax = plt.subplots(figsize=(10,4))

        ax.plot(
            df["Revenue"],
            label="Revenue"
        )

        ax.plot(
            df["Net_Profit"],
            
            label="Profit"
        )

        ax.legend()

        st.pyplot(fig)
        # ----------------------------------------------------
# OWNER PROFIT CALCULATOR
# ----------------------------------------------------

elif menu == "💰 Profit Calculator":

    st.title("💰 Taxi Owner Profit Calculator")

    st.markdown("### Daily Business Calculation")

    total_income = st.number_input(
        "Total Revenue from Customer (₹)",
        value=1000.0,
        step=100.0
    )

    st.markdown("---")

    st.subheader("Revenue Distribution")

    driver_salary = st.number_input(
        "Driver Salary (₹)",
        value=300.0
    )

    agent_commission = st.number_input(
        "Taxi Agent Commission (₹)",
        value=200.0
    )

    owner_share = total_income - driver_salary - agent_commission

    st.success(
        f"Owner Share Before Expenses : ₹{owner_share:.0f}"
    )

    st.markdown("---")

    st.subheader("Owner Expenses")

    fuel = st.number_input(
        "Fuel Cost (₹)",
        value=180.0
    )

    emi = st.number_input(
        "Daily EMI (₹)",
        value=100.0
    )

    maintenance = st.number_input(
        "Maintenance (₹)",
        value=40.0
    )

    insurance = st.number_input(
        "Insurance (₹)",
        value=20.0
    )

    road_tax = st.number_input(
        "Road Tax / Permit (₹)",
        value=15.0
    )

    miscellaneous = st.number_input(
        "Miscellaneous (₹)",
        value=25.0
    )

    total_owner_expense = (
        fuel
        + emi
        + maintenance
        + insurance
        + road_tax
        + miscellaneous
    )

    final_profit = owner_share - total_owner_expense

    st.markdown("---")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Owner Share",
        f"₹{owner_share:.0f}"
    )

    c2.metric(
        "Owner Expenses",
        f"₹{total_owner_expense:.0f}"
    )

    c3.metric(
        "Owner Net Profit",
        f"₹{final_profit:.0f}"
    )

    st.markdown("---")

    st.subheader("Profit Flow")

    st.write(f"Customer Paid : ₹{total_income:.0f}")

    st.write(f"Less Driver Salary : ₹{driver_salary:.0f}")

    st.write(f"Less Agent Commission : ₹{agent_commission:.0f}")

    st.write(f"Owner Share : ₹{owner_share:.0f}")

    st.write(f"Less Fuel : ₹{fuel:.0f}")

    st.write(f"Less EMI : ₹{emi:.0f}")

    st.write(f"Less Maintenance : ₹{maintenance:.0f}")

    st.write(f"Less Insurance : ₹{insurance:.0f}")

    st.write(f"Less Road Tax : ₹{road_tax:.0f}")

    st.write(f"Less Miscellaneous : ₹{miscellaneous:.0f}")

    st.success(
        f"Final Owner Profit : ₹{final_profit:.0f}"
    )

    st.markdown("---")

    if final_profit >= 200:

        st.success("🟢 Excellent Business Performance")

    elif final_profit >= 100:

        st.info("🟡 Good Profit")

    elif final_profit >= 50:

        st.warning("🟠 Low Profit")

    else:

        st.error("🔴 Loss / Very Low Profit")

    st.markdown("---")

    st.subheader("AI Business Suggestions")

    if fuel > owner_share * 0.40:

        st.warning(
            "Fuel expense is consuming more than 40% of the owner's share."
        )

    if emi > 150:

        st.warning(
            "High EMI. Consider refinancing if possible."
        )

    if maintenance > 60:

        st.warning(
            "Vehicle maintenance is high. Schedule preventive servicing."
        )

    if final_profit > 250:

        st.success(
            "Business is highly profitable. Consider adding another vehicle."
        )
    # ----------------------------------------------------
# BUSINESS ANALYTICS
# ----------------------------------------------------

elif menu == "📊 Business Analytics":

    st.title("📊 Taxi Business Analytics Dashboard")

    if len(df) == 0:

        st.error("Dataset not found.")

    else:

        total_revenue = df["Revenue"].sum()

        total_profit = df["Net_Profit"].sum()

        total_driver = df["Driver_Salary"].sum()

        total_agent = df["Agent_Commission"].sum()

        total_fuel = df["Fuel_Cost"].sum()

        total_emi = df["EMI"].sum()

        total_maintenance = df["Maintenance"].sum()

        total_insurance = df["Insurance"].sum()

        total_tax = df["Road_Tax"].sum()

        c1,c2,c3,c4 = st.columns(4)

        c1.metric(
            "Total Revenue",
            f"₹{total_revenue:,.0f}"
        )

        c2.metric(
            "Owner Profit",
            f"₹{total_profit:,.0f}"
        )

        c3.metric(
            "Fuel Expense",
            f"₹{total_fuel:,.0f}"
        )

        c4.metric(
            "Driver Salary",
            f"₹{total_driver:,.0f}"
        )

        st.markdown("---")

        st.subheader("📈 Revenue vs Profit")

        fig, ax = plt.subplots(figsize=(12,4))

        ax.plot(
            df["Revenue"],
            color="green",
            label="Revenue"
        )

        ax.plot(
            df["Net_Profit"],
            color="blue",
            label="Profit"
        )

        ax.legend()

        ax.set_xlabel("Business Days")

        ax.set_ylabel("Amount (₹)")

        st.pyplot(fig)

        st.markdown("---")

        st.subheader("💸 Expense Distribution")

        expense = pd.DataFrame({

            "Expense":[
                "Driver",
                "Agent",
                "Fuel",
                "EMI",
                "Maintenance",
                "Insurance",
                "Road Tax"
            ],

            "Amount":[
                total_driver,
                total_agent,
                total_fuel,
                total_emi,
                total_maintenance,
                total_insurance,
                total_tax
            ]

        })

        fig2, ax2 = plt.subplots(figsize=(8,8))

        ax2.pie(
            expense["Amount"],
            labels=expense["Expense"],
            autopct="%1.1f%%"
        )

        ax2.set_title("Expense Analysis")

        st.pyplot(fig2)

        st.markdown("---")

        st.subheader("🏆 Business Performance")

        profit_percentage = (
            total_profit /
            total_revenue
        ) * 100

        st.metric(
            "Profit Margin",
            f"{profit_percentage:.2f}%"
        )

        if profit_percentage >= 25:

            st.success("🟢 Excellent Business Performance")

        elif profit_percentage >= 15:

            st.info("🟡 Good Business")

        elif profit_percentage >= 10:

            st.warning("🟠 Average Business")

        else:

            st.error("🔴 Poor Business Performance")

        st.markdown("---")

        st.subheader("🤖 AI Business Recommendation")

        if total_fuel > total_revenue * 0.30:

            st.warning(
                "Fuel expenses are too high. Improve route planning."
            )

        if total_maintenance > total_revenue * 0.08:

            st.warning(
                "Maintenance cost is increasing. Schedule preventive servicing."
            )

        if total_profit < total_revenue * 0.10:

            st.error(
                "Business profitability is low. Reduce operating expenses."
            )

        if total_profit > total_revenue * 0.20:

            st.success(
                "Excellent profitability. Fleet expansion can be considered."
            )

        st.markdown("---")

        st.subheader("📋 Complete Business Report")

        st.dataframe(df)
        # ----------------------------------------------------
# TAXI DETAILS
# ----------------------------------------------------

elif menu == "🚕 Taxi Details":

    st.title("🚕 Taxi Information")

    taxi_no = st.text_input("Vehicle Number", "TS09AB1234")

    vehicle = st.selectbox(
        "Vehicle Type",
        [
            "Sedan",
            "Hatchback",
            "SUV",
            "Electric Taxi"
        ]
    )

    owner = st.text_input(
        "Owner Name",
        "Natarajan"
    )

    purchase = st.number_input(
        "Purchase Price (₹)",
        value=900000
    )

    loan = st.number_input(
        "Loan Amount (₹)",
        value=700000
    )

    emi = st.number_input(
        "Monthly EMI (₹)",
        value=18000
    )

    insurance = st.number_input(
        "Yearly Insurance (₹)",
        value=25000
    )

    permit = st.date_input(
        "Permit Expiry"
    )

    fitness = st.date_input(
        "Fitness Certificate Expiry"
    )

    pollution = st.date_input(
        "Pollution Certificate Expiry"
    )

    st.success("Vehicle details recorded successfully.")

# ----------------------------------------------------
# DRIVER DETAILS
# ----------------------------------------------------

elif menu == "👨 Driver Details":

    st.title("👨 Driver Information")

    driver = st.text_input(
        "Driver Name",
        "Ravi"
    )

    mobile = st.text_input(
        "Mobile Number"
    )

    license_no = st.text_input(
        "Driving License Number"
    )

    experience = st.slider(
        "Experience (Years)",
        0,
        30,
        5
    )

    rating = st.slider(
        "Driver Rating",
        1.0,
        5.0,
        4.5
    )

    salary = st.number_input(
        "Monthly Salary",
        value=18000
    )

    attendance = st.slider(
        "Attendance %",
        0,
        100,
        95
    )

    st.metric(
        "Attendance",
        f"{attendance}%"
    )

    if attendance >= 95:

        st.success("Excellent Driver")

    elif attendance >= 80:

        st.info("Good Driver")

    else:

        st.warning("Needs Improvement")

# ----------------------------------------------------
# FUEL ANALYSIS
# ----------------------------------------------------

elif menu == "⛽ Fuel Analysis":

    st.title("⛽ Fuel Analytics")

    distance = st.number_input(
        "Distance Travelled (km)",
        value=250
    )

    fuel_used = st.number_input(
        "Fuel Used (Litres)",
        value=20.0
    )

    fuel_price = st.number_input(
        "Fuel Price/Litre",
        value=110.0
    )

    mileage = distance / fuel_used

    fuel_cost = fuel_used * fuel_price

    cost_per_km = fuel_cost / distance

    c1,c2,c3 = st.columns(3)

    c1.metric(
        "Mileage",
        f"{mileage:.2f} km/L"
    )

    c2.metric(
        "Fuel Cost",
        f"₹{fuel_cost:.0f}"
    )

    c3.metric(
        "Cost / km",
        f"₹{cost_per_km:.2f}"
    )

    if mileage >= 18:

        st.success("Excellent Fuel Efficiency")

    elif mileage >= 15:

        st.info("Good Fuel Efficiency")

    else:

        st.warning("Vehicle needs servicing")

# ----------------------------------------------------
# REPORTS
# ----------------------------------------------------

elif menu == "📅 Reports":

    st.title("📅 Business Reports")

    if len(df)==0:

        st.warning("No data available.")

    else:

        st.write(df)

        st.download_button(

            "📥 Download CSV Report",

            data=df.to_csv(index=False),

            file_name="Taxi_Business_Report.csv",

            mime="text/csv"

        )

        st.markdown("---")

        st.subheader("Summary")

        st.write(
            f"Total Revenue : ₹{df['Revenue'].sum():,.0f}"
        )

        st.write(
            f"Total Profit : ₹{df['Net_Profit'].sum():,.0f}"
        )

        st.write(
            f"Average Daily Profit : ₹{df['Net_Profit'].mean():.0f}"
        )

# ----------------------------------------------------
# ABOUT
# ----------------------------------------------------

elif menu == "ℹ About":

    st.title("ℹ About Project")

    st.markdown("""

# 🚖 Taxi Business Profit Management System

### Features

- Daily Revenue Tracking

- Driver Salary Management

- Taxi Agent Commission

- Owner Profit Calculator

- Fuel Analytics

- Business Dashboard

- Expense Analysis

- CSV Report Download

- AI Business Suggestions

---

### Technologies

- Python

- Streamlit

- Pandas

- Matplotlib

---

### Future Enhancements

- Multiple Taxi Management

- Fleet Analytics

- GPS Tracking

- Google Maps Integration

- AI Profit Prediction

- Break-even Analysis

- ROI Calculator

- Driver Performance Analytics

- Mobile App

---

Developed using Python and Streamlit.

""")
    
