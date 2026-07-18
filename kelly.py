
def classical(probability, odds=1):

    #Classical Kelly using the true probability.

    q = 1 - probability
    fraction = (odds * probability - q) / odds

    return max(0.0, fraction)


def estimated(heads, tails, odds=1):

    #Estimated Kelly using the estimated probability.

    total = heads + tails

    if total == 0:
        return 0.0

    probability = heads / total

    return classical(probability, odds)


def adaptive(heads, tails, previous_probability,alpha=0.10, odds=1):

    #Adaptive Kelly using Exponential Moving Average.

    total = heads + tails

    if total == 0:
        return 0.0, previous_probability

    estimate = heads / total

    probability = (
        alpha * estimate +
        (1 - alpha) * previous_probability
    )

    fraction = classical(probability, odds)

    return fraction, probability
