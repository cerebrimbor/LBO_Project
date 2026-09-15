import numpy as np


def simulate_ou_step(
    current_value,
    kappa,
    long_run_mean,
    sigma,
    rng,
    dt=1.0
):
    mean = (current_value * np.exp(-kappa * dt)+ long_run_mean * (1 - np.exp(-kappa * dt)))

    variance = (sigma**2 / (2 * kappa)* (1 - np.exp(-2 * kappa * dt)))

    standard_deviation = np.sqrt(variance)

    next_value = rng.normal(
        loc=mean,
        scale=standard_deviation
    )

    return max(next_value, 0.5)