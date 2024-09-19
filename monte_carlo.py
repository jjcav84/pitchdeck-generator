import numpy as np
import matplotlib.pyplot as plt

def generate_monte_carlo_chart(image_path, financial_data):
    num_simulations = 1000
    num_years = 10
    initial_revenue = financial_data['revenue_projections'][0]
    growth_rate = 0.25  # Reduced to keep it under 200% per year
    volatility = 0.15  # Adjusted for more realistic scenarios

    simulations = np.zeros((num_simulations, num_years))
    for i in range(num_simulations):
        revenue = initial_revenue
        for j in range(num_years):
            growth = min(np.random.normal(growth_rate, volatility), 2.0)  # Cap growth at 200%
            revenue *= (1 + growth)
            simulations[i, j] = revenue

    unicorn_threshold = 1e9  # $1 billion
    unicorn_years = np.argmax(simulations >= unicorn_threshold, axis=1)
    unicorn_years = np.where(unicorn_years == 0, num_years, unicorn_years)
    unicorn_probability = np.sum(unicorn_years < num_years) / num_simulations
    avg_unicorn_year = np.mean(unicorn_years) + 1

    plt.figure(figsize=(10, 6))
    plt.plot(range(1, num_years + 1), simulations.T, alpha=0.1, color='blue')
    plt.axhline(y=unicorn_threshold, color='r', linestyle='--', label='Unicorn Threshold')
    plt.title('Monte Carlo Simulation of Revenue Growth')
    plt.xlabel('Years')
    plt.ylabel('Revenue ($)')
    plt.legend()
    plt.savefig(f'{image_path}/monte_carlo_chart.png')
    plt.close()

    return unicorn_probability, avg_unicorn_year, f'{image_path}/monte_carlo_chart.png'
