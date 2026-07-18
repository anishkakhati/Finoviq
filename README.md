#  Finoviq AI

> **An End-to-End AI-Powered Intelligent Investment Platform**

Finoviq AI is an intelligent investment platform that leverages **Machine Learning, Deep Learning, Reinforcement Learning, and Explainable AI (XAI)** to analyze financial markets, predict stock prices, optimize investment portfolios, assess risk, and provide transparent, data-driven investment recommendations.

The project is being built as a production-ready AI system with a modular architecture, automated data pipelines, and scalable machine learning workflows.

---

#  Features

##  Data Engineering

- Historical stock data collection using Yahoo Finance API
- Automated ETL (Extract, Transform, Load) Pipeline
- PostgreSQL Database Integration
- Automated Data Validation
- Data Cleaning & Preprocessing Pipeline
- Multi-company Data Pipeline

---

## Feature Engineering

### Price-Based Features

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
- ATR (Average True Range)
- OBV (On Balance Volume)
- VWAP (Volume Weighted Average Price)

### Time-Series Features

- Close Price Lags
- Volume Lags
- Open Price Lag
- High Price Lag
- Low Price Lag

### Rolling Statistics

- Rolling Mean
- Rolling Maximum
- Rolling Minimum
- Rolling Standard Deviation
- Rolling Median

---

##  Upcoming Features

- Stock Price Prediction
- Multi-Step Forecasting
- Risk Analysis
- Portfolio Optimization
- Reinforcement Learning Agent
- Explainable AI (SHAP & LIME)
- FastAPI Backend
- React Dashboard
- Real-Time Stock Data
- Docker Deployment
- Cloud Deployment

---

#  Project Structure

```text
Finoviq/

├── backend/
│
├── api/
│
├── data_pipeline/
│ ├── extract.py
│ ├── transform.py
│ ├── validate.py
│ └── load.py
│
├── database/
│ └── db.py
│
├── feature_engineering/
│ ├── preprocessing.py
│ ├── indicators.py
│ ├── lag_features.py
│ └── scaling.py
│
├── models/
├── routes/
├── services/
│
├── config/
│ ├── init.py
│ └── settings.py
│
├── data/
│ ├── raw/
│ └── processed/
│
├── docs/
├── utils/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

#  Database

Current PostgreSQL Tables

- companies
- stock_prices
- processed_stock_data
- predictions
- recommendations
- news

---

#  Machine Learning Dataset

The processed dataset contains

## Raw Features

- Open
- High
- Low
- Close
- Adj Close
- Volume

## Engineered Features

- Daily Return
- Price Range
- Candle Size
- Volatility

## Technical Indicators

- SMA
- EMA
- RSI
- MACD
- Bollinger Bands
- ATR
- OBV
- VWAP

## Time-Series Features

- Close Lag Features
- Volume Lag Features
- Open Lag
- High Lag
- Low Lag

## Rolling Features

- Rolling Mean
- Rolling Maximum
- Rolling Minimum
- Rolling Standard Deviation
- Rolling Median

These features will serve as the primary input for the Machine Learning models.

---

#  Tech Stack

## Programming Language

- Python

## Database

- PostgreSQL
- psycopg2
- SQLAlchemy

## Data Engineering

- Pandas
- NumPy
- Yahoo Finance (yfinance)

## Machine Learning (Upcoming)

- Scikit-learn
- XGBoost
- TensorFlow
- PyTorch

## Backend (Upcoming)

- FastAPI

## Frontend (Upcoming)

- React.js
- Tailwind CSS

## Visualization (Upcoming)

- Plotly
- Matplotlib

---


#  Roadmap

- [x] Project Setup
- [x] GitHub Repository
- [x] PostgreSQL Database
- [x] Database Design
- [x] ETL Pipeline
- [x] Data Validation
- [x] Data Cleaning
- [x] Feature Engineering
- [x] Technical Indicators
- [x] Lag Features
- [x] Rolling Statistics
- [x] Processed Dataset Generation
- [ ] Machine Learning Dataset Builder
- [ ] Stock Price Prediction Models
- [ ] Hyperparameter Optimization
- [ ] Deep Learning Models (LSTM / GRU / Transformer)
- [ ] Reinforcement Learning Trading Agent
- [ ] Portfolio Optimization
- [ ] Risk Analysis
- [ ] Explainable AI (SHAP & LIME)
- [ ] FastAPI Backend
- [ ] React Dashboard
- [ ] Docker Support
- [ ] Cloud Deployment

---

# Project Goal

The objective of Finoviq AI is to develop a complete AI-driven investment platform capable of:

- Predicting future stock prices
- Generating buy/sell recommendations
- Assessing investment risk
- Optimizing portfolios
- Providing explainable investment insights
- Continuously improving trading strategies using Reinforcement Learning

---

#  Author

**Anishka Khati**

B.Tech Computer Science & Engineering (Artificial Intelligence & Machine Learning)

Building **Finoviq AI** as an end-to-end intelligent investment platform integrating Data Engineering, Machine Learning, Deep Learning, Reinforcement Learning, and Explainable AI.

---