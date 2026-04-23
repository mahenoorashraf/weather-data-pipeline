import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px


# ==============================
# 📌 DATABASE CONFIG
# ==============================
DB_PATH = "weather.db"


# ==============================
# 📊 LOAD DATA
# ==============================
@st.cache_data
def load_data():
    conn = sqlite3.connect(DB_PATH)

    query = """
    SELECT 
        city,
        temperature,
        humidity,
        weather_condition,
        timestamp
    FROM weather
    ORDER BY timestamp DESC
    """

    df = pd.read_sql_query(query, conn)
    conn.close()

    df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


# ==============================
# 🎨 PAGE CONFIG
# ==============================
st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("🌤️ Interactive Weather Dashboard")
st.markdown("---")


# ==============================
# 📥 LOAD DATA
# ==============================
df = load_data()

if df.empty:
    st.error("❌ No data found. Run ETL pipeline first.")
    st.stop()


# ==============================
# 🎛️ SIDEBAR FILTERS
# ==============================
st.sidebar.header("🔍 Filters")

city_list = df["city"].unique()
selected_city = st.sidebar.multiselect("Select City", city_list, default=list(city_list))

min_date = df["timestamp"].min().date()
max_date = df["timestamp"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    [min_date, max_date]
)


# ==============================
# 📊 FILTER DATA
# ==============================
filtered_df = df[df["city"].isin(selected_city)]

filtered_df = filtered_df[
    (filtered_df["timestamp"].dt.date >= date_range[0]) &
    (filtered_df["timestamp"].dt.date <= date_range[1])
]


# ==============================
# 📈 KPI METRICS
# ==============================
st.subheader("📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("🌡️ Avg Temp", f"{filtered_df['temperature'].mean():.2f} °C")
col2.metric("💧 Avg Humidity", f"{filtered_df['humidity'].mean():.2f} %")
col3.metric("📍 Cities", filtered_df['city'].nunique())
col4.metric("📊 Records", len(filtered_df))


st.markdown("---")


# ==============================
# 📈 TEMPERATURE TREND (LINE)
# ==============================
st.subheader("🌡️ Temperature Trend")

fig_temp = px.line(
    filtered_df,
    x="timestamp",
    y="temperature",
    color="city",
    markers=True,
    title="Temperature Over Time"
)

st.plotly_chart(fig_temp, use_container_width=True)


# ==============================
# 💧 HUMIDITY TREND
# ==============================
st.subheader("💧 Humidity Trend")

fig_humidity = px.line(
    filtered_df,
    x="timestamp",
    y="humidity",
    color="city",
    markers=True,
    title="Humidity Over Time"
)

st.plotly_chart(fig_humidity, use_container_width=True)


# ==============================
# 🌍 CITY COMPARISON (BAR)
# ==============================
st.subheader("🌍 City-wise Average Temperature")

city_avg = filtered_df.groupby("city")["temperature"].mean().reset_index()

fig_bar = px.bar(
    city_avg,
    x="city",
    y="temperature",
    color="city",
    text_auto=".2f",
    title="Average Temperature by City"
)

st.plotly_chart(fig_bar, use_container_width=True)


# ==============================
# 🌤️ WEATHER CONDITION PIE CHART
# ==============================
st.subheader("🌤️ Weather Condition Distribution")

condition_counts = filtered_df["weather_condition"].value_counts().reset_index()
condition_counts.columns = ["condition", "count"]

fig_pie = px.pie(
    condition_counts,
    names="condition",
    values="count",
    title="Weather Conditions"
)

st.plotly_chart(fig_pie, use_container_width=True)


# ==============================
# 📋 DATA TABLE
# ==============================
st.subheader("📋 Live Data Table")
st.dataframe(filtered_df.sort_values("timestamp", ascending=False), use_container_width=True)


# ==============================
# 🔄 REFRESH BUTTON
# ==============================
if st.button("🔄 Refresh Dashboard"):
    st.cache_data.clear()
    st.rerun()