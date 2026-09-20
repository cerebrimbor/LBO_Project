# Stochastic LBO Model

A Python-based **stochastic Leveraged Buyout (LBO) model** that evaluates investment returns under uncertain economic conditions.

## Overview

Instead of using a single deterministic scenario, the model simulates changing economic regimes and valuation multiples, then evaluates their impact on LBO returns.

### Model Pipeline

Markov Economic Regimes  
→ OU Valuation Multiples  
→ Operating Forecast  
→ Debt Schedule  
→ Exit Valuation  
→ MOIC / IRR  
→ Monte Carlo Risk Analysis

## Features

- Markov regime-switching: Expansion, Normal, Slowdown, Recession
- Ornstein–Uhlenbeck stochastic valuation multiples
- Revenue and EBITDA forecasting
- Debt repayment based on free cash flow
- LBO exit valuation and sponsor returns
- MOIC and IRR calculation
- Monte Carlo simulation with downside-risk analysis
- Visualization of return distributions and stochastic paths

## Tech Stack

- Python
- NumPy
- Matplotlib
- Monte Carlo Simulation
- Markov Chains
- Ornstein–Uhlenbeck Process

## Run

```bash
pip install numpy matplotlib
python main.py
