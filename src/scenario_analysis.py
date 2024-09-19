import matplotlib.pyplot as plt
import pandas as pd

def generate_scenario_analysis_chart(image_path, financial_data):
    scenarios = financial_data['scenario_data']['scenarios']
    revenues = financial_data['scenario_data']['revenues']
    costs = financial_data['scenario_data']['costs']
    profits = financial_data['scenario_data']['profits']

    df = pd.DataFrame({
        'Scenario': scenarios,
        'Revenue': revenues,
        'Costs': costs,
        'Profit': profits
    })

    ax = df.plot(kind='bar', x='Scenario', stacked=True, figsize=(10, 6), color=['blue', 'orange', 'green'])
    ax.set_title('Scenario Analysis')
    ax.set_xlabel('Scenario')
    ax.set_ylabel('Amount ($)')
    plt.grid(True)

    plt.savefig(f'{image_path}/scenario_analysis_chart.png')
    plt.close()