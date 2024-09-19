import matplotlib.pyplot as plt
import numpy as np

def generate_competitive_landscape_chart(image_path):
    companies = ['Cosmic Life', 'Traditional Insurers', 'Insurtech Startups']
    innovation = [9, 3, 7]
    customer_experience = [9, 4, 8]
    product_range = [8, 9, 5]

    x = np.arange(len(companies))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))
    rects1 = ax.bar(x - width, innovation, width, label='Innovation')
    rects2 = ax.bar(x, customer_experience, width, label='Customer Experience')
    rects3 = ax.bar(x + width, product_range, width, label='Product Range')

    ax.set_ylabel('Score')
    ax.set_title('Competitive Landscape')
    ax.set_xticks(x)
    ax.set_xticklabels(companies)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3) # this is the customer experience bar
    ax.bar_label(rects3, padding=3)

    fig.tight_layout()

    plt.savefig(f'{image_path}/competitive_landscape_chart.png')
    plt.close()

def generate_optimization_results_chart(image_path, financial_data):
    metrics = ['Growth Rate', 'EV/EBITDA Multiple']
    before = [financial_data['initial_growth_rate'], financial_data['initial_ev_ebitda']]
    after = [financial_data['optimized_growth_rate'], financial_data['optimized_ev_ebitda']]

    x = np.arange(len(metrics))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    rects1 = ax.bar(x - width/2, before, width, label='Before Optimization')
    rects2 = ax.bar(x + width/2, after, width, label='After Optimization')

    ax.set_ylabel('Value')
    ax.set_title('Optimization Results')
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.savefig(f'{image_path}/optimization_results_chart.png')
    plt.close()

def generate_competitive_quadrant_chart(image_path):
    companies = ['Cosmic Life', 'Traditional Insurer A', 'Traditional Insurer B', 'Insurtech Startup X', 'Insurtech Startup Y']
    x = [0.8, 0.2, 0.3, 0.6, 0.7]  # Technology Innovation
    y = [0.6, 0.8, 0.7, 0.3, 0.2]  # Market Share

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.scatter(x, y, s=200)

    for i, company in enumerate(companies):
        ax.annotate(company, (x[i], y[i]), xytext=(5, 5), textcoords='offset points')

    ax.axvline(x=0.5, color='gray', linestyle='--')
    ax.axhline(y=0.5, color='gray', linestyle='--')

    ax.text(0.25, 0.75, 'Market Leaders\n(Low Innovation)', ha='center', va='center', fontsize=10)
    ax.text(0.75, 0.75, 'Ideal Position\n(High Innovation, High Market Share)', ha='center', va='center', fontsize=10)
    ax.text(0.25, 0.25, 'Laggards', ha='center', va='center', fontsize=10)
    ax.text(0.75, 0.25, 'Innovators\n(Low Market Share)', ha='center', va='center', fontsize=10)

    ax.set_xlabel('Technology Innovation')
    ax.set_ylabel('Market Share')
    ax.set_title('Competitive Analysis Quadrant')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    plt.savefig(f'{image_path}/competitive_quadrant_chart.png', dpi=300, bbox_inches='tight')
    plt.close()
