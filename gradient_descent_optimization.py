import matplotlib.pyplot as plt
import numpy as np

def objective_function(growth_rate, ev_multiple):
    # This function represents our business model
    # You can modify this to better reflect your specific business metrics
    return growth_rate * ev_multiple - 0.5 * (growth_rate**2 + ev_multiple**2)

def sgd_with_momentum(initial_growth_rate, initial_ev_multiple, learning_rate, momentum, num_iterations):
    growth_rate = initial_growth_rate
    ev_multiple = initial_ev_multiple
    velocity_growth = 0
    velocity_ev = 0
    history = []

    for _ in range(num_iterations):
        # Calculate gradients
        grad_growth = ev_multiple - growth_rate
        grad_ev = growth_rate - ev_multiple

        # Update velocities
        velocity_growth = momentum * velocity_growth + learning_rate * grad_growth
        velocity_ev = momentum * velocity_ev + learning_rate * grad_ev

        # Update parameters
        growth_rate += velocity_growth
        ev_multiple += velocity_ev

        # Store current state
        history.append((growth_rate, ev_multiple, objective_function(growth_rate, ev_multiple)))

    return history

def backtracking_line_search(growth_rate, ev_multiple, direction, alpha=0.5, beta=0.8):
    t = 1.0
    while objective_function(growth_rate + t * direction[0], ev_multiple + t * direction[1]) < \
          objective_function(growth_rate, ev_multiple) + alpha * t * np.dot(direction, [ev_multiple - growth_rate, growth_rate - ev_multiple]):
        t *= beta
    return t

def generate_optimization_results_chart(image_path, financial_data):
    initial_growth_rate = financial_data['initial_growth_rate']
    initial_ev_multiple = financial_data['initial_ev_ebitda']
    
    # Run SGD with momentum
    history = sgd_with_momentum(initial_growth_rate, initial_ev_multiple, learning_rate=0.01, momentum=0.9, num_iterations=100)

    # Extract results
    growth_rates, ev_multiples, objective_values = zip(*history)

    # Plot results
    plt.figure(figsize=(12, 8))
    plt.subplot(2, 1, 1)
    plt.plot(growth_rates, ev_multiples, marker='o', linestyle='-')
    plt.title('Optimization Path: Growth Rates vs EV Multiples')
    plt.xlabel('Growth Rate')
    plt.ylabel('EV/EBITDA Multiple')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(range(len(objective_values)), objective_values)
    plt.title('Objective Function Value Over Iterations')
    plt.xlabel('Iteration')
    plt.ylabel('Objective Value')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig(f'{image_path}/optimization_results_chart.png')
    plt.close()

    # Update financial_data with optimized values, capping growth rate at 200%
    financial_data['optimized_growth_rate'] = min(2.00, growth_rates[-1])
    financial_data['optimized_ev_ebitda'] = max(8, min(20, ev_multiples[-1]))
    financial_data['optimization_improvement'] = (financial_data['optimized_growth_rate'] - financial_data['initial_growth_rate']) / financial_data['initial_growth_rate']

    return financial_data