import streamlit as st
import pandas as pd
import numpy as np

from analytics.stats import (
    most_travelled_destination,
    most_used_transport,
    most_used_fuel,
    average_distance_monthly,
    most_common_purpose,
    average_companions,
    average_spent,
    most_travelled_routes,
    co2_monthly,
    average_toll
)

from analytics.charts import (
    plot_pie,
    plot_line,
    plot_single_value,
    plot_bar
)

st.set_page_config(page_title="Travel Analytics Dashboard", layout="wide")
st.title("Travel Analytics Dashboard")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file is None:
    st.warning("Upload an Excel file to continue.")
    st.stop()

df = pd.read_excel(uploaded_file)

df["Trip Start Date"] = pd.to_datetime(df["Trip Start Date"])

st.subheader("Uploaded Data Preview")
st.write(df.head())

st.subheader("Most Travelled Destinations")
st.table(most_travelled_destination(df))

st.subheader("Most Used Transport Type")
series = most_used_transport(df)
st.pyplot(plot_pie(series, "Most Used Transport"))

st.subheader("Most Used Fuel Type")
series = most_used_fuel(df)
st.pyplot(plot_pie(series, "Most Used Fuel Type"))

st.subheader("Average Distance Per Month")
series = average_distance_monthly(df)
st.pyplot(plot_line(series, "Average Distance Over Time", "Month", "Distance (km)"))

st.subheader("Most Common Trip Purpose")
series = most_common_purpose(df)
st.pyplot(plot_pie(series, "Most Common Trip Purpose"))

st.subheader("Average Companions Per Trip")
st.metric("Average Companions", f"{average_companions(df):.2f}")

st.subheader("Average Spending Per Trip")
st.metric("Avg Spending (INR)", f"{average_spent(df):.2f}")

st.subheader("Most Travelled Routes")
st.table(most_travelled_routes(df))

st.subheader("CO2 Emissions Per Month")
series = co2_monthly(df)
st.pyplot(plot_line(series, "CO2 Emissions Over Time", "Month", "CO2 (kg)"))

st.subheader("Average Toll Cost")
st.metric("Avg Toll (INR)", f"{average_toll(df):.2f}")

