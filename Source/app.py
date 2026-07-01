import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="NexGen Gaming | Executive Dashboard",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PROFESSIONAL CSS
# =====================================================

st.markdown("""
<style>

/* Background */
.stApp{
    background:#0F172A;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#111827;
}

[data-testid="stSidebar"] *{
    color:white;
}

/* Headers */

h1{
    color:white;
    font-weight:700;
}

h2{
    color:#38BDF8;
}

h3{
    color:white;
}

/* KPI Cards */

[data-testid="metric-container"]{
    background:#1E293B;
    border-radius:15px;
    padding:20px;
    border-left:6px solid #38BDF8;
    box-shadow:0px 0px 12px rgba(0,0,0,.4);
}

[data-testid="metric-container"] label{
    color:white !important;
}

[data-testid="metric-container"] div{
    color:white !important;
}

/* Dataframe */

[data-testid="stDataFrame"]{
    border-radius:12px;
}

/* Buttons */

.stDownloadButton button{
    background:#2563EB;
    color:white;
    border:none;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================

@st.cache_data
def load_data():

    df = pd.read_csv("video_game_sales_cleaned.csv")

    df.drop_duplicates(inplace=True)

    df["Year"] = pd.to_numeric(
        df["Year"],
        errors="coerce"
    )

    df = df.dropna(subset=["Year"])

    df["Year"] = df["Year"].astype(int)

    return df


df = load_data()

# =====================================================
# COMPANY HEADER
# =====================================================

st.markdown("""
# 🎮 NexGen Gaming

### Executive Sales Intelligence Dashboard

Monitor global game sales, platform performance,
publisher growth and regional market trends.

---
""")

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/686/686589.png",
    width=90
)

st.sidebar.title("🎮 NexGen Gaming")

st.sidebar.markdown("---")

st.sidebar.header("Dashboard Filters")

selected_year = st.sidebar.multiselect(
    "Select Year",
    sorted(df["Year"].unique()),
    default=sorted(df["Year"].unique())
)

selected_platform = st.sidebar.multiselect(
    "Platform",
    sorted(df["Platform"].unique()),
    default=sorted(df["Platform"].unique())
)

selected_genre = st.sidebar.multiselect(
    "Genre",
    sorted(df["Genre"].unique()),
    default=sorted(df["Genre"].unique())
)

selected_publisher = st.sidebar.multiselect(
    "Publisher",
    sorted(df["Publisher"].unique()),
    default=sorted(df["Publisher"].unique())
)

filtered_df = df[
    (df["Year"].isin(selected_year))
    &
    (df["Platform"].isin(selected_platform))
    &
    (df["Genre"].isin(selected_genre))
    &
    (df["Publisher"].isin(selected_publisher))
]

st.sidebar.markdown("---")

st.sidebar.success(
    f"Games : {filtered_df['Name'].nunique():,}"
)

st.sidebar.info(
    f"Global Sales : {filtered_df['Global_Sales'].sum():.2f} M"
)

# =====================================================
# KPI CALCULATIONS
# =====================================================

total_games = filtered_df["Name"].nunique()

total_publishers = filtered_df["Publisher"].nunique()

total_platforms = filtered_df["Platform"].nunique()

global_sales = filtered_df["Global_Sales"].sum()

na_sales = filtered_df["NA_Sales"].sum()

eu_sales = filtered_df["EU_Sales"].sum()

jp_sales = filtered_df["JP_Sales"].sum()

other_sales = filtered_df["Other_Sales"].sum()

# =====================================================
# EXECUTIVE KPI DASHBOARD
# =====================================================

st.subheader("📊 Executive Overview")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

kpi1.metric(
    "🎮 Total Games",
    f"{total_games:,}"
)

kpi2.metric(
    "🌍 Global Sales",
    f"{global_sales:.2f} M"
)

kpi3.metric(
    "🏢 Publishers",
    f"{total_publishers:,}"
)

kpi4.metric(
    "🖥 Platforms",
    f"{total_platforms:,}"
)

st.write("")

reg1, reg2, reg3, reg4 = st.columns(4)

reg1.metric(
    "🇺🇸 North America",
    f"{na_sales:.2f} M"
)

reg2.metric(
    "🇪🇺 Europe",
    f"{eu_sales:.2f} M"
)

reg3.metric(
    "🇯🇵 Japan",
    f"{jp_sales:.2f} M"
)

reg4.metric(
    "🌎 Other Regions",
    f"{other_sales:.2f} M"
)

st.markdown("---")

# =====================================================
# DATA PREVIEW
# =====================================================

with st.expander("📄 View Filtered Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        height=450
    )

st.markdown("---")

# =====================================================
# EXECUTIVE SALES DASHBOARD
# =====================================================

st.header("📈 Executive Sales Dashboard")

# =====================================================
# ROW 1
# =====================================================

col1, col2 = st.columns(2)

# -----------------------------
# GLOBAL SALES TREND
# -----------------------------
with col1:

    st.subheader("📈 Global Sales Trend")

    year_sales = (
        filtered_df
        .groupby("Year", as_index=False)["Global_Sales"]
        .sum()
    )

    fig = px.line(
        year_sales,
        x="Year",
        y="Global_Sales",
        markers=True,
        template="plotly_dark",
        color_discrete_sequence=["#38BDF8"]
    )

    fig.update_layout(
        paper_bgcolor="#0F172A",
        plot_bgcolor="#1E293B",
        height=450,
        title="Year-wise Global Sales",
        title_x=0.25,
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# TOP 10 GAMES
# -----------------------------
with col2:

    st.subheader("🏆 Top 10 Best Selling Games")

    top_games = (
        filtered_df
        .sort_values(
            "Global_Sales",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        top_games,
        x="Global_Sales",
        y="Name",
        orientation="h",
        color="Global_Sales",
        color_continuous_scale="Blues",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="#0F172A",
        plot_bgcolor="#1E293B",
        height=450,
        yaxis=dict(autorange="reversed"),
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =====================================================
# ROW 2
# =====================================================

col3, col4 = st.columns(2)

# -----------------------------
# TOP PLATFORMS
# -----------------------------
with col3:

    st.subheader("🖥 Top Platforms")

    platform_sales = (
        filtered_df
        .groupby("Platform", as_index=False)["Global_Sales"]
        .sum()
        .sort_values(
            "Global_Sales",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        platform_sales,
        x="Platform",
        y="Global_Sales",
        color="Global_Sales",
        color_continuous_scale="Teal",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="#0F172A",
        plot_bgcolor="#1E293B",
        height=450,
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# TOP PUBLISHERS
# -----------------------------
with col4:

    st.subheader("🏢 Top Publishers")

    publisher_sales = (
        filtered_df
        .groupby("Publisher", as_index=False)["Global_Sales"]
        .sum()
        .sort_values(
            "Global_Sales",
            ascending=False
        )
        .head(10)
    )

    fig = px.bar(
        publisher_sales,
        x="Publisher",
        y="Global_Sales",
        color="Global_Sales",
        color_continuous_scale="Oranges",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="#0F172A",
        plot_bgcolor="#1E293B",
        height=450,
        xaxis_tickangle=-35,
        font_color="white"
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =====================================================
# EXECUTIVE SUMMARY
# =====================================================

top_platform = (
    filtered_df
    .groupby("Platform")["Global_Sales"]
    .sum()
    .idxmax()
)

top_publisher = (
    filtered_df
    .groupby("Publisher")["Global_Sales"]
    .sum()
    .idxmax()
)

top_game = (
    filtered_df
    .sort_values(
        "Global_Sales",
        ascending=False
    )
    .iloc[0]
)

st.success(f"""
### 🎯 Executive Summary

✅ **Best Selling Platform:** {top_platform}

✅ **Leading Publisher:** {top_publisher}

✅ **Highest Selling Game:** {top_game['Name']}

✅ **Global Revenue:** {global_sales:.2f} Million Units

These metrics provide executives with a quick overview of the company's strongest-performing products and business partners.
""")

st.markdown("---")

# =====================================================
# GENRE & REGIONAL ANALYSIS
# =====================================================

st.header("🎯 Market Performance Analysis")

col1, col2 = st.columns(2)

# =====================================================
# GENRE PERFORMANCE
# =====================================================

with col1:

    st.subheader("🎮 Genre Performance")

    genre_sales = (
        filtered_df
        .groupby("Genre", as_index=False)["Global_Sales"]
        .sum()
        .sort_values(
            "Global_Sales",
            ascending=False
        )
    )

    fig = px.bar(
        genre_sales,
        x="Genre",
        y="Global_Sales",
        color="Global_Sales",
        color_continuous_scale="Viridis",
        template="plotly_dark"
    )

    fig.update_layout(
        paper_bgcolor="#0F172A",
        plot_bgcolor="#1E293B",
        font_color="white",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

# =====================================================
# GAMES RELEASED PER YEAR
# =====================================================

with col2:

    st.subheader("📅 Games Released Per Year")

    release = (
        filtered_df
        .groupby("Year", as_index=False)["Name"]
        .count()
        .rename(columns={"Name":"Games"})
    )

    fig = px.area(
        release,
        x="Year",
        y="Games",
        template="plotly_dark",
        color_discrete_sequence=["#06B6D4"]
    )

    fig.update_layout(
        paper_bgcolor="#0F172A",
        plot_bgcolor="#1E293B",
        font_color="white",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# =====================================================
# REGIONAL SALES
# =====================================================

col3, col4 = st.columns(2)

regional_sales = pd.DataFrame({

    "Region":[
        "North America",
        "Europe",
        "Japan",
        "Other"
    ],

    "Sales":[
        na_sales,
        eu_sales,
        jp_sales,
        other_sales
    ]

})

# =====================================================
# REGIONAL BAR CHART
# =====================================================

with col3:

    st.subheader("🌍 Regional Revenue")

    fig = px.bar(
        regional_sales,
        x="Region",
        y="Sales",
        color="Region",
        template="plotly_dark"
    )

    fig.update_layout(

        paper_bgcolor="#0F172A",

        plot_bgcolor="#1E293B",

        font_color="white",

        showlegend=False,

        height=450

    )

    st.plotly_chart(fig,use_container_width=True)

# =====================================================
# DONUT CHART
# =====================================================

with col4:

    st.subheader("🥧 Regional Market Share")

    fig = px.pie(

        regional_sales,

        names="Region",

        values="Sales",

        hole=.55,

        template="plotly_dark"

    )

    fig.update_layout(

        paper_bgcolor="#0F172A",

        font_color="white",

        height=450

    )

    st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

# =====================================================
# HIGHEST SELLING GAME
# =====================================================

st.header("⭐ Business Highlight")

best_game = filtered_df.loc[
    filtered_df["Global_Sales"].idxmax()
]

col1,col2,col3,col4 = st.columns(4)

col1.metric(
    "🎮 Game",
    best_game["Name"]
)

col2.metric(
    "🖥 Platform",
    best_game["Platform"]
)

col3.metric(
    "🎯 Genre",
    best_game["Genre"]
)

col4.metric(
    "🌍 Sales",
    f"{best_game['Global_Sales']:.2f} M"
)

st.markdown("---")

# =====================================================
# CORRELATION HEATMAP
# =====================================================

st.header("📊 Regional Sales Correlation")

corr = filtered_df[

    [

        "NA_Sales",

        "EU_Sales",

        "JP_Sales",

        "Other_Sales",

        "Global_Sales"

    ]

].corr()

fig = px.imshow(

    corr,

    text_auto=".2f",

    color_continuous_scale="RdBu",

    template="plotly_dark",

    aspect="auto"

)

fig.update_layout(

    paper_bgcolor="#0F172A",

    plot_bgcolor="#1E293B",

    font_color="white",

    height=550

)

st.plotly_chart(fig,use_container_width=True)

st.markdown("---")

# =====================================================
# TOP GENRES TABLE
# =====================================================

st.subheader("📋 Top Genres Summary")

genre_table = (

    filtered_df

    .groupby("Genre")

    .agg(

        Games=("Name","count"),

        Global_Sales=("Global_Sales","sum")

    )

    .sort_values(

        "Global_Sales",

        ascending=False

    )

)

st.dataframe(

    genre_table,

    use_container_width=True

)

st.markdown("---")

# =====================================================
# EXECUTIVE INSIGHTS
# =====================================================

st.header("💡 Executive Business Insights")

top_platform = (
    filtered_df.groupby("Platform")["Global_Sales"]
    .sum()
    .idxmax()
)

top_platform_sales = (
    filtered_df.groupby("Platform")["Global_Sales"]
    .sum()
    .max()
)

top_publisher = (
    filtered_df.groupby("Publisher")["Global_Sales"]
    .sum()
    .idxmax()
)

top_publisher_sales = (
    filtered_df.groupby("Publisher")["Global_Sales"]
    .sum()
    .max()
)

top_genre = (
    filtered_df.groupby("Genre")["Global_Sales"]
    .sum()
    .idxmax()
)

top_genre_sales = (
    filtered_df.groupby("Genre")["Global_Sales"]
    .sum()
    .max()
)

top_region = regional_sales.loc[
    regional_sales["Sales"].idxmax(),
    "Region"
]

col1, col2 = st.columns(2)

with col1:

    st.info(f"""
### 🎯 Key Business Insights

🎮 **Top Selling Genre**
- **{top_genre}**
- Generated **{top_genre_sales:.2f} Million** sales.

🖥 **Best Performing Platform**
- **{top_platform}**
- Achieved **{top_platform_sales:.2f} Million** sales.

🏢 **Leading Publisher**
- **{top_publisher}**
- Recorded **{top_publisher_sales:.2f} Million** sales.
""")

with col2:

    st.success(f"""
### 🌍 Market Insights

🌎 Highest Revenue Region:
**{top_region}**

🎮 Total Games Analyzed:
**{total_games:,}**

💻 Platforms Covered:
**{total_platforms}**

🏢 Publishers Covered:
**{total_publishers}**

🌍 Total Global Sales:
**{global_sales:.2f} Million**
""")

st.markdown("---")

# =====================================================
# STRATEGIC RECOMMENDATIONS
# =====================================================

st.header("📌 Strategic Recommendations")

recommendations = pd.DataFrame({

    "Business Area":[
        "Game Development",
        "Marketing",
        "Regional Expansion",
        "Publisher Partnerships",
        "Platform Strategy"
    ],

    "Recommendation":[
        "Invest more in the highest-selling game genres.",
        "Increase promotional campaigns for blockbuster titles.",
        f"Expand operations in {top_region} where demand is strongest.",
        f"Strengthen collaboration with {top_publisher}.",
        f"Continue supporting {top_platform} with exclusive releases."
    ]

})

st.dataframe(
    recommendations,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# =====================================================
# DOWNLOAD DATA
# =====================================================

st.header("📥 Export Filtered Data")

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇ Download Filtered Dataset",
    data=csv,
    file_name="NexGen_Gaming_Executive_Report.csv",
    mime="text/csv"
)

st.markdown("---")

# =====================================================
# ABOUT DASHBOARD
# =====================================================

st.header("🏢 About NexGen Gaming")

st.markdown("""
### Executive Sales Intelligence Dashboard

This dashboard empowers business stakeholders to monitor video game sales performance across:

- 🎮 Games
- 🖥 Gaming Platforms
- 🏢 Publishers
- 🌍 Global Markets
- 🎯 Genres

### Business Objective

Support strategic decision-making by identifying:

- Best-selling games
- High-performing genres
- Strongest regional markets
- Leading publishers
- Platform performance
- Market trends

The insights help executives optimize product strategy, marketing investments, and regional expansion initiatives.
""")

st.markdown("---")

# =====================================================
# FOOTER
# =====================================================

st.markdown(
"""
<div style='text-align:center;
padding:20px;
background:#111827;
border-radius:12px;
color:white;'>

<h3>🎮 NexGen Gaming</h3>

Executive Sales Intelligence Dashboard

Developed using
<b>Python | Streamlit | Pandas | Plotly</b>

© 2026 NexGen Gaming Analytics

</div>
""",
unsafe_allow_html=True
)