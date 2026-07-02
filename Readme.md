# Video Game Sales Analysis Dashboard

An interactive data analytics dashboard built using **Python**, **Pandas**, **Matplotlib**, and **Streamlit** to analyze historical video game sales across different platforms, publishers, genres, and global regions.

The dashboard provides business insights that help understand market trends, top-performing games, regional demand, and publisher performance.

---

# Project Overview

The global video game industry generates billions of dollars every year across multiple gaming platforms, publishers, and regions. Gaming companies often struggle to identify which factors contribute to successful game sales.

This project analyzes historical video game sales data to uncover:

- Sales trends over time
- Best-selling games
- Top-performing platforms
- Leading publishers
- Popular genres
- Regional market performance
- Business recommendations for future decision-making

---

# Problem Statement

Gaming companies need data-driven insights to identify:

- Which platforms generate the highest sales
- Which genres perform best
- Which publishers dominate the market
- Which regions contribute the most revenue
- Historical sales trends for strategic planning

This dashboard helps answer these business questions through interactive visualizations.

---

# Dataset
| **Column Name**                      | **Description**                                                                                                                   |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| **Game Name**                        | The title of the video game. This identifies the specific game being analyzed.                                                    |
| **Platform**                         | The gaming platform on which the game was released (e.g., PlayStation, Xbox, Wii, PC, Nintendo DS).                               |
| **Year**                             | The year in which the video game was officially released. This helps analyze sales trends over time.                              |
| **Genre**                            | The category or type of the game, such as Action, Sports, Role-Playing, Adventure, Racing, Shooter, etc.                          |
| **Publisher**                        | The company responsible for publishing and distributing the video game.                                                           |
| **North America Sales (NA_Sales)**   | Total sales generated in the North American market, measured in **millions of units sold**.                                       |
| **Europe Sales (EU_Sales)**          | Total sales generated in the European market, measured in **millions of units sold**.                                             |
| **Japan Sales (JP_Sales)**           | Total sales generated in the Japanese market, measured in **millions of units sold**.                                             |
| **Other Region Sales (Other_Sales)** | Total sales generated in all other regions outside North America, Europe, and Japan, measured in **millions of units sold**.      |
| **Global Sales (Global_Sales)**      | The total worldwide sales of the game, calculated as the sum of sales across all regions, measured in **millions of units sold**. |


---

# Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib

---

# Dashboard Features

### KPI Cards

- Total Games
- Total Publishers
- Total Platforms
- Total Global Sales
- North America Sales
- Europe Sales
- Japan Sales
- Other Region Sales

---

### Visualizations

- Year-wise Global Sales Trend
- Top 10 Best Selling Games
- Top Platforms by Sales
- Top Publishers
- Genre Performance
- Regional Sales Comparison
- Regional Market Share (Pie Chart)
- Games Released Per Year
- Top Genres by Number of Games
- Correlation Heatmap

---

### Insights

- Highest Selling Game
- Highest Selling Publisher
- Best Performing Platform
- Best Selling Genre
- Highest Revenue Region

---

### Additional Features

- Interactive Sidebar Filters
- Dataset Preview
- Download Filtered Dataset
- Business Insights
- Business Recommendations


---

# Business Insights

The dashboard helps stakeholders:

- Identify the highest-selling game
- Discover top-performing platforms
- Analyze publisher performance
- Understand regional demand
- Compare genre popularity
- Monitor yearly sales trends

---

# Business Recommendations

- Invest more in high-performing genres.
- Focus marketing campaigns on strong-performing regions.
- Collaborate with successful publishers.
- Continue supporting profitable gaming platforms.
- Use historical trends to plan future game launches.
- Optimize distribution based on regional demand.

---

# How to Run the Project

## 1 Clone the repository

```bash
git clone https://https://github.com/Swetha-manikandan/vid-game
```

---

## 2 Navigate to the project folder

```bash
cd video-game-sales-analysis
```

---

## 3 Install dependencies

```bash
pip install -r requirements.txt
```


---

## 4 Run the Streamlit application

```bash
streamlit run app.py
```

---

# Project Structure

Video-Game-Sales-Analysis/
│
├── app.py
├── video_game_sales_cleaned.csv
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── dashboard_home.png
│   ├── sales_trend.png
│   ├── top_games.png
│   ├── regional_sales.png
│   └── heatmap.png
│
└── assets/

---

# Dashboard Preview

![alt text](<WhatsApp Image 2026-07-02 at 11.26.34 AM.jpeg>)

---

# Future Improvements

- Add Plotly interactive charts
- Machine Learning sales prediction
- Publisher performance forecasting
- Genre recommendation system
- Real-time dashboard updates
- User authentication

---

# Author

**Swetha Manikandan**

Aspiring Data Analyst

Skills:
- Python
- SQL
- Excel
- Power BI
- Streamlit
- Pandas
- Matplotlib
- Data Visualization
- Business Analytics


---

# License

Copyright (c) 2026 Swetha Manikandan

Permission is granted to use, copy, modify, and distribute this project with proper credit to the author.

This project is shared for learning and portfolio purposes only

---

---

# If you like this project

Please consider giving this repository a **Star ⭐** on GitHub.

---