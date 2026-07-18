import random
import statistics
from typing import List
import matplotlib.pyplot as plt
import kelly

# PARAMETERS

INITIAL_WEALTH = 1000
NUM_TOSSES = 1000
NUM_SIMULATIONS = 1000

TRUE_PROBABILITY = 0.60
ODDS = 1

def generate_coin_tosses():

    tosses = []

    for _ in range(NUM_TOSSES):

        if random.random() < TRUE_PROBABILITY:
            tosses.append(True)      # Heads

        else:
            tosses.append(False)     # Tails

    return tosses

def simulate(strategy,tosses):

    wealth = INITIAL_WEALTH

    heads = 0
    tails = 0

    estimate = 0.50

    wealth_history: List[float] = [wealth]

    for toss in range(NUM_TOSSES):

        # Kelly Strategy

        if strategy == "classical":

            fraction = kelly.classical(
                TRUE_PROBABILITY,
                ODDS
            )

        elif strategy == "estimated":

            fraction = kelly.estimated(
                heads,
                tails,
                ODDS
            )

        elif strategy == "adaptive":

            fraction, estimate = kelly.adaptive(
                heads,
                tails,
                estimate,
                odds=ODDS
            )

        else:
            raise ValueError("Unknown Strategy")

        bet = wealth * fraction

        # Coin Toss

        if tosses[toss]:

            wealth += bet
            heads += 1

        else:

            wealth -= bet
            tails += 1

        wealth_history.append(wealth)

    return wealth, wealth_history


# RUN ALL STRATEGIES

classical_results = []
estimated_results = []
adaptive_results = []

classical_path = []
estimated_path = []
adaptive_path = []

for simulation in range(NUM_SIMULATIONS):

    tosses = generate_coin_tosses()

    result, path = simulate("classical", tosses)
    classical_results.append(result)

    if simulation == 0:
        classical_path = path

    result, path = simulate("estimated", tosses)
    estimated_results.append(result)

    if simulation == 0:
        estimated_path = path

    result, path = simulate("adaptive", tosses)
    adaptive_results.append(result)

    if simulation == 0:
        adaptive_path = path


# PRINT RESULTS

def print_results(name, results):

    print(f"\n{name}")

    print("-" * len(name))

    print(f"Average : {statistics.mean(results):,.2f}")
    print(f"Median  : {statistics.median(results):,.2f}")
    print(f"Std Dev : {statistics.stdev(results):,.2f}")
    print(f"Best    : {max(results):,.2f}")
    print(f"Worst   : {min(results):,.2f}")


print_results("Classical Kelly", classical_results)

print_results("Estimated Kelly", estimated_results)

print_results("Adaptive Kelly", adaptive_results)

# Average Wealth Comparison

plt.figure(figsize=(7,5))

averages = [

    statistics.mean(classical_results),
    statistics.mean(estimated_results),
    statistics.mean(adaptive_results)

]

labels = [

    "Classical",
    "Estimated",
    "Adaptive"

]

plt.bar(labels, averages)

plt.title("Average Final Wealth")

plt.ylabel("Wealth")

plt.grid(axis="y")

plt.show()

# Histogram

plt.figure(figsize=(10,6))

plt.hist(classical_results,
         bins=40,
         alpha=0.5,
         label="Classical")

plt.hist(estimated_results,
         bins=40,
         alpha=0.5,
         label="Estimated")

plt.hist(adaptive_results,
         bins=40,
         alpha=0.5,
         label="Adaptive")

plt.title("Distribution of Final Wealth")

plt.xlabel("Final Wealth")

plt.ylabel("Frequency")

plt.legend()

plt.grid(True)

plt.show()

# Wealth Paths

plt.figure(figsize=(10,6))

plt.plot(classical_path,
         label="Classical")

plt.plot(estimated_path,
         label="Estimated")

plt.plot(adaptive_path,
         label="Adaptive")

plt.title("Sample Wealth Path")

plt.xlabel("Coin Toss")

plt.ylabel("Wealth")

plt.legend()

plt.grid(True)

plt.show()

# Box Plot

plt.figure(figsize=(8,6))

plt.boxplot([

    classical_results,
    estimated_results,
    adaptive_results

],
labels=[

    "Classical",
    "Estimated",
    "Adaptive"

])

plt.title("Final Wealth Comparison")

plt.ylabel("Final Wealth")

plt.grid(True)

plt.show()
