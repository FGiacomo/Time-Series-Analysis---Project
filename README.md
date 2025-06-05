# 📊 Time Series Analysis Project

This repository contains the full implementation of a **time series analysis** pipeline focused on estimating and validating **Value-at-Risk (VaR)** for a diversified financial portfolio using **GARCH-family models**.

---

## 🔍 Project Overview

The objective is to:
- Construct an equally weighted portfolio consisting of five financial assets (equity index, company stock, currency pair, commodity, and cryptocurrency).
- Estimate volatility using two GARCH-family models: **GARCH(1,1)** and **EGARCH**.
- Compute and compare **annualized conditional standard deviations** and **Value-at-Risk (VaR)** estimates in both in-sample and out-of-sample periods.
- Validate models through rigorous diagnostics and visualize key stylized facts of financial returns.

---

## 🧠 Methodology

The project includes:
- Return computation and data alignment
- Statistical tests for normality, autocorrelation, and ARCH effects
- Automated GARCH model selection pipeline using AIC, Ljung–Box, and LM-ARCH diagnostics
- Volatility modeling and VaR computation using a **rolling forecast approach**
- Comparison of model performance based on empirical coverage of VaR

---

## 📅 Time Frames

- **In-sample period:** 2020-05-01 to 2024-04-30  
- **Out-of-sample period:** 2024-05-01 to 2025-04-30 (365 days)

---

## 👨‍💻 Authors

- **Giacomo Fantato**  
- **Domenico Castaldo**  
- **Federico Mennella**

---

## 📂 Structure

