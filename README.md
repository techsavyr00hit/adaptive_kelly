# Adaptive Kelly

A Python project exploring the Kelly Criterion through Monte Carlo simulation.

The goal of this project is to understand how different versions of the Kelly Criterion perform when the true probability of winning is unknown. Instead of jumping directly into advanced financial models, this project builds the ideas step by step using probability, optimization, statistics, and simulation.

---

## Project Overview

The project compares three betting strategies.

### 1. Classical Kelly

Assumes the true probability of winning is already known.

\[
f^*=\frac{bp-q}{b}
\]

For even odds,

\[
f^*=2p-1
\]

This represents the theoretical optimal betting fraction.

---

### 2. Estimated Kelly

In reality, the true probability is usually unknown.

Estimated Kelly calculates the probability from previous coin tosses.

\[
\hat p=\frac{\text{Heads}}{\text{Heads}+\text{Tails}}
\]

The Kelly fraction is recalculated after every toss using the latest estimate.

---

### 3. Adaptive Kelly

Estimated probabilities often fluctuate because of randomness.

Adaptive Kelly smooths these fluctuations using an Exponential Moving Average (EMA).

\[
p_t=\alpha\hat p_t+(1-\alpha)p_{t-1}
\]

where

- \(p_t\) = updated probability estimate
- \(\hat p_t\) = current estimate
- \(p_{t-1}\) = previous estimate
- \(\alpha\) = learning rate

The smoothed probability is then used to calculate the Kelly fraction.

---

## Monte Carlo Simulation

Each experiment consists of

- 1000 biased coin tosses
- Initial wealth of \$1000
- Even betting odds
- 1000 independent simulations

To ensure a fair comparison, every strategy receives the **same sequence of coin tosses** during each simulation.

---

## Performance Metrics

For every strategy the project measures

- Average Final Wealth
- Median Final Wealth
- Standard Deviation
- Maximum Wealth
- Minimum Wealth

---

## Visualizations

The project generates several plots for comparison.

### Average Final Wealth

Compares the average performance of each strategy.

### Wealth Distribution

Overlapping histograms showing the distribution of final wealth across simulations.

### Wealth Paths

Shows how wealth evolves over time for a representative simulation.

### Box Plot

Compares

- Median
- Spread
- Outliers
- Overall variability

between the three strategies.

---

## Mathematical Concepts

This project uses concepts from undergraduate Computer Science and Mathematics.

- Calculus
- Probability Theory
- Bernoulli Trials
- Expected Value
- Statistical Estimation
- Monte Carlo Simulation
- Optimization
- Recurrence Relations

---

## Repository Structure

```
adaptive-kelly/
│
├── kelly.py
├── simul.py
├── README.md
└── results/
```

---

## Future Work

Future versions of this project may include

- Bayesian Kelly
- Fractional Kelly
- Dynamic Probability Drift
- Risk-adjusted Kelly
- Multi-asset Kelly
- Real Market Data
- Reinforcement Learning based Kelly

---

## Purpose

This repository is a personal learning project created to understand the mathematics behind the Kelly Criterion and how different probability estimation techniques influence long-term wealth growth through simulation.
