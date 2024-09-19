import os
import numpy as np
import matplotlib.pyplot as plt

def generate_financial_projections_chart(image_path, financial_data, chart_style=None):
    years = financial_data['years']
    ebitda_projections = financial_data['ebitda_projections']
    revenue_projections = financial_data['revenue_projections']
    npv_projections = financial_data['npv_projections']
    dcf_projections = financial_data['dcf_projections']
    
    plt.figure(figsize=(12, 8))
    if chart_style:
        plt.style.use(chart_style)
    else:
        plt.style.use('default')

    plt.plot(years, ebitda_projections, marker='o', label='EBITDA Projections', linewidth=2)
    plt.plot(years, revenue_projections, marker='s', label='Revenue Projections', linewidth=2)
    plt.plot(years, npv_projections, marker='^', label='NPV Projections', linewidth=2)
    plt.plot(years, dcf_projections, marker='D', label='DCF Projections', linewidth=2)
    
    plt.xlabel('Years', fontsize=12)
    plt.ylabel('Amount ($)', fontsize=12)
    plt.title('Financial Projections: EBITDA, Revenue, NPV, and DCF', fontsize=16)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    
    chart_path = os.path.join(image_path, 'financial_projections_chart.png')
    plt.savefig(chart_path, dpi=300)
    plt.close()
    print(f"Financial Projections chart saved at {chart_path}")