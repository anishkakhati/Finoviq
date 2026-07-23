# Finoviq AI

> **An End-to-End AI-Powered Intelligent Investment Platform**

Finoviq AI is a production-ready AI investment platform that combines **Machine Learning, Data Engineering, Trading Intelligence, and Explainable AI** to analyze financial markets, forecast stock prices, manage risk, and generate intelligent investment recommendations.

Unlike traditional stock prediction projects, **Finoviq AI separates prediction from decision-making** by combining machine learning with a modular trading engine that recommends **BUY, HOLD, or SELL** actions based on technical indicators, risk management, and expected returns.

---

# Features

## Data Engineering

- Historical stock data collection using Yahoo Finance API
- Automated ETL Pipeline
- PostgreSQL Database Integration
- Data Validation Pipeline
- Data Cleaning & Preprocessing
- Multi-company Data Pipeline

---

## Feature Engineering

### Price Features

- Daily Return
- Price Range
- Candle Size
- Volatility

### Technical Indicators

- SMA (5, 10, 20, 50, 200)
- EMA (12, 26)
- RSI (14)
- MACD
- Bollinger Bands
- ATR
- OBV
- VWAP

### Time-Series Features

- Close Price Lag Features
- Volume Lag Features
- Open Lag
- High Lag
- Low Lag

### Rolling Statistics

- Rolling Mean
- Rolling Max
- Rolling Min
- Rolling Median
- Rolling Standard Deviation

---

# Machine Learning

### Multi-Output Stock Prediction

Predicts next-day:

- Open Price
- High Price
- Low Price
- Close Price

### Current Model

- Multi-Output Linear Regression

### Planned Models

- Random Forest
- XGBoost
- LightGBM
- CatBoost
- LSTM
- GRU
- Transformer

---

# AI Trading Intelligence Engine

Finoviq AI transforms price predictions into actionable investment decisions.

### Trading Modules

- Entry Strategy
- Exit Strategy
- ATR-based Stop Loss
- Risk-Reward Take Profit
- Expected Profit Calculator
- Expected Loss Calculator
- ROI Calculator
- Confidence Score Engine
- BUY / HOLD / SELL Recommendation Engine

---

# FastAPI Backend

REST APIs currently available:

## Prediction API

```http
POST /prediction/predict
```

Predicts next-day OHLC prices.

---

## Recommendation API

```http
POST /recommendation/recommend
```

Returns:

- OHLC Prediction
- Entry Price
- Exit Price
- Stop Loss
- Take Profit
- Expected Profit
- Expected Loss
- ROI
- Confidence Score
- BUY / HOLD / SELL Recommendation


---

# Project Structure

```text
Finoviq/

├── backend/
│
├── api/
│   ├── prediction.py
│   └── recommendation.py
│
├── database/
│   ├── db.py
│   ├── save_prediction.py
│   └── save_recommendation.py
│
├── feature_engineering/
│
├── models/
│   ├── train.py
│   ├── predict.py
│   └── prediction_report.py
│
├── trading/
│   ├── strategy.py
│   ├── entry_strategy.py
│   ├── exit_strategy.py
│   ├── stop_loss.py
│   ├── take_profit.py
│   ├── confidence.py
│   ├── profit_calculator.py
│   └── recommendation.py
│
├── data_pipeline/
│
├── saved_models/
│
├── config/
│
├── docs/
│
├── README.md
└── requirements.txt
```

---

# Tech Stack

## Programming Language

- Python

## Database

- PostgreSQL
- psycopg2

## Data Engineering

- Pandas
- NumPy
- yfinance

## Machine Learning

- Scikit-learn

## Backend

- FastAPI
- Pydantic

## Visualization

- Matplotlib
- Plotly

---

# Current Progress

## Completed

- Project Setup
- PostgreSQL Database
- ETL Pipeline
- Data Validation
- Data Cleaning
- Feature Engineering
- Technical Indicators
- Lag Features
- Rolling Statistics
- Multi-Output ML Model
- Model Training Pipeline
- Prediction API
- AI Trading Intelligence Engine
- Recommendation API
- PostgreSQL Prediction Storage
- PostgreSQL Recommendation Storage

---

## In Progress

- Hyperparameter Optimization
- Multiple ML Models
- Model Comparison
- Explainable AI (SHAP)
- Explainable AI (LIME)

---

## Planned

- LSTM
- GRU
- Transformer
- Reinforcement Learning Trading Agent
- Portfolio Optimization
- Risk Analysis
- News Sentiment Analysis
- Backtesting Engine
- React Dashboard
- Docker Deployment
- Cloud Deployment

---

# Project Goal

Finoviq AI aims to become a complete AI-powered investment platform capable of:

- Predicting stock prices
- Generating investment recommendations
- Managing investment risk
- Calculating expected returns
- Optimizing portfolios
- Providing explainable AI insights
- Learning continuously through Reinforcement Learning

---

# Author

**Anishka Khati**

B.Tech Computer Science & Engineering (Artificial Intelligence & Machine Learning)

Building **Finoviq AI** as a production-ready AI investment platform integrating **Data Engineering, Machine Learning, Trading Intelligence, Reinforcement Learning, and Explainable AI**.

---

If you found this project interesting, consider giving it a star.