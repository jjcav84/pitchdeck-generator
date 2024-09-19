import matplotlib.pyplot as plt
import numpy as np

def generate_sensitivity_analysis_chart(image_path, financial_data):
    parameters = ['Customer Acquisition Cost', 'Retention Rate', 'Pricing']
    sensitivities = [0.8, 0.6, 0.7]  # Example values, adjust based on your analysis

    plt.figure(figsize=(12, 7))
    plt.barh(parameters, sensitivities)
    plt.xlabel('Sensitivity')
    plt.title('Sensitivity Analysis of Key Parameters')
    plt.xlim(0, 1)

    for i, v in enumerate(sensitivities):
        plt.text(v + 0.01, i, f'{v:.2f}', va='center')

    plt.tight_layout()
    plt.savefig(f'{image_path}/sensitivity_analysis_chart.png', dpi=300, bbox_inches='tight')
    plt.close()