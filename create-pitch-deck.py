from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Define paths for saving images and PDFs
image_path = './'
pdf_path = './pitch_deck.pdf'
roboto_font_dir = './Roboto/'

# Set up fonts
def add_custom_fonts(pdf):
    regular_font_path = os.path.join(roboto_font_dir, 'Roboto-Regular.ttf')
    bold_font_path = os.path.join(roboto_font_dir, 'Roboto-Bold.ttf')
    italic_font_path = os.path.join(roboto_font_dir, 'Roboto-Italic.ttf')
    
    pdf.add_font('Roboto-Regular', '', regular_font_path, uni=True)
    pdf.add_font('Roboto-Bold', '', bold_font_path, uni=True)
    pdf.add_font('Roboto-Italic', '', italic_font_path, uni=True)

# Generate Charts
def generate_financial_projections_chart():
    years = np.arange(1, 11)
    ebitda_projections = [114000, 159600, 220000, 300000, 380000, 470000, 570000, 680000, 800000, 930000]
    revenue_projections = [500000, 700000, 950000, 1.3e6, 1.7e6, 2.2e6, 2.8e6, 3.5e6, 4.3e6, 5.2e6]
    
    plt.figure(figsize=(10, 6))
    plt.plot(years, ebitda_projections, marker='o', label='EBITDA Projections')
    plt.plot(years, revenue_projections, marker='o', label='Revenue Projections')
    plt.xlabel('Years')
    plt.ylabel('Amount ($)')
    plt.title('Financial Projections')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(image_path, 'financial_projections_chart.png'))
    plt.close()

def generate_monte_carlo_chart():
    np.random.seed(0)
    simulations = 1000
    years = 10
    growth_rates = np.random.normal(loc=0.2, scale=0.1, size=(simulations, years))
    initial_value = 1000000
    final_values = np.zeros(simulations)
    
    for i in range(simulations):
        value = initial_value
        for rate in growth_rates[i]:
            value *= (1 + rate)
        final_values[i] = value
    
    plt.figure(figsize=(10, 6))
    plt.hist(final_values, bins=30, edgecolor='k')
    plt.xlabel('Final Value ($)')
    plt.ylabel('Frequency')
    plt.title('Monte Carlo Simulation of Business Valuation')
    plt.savefig(os.path.join(image_path, 'monte_carlo_chart.png'))
    plt.close()

def generate_scenario_analysis_chart():
    scenarios = ['Best Case', 'Base Case', 'Worst Case']
    revenues = [7e6, 5e6, 3e6]
    costs = [3e6, 2.5e6, 2e6]
    profits = [4e6, 2.5e6, 1e6]
    
    df = pd.DataFrame({'Scenario': scenarios, 'Revenue': revenues, 'Costs': costs, 'Profit': profits})
    df.plot(kind='bar', x='Scenario', stacked=True, figsize=(10, 6))
    plt.title('Scenario Analysis')
    plt.xlabel('Scenario')
    plt.ylabel('Amount ($)')
    plt.savefig(os.path.join(image_path, 'scenario_analysis_chart.png'))
    plt.close()

def generate_sensitivity_analysis_chart():
    parameters = ['Customer Acquisition Cost', 'Churn Rate', 'Conversion Rate']
    base_values = [200, 0.1, 0.05]
    sensitivities = [0.1, 0.05, 0.02]
    
    df = pd.DataFrame({
        'Parameter': parameters,
        'Base Value': base_values,
        'Sensitivity': sensitivities
    })
    df.plot(kind='bar', x='Parameter', figsize=(10, 6))
    plt.title('Sensitivity Analysis')
    plt.xlabel('Parameter')
    plt.ylabel('Impact')
    plt.savefig(os.path.join(image_path, 'sensitivity_analysis_chart.png'))
    plt.close()

def generate_backtesting_chart():
    actual_values = [100000, 120000, 140000, 160000, 180000, 200000, 220000, 240000, 260000, 280000]
    forecasted_values = [95000, 115000, 135000, 155000, 175000, 195000, 215000, 235000, 255000, 275000]
    
    plt.figure(figsize=(10, 6))
    plt.plot(actual_values, label='Actual Values', marker='o')
    plt.plot(forecasted_values, label='Forecasted Values', marker='o')
    plt.xlabel('Time Period')
    plt.ylabel('Amount ($)')
    plt.title('Backtesting: Actual vs Forecasted Values')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(image_path, 'backtesting_chart.png'))
    plt.close()

def generate_stress_testing_chart():
    stress_tests = ['Low Demand', 'High Costs', 'Regulatory Changes']
    impacts = [-0.2, -0.15, -0.1]
    
    plt.figure(figsize=(10, 6))
    plt.bar(stress_tests, impacts, color=['blue', 'orange', 'green'])
    plt.xlabel('Stress Test')
    plt.ylabel('Impact (%)')
    plt.title('Stress Testing Analysis')
    plt.savefig(os.path.join(image_path, 'stress_testing_chart.png'))
    plt.close()

def create_pitch_deck():
    pdf = FPDF()
    add_custom_fonts(pdf)
    
    # Slide 1: Title Slide
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Investor Pitch Deck', ln=True, align='C')
    pdf.set_font('Roboto-Regular', '', 12)
    pdf.cell(0, 10, 'Cosmic Life', ln=True, align='C')
    pdf.cell(0, 10, 'Founder: Vanessa Buchanan', ln=True, align='C')
    pdf.cell(0, 10, 'Website: startcosmic.com', ln=True, align='C')
    
    # Slide 2: Vision and Market Opportunity
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Vision and Market Opportunity', ln=True)
    pdf.set_font('Roboto-Regular', '', 12)
    pdf.multi_cell(0, 10, (
        "• Vision: Become a leading unicorn in the insurtech industry by revolutionizing the way insurance products are delivered and managed.\n"
        "• Market Opportunity: The insurtech sector is rapidly growing with increasing demand for streamlined, customer-centric solutions. By addressing the pain points of traditional insurance processes, the company is well-positioned to capture a significant market share."
    ))

    # Slide 3: Business Model
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Business Model', ln=True)
    pdf.set_font('Roboto-Regular', '', 12)
    pdf.multi_cell(0, 10, (
        "• Core Offering: Provide premium insurance products with real-time quoting capabilities. Ensure a frictionless user experience by avoiding the typical data collection and sales calls.\n"
        "• Customer Experience: Focus on exceptional support and ease of use, which will differentiate the company from competitors and build customer loyalty."
    ))

    # Slide 4: Financial Strategy
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Financial Strategy', ln=True)
    pdf.set_font('Roboto-Regular', '', 12)
    pdf.multi_cell(0, 10, (
        "• Revenue Projections:\n"
        "  • Short-Term: Achieve strong growth in the first few years through aggressive marketing and customer acquisition.\n"
        "  • Long-Term: Reach $1 billion valuation within 10 years by scaling operations, expanding market reach, and optimizing business processes.\n"
        "• Financial Metrics: Highlight key metrics such as EBITDA, NPV, and discounted cash flow."
    ))

    # Slide 5: Financial Projections
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Financial Projections', ln=True)
    pdf.set_font('Roboto-Regular', '', 12)
    generate_financial_projections_chart()
    pdf.image(os.path.join(image_path, 'financial_projections_chart.png'), x=10, y=30, w=190)

    # Slide 6: Monte Carlo Simulation
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Monte Carlo Simulation', ln=True)
    pdf.set_font('Roboto-Regular', '', 12)
    pdf.image(os.path.join(image_path, 'monte_carlo_chart.png'), x=10, y=30, w=190)

    # Slide 7: Scenario Analysis
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Scenario Analysis', ln=True)
    pdf.set_font('Roboto-Regular', '', 12)
    generate_scenario_analysis_chart()
    pdf.image(os.path.join(image_path, 'scenario_analysis_chart.png'), x=10, y=30, w=190)

    # Slide 8: Sensitivity Analysis
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Sensitivity Analysis', ln=True)
    pdf.set_font('Roboto-Regular', '', 12)
    generate_sensitivity_analysis_chart()
    pdf.image(os.path.join(image_path, 'sensitivity_analysis_chart.png'), x=10, y=30, w=190)

    # Slide 9: Backtesting
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Backtesting', ln=True)
    pdf.set_font('Roboto-Regular', '', 12)
    generate_backtesting_chart()
    pdf.image(os.path.join(image_path, 'backtesting_chart.png'), x=10, y=30, w=190)

    # Slide 10: Stress Testing
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Stress Testing', ln=True)
    pdf.set_font('Roboto-Regular', '', 12)
    generate_stress_testing_chart()
    pdf.image(os.path.join(image_path, 'stress_testing_chart.png'), x=10, y=30, w=190)

    # Slide 11: Conclusion and Next Steps
    pdf.add_page()
    pdf.set_font('Roboto-Bold', '', 16)
    pdf.cell(0, 10, 'Conclusion and Next Steps', ln=True)
    pdf.set_font('Roboto-Regular', '', 12)
    pdf.multi_cell(0, 10, (
        "• Summary: With a solid financial foundation, an innovative business model, and a clear path to becoming a unicorn, Cosmic Life is poised to disrupt the insurtech industry.\n"
        "• Next Steps: We are seeking an investment of $1.5 million to accelerate growth and reach our next milestones.\n"
        "• Contact Information: Please reach out for further discussion and detailed financials."
    ))

    # Output the PDF
    pdf.output(pdf_path)
    print(f"PDF created successfully at {pdf_path}")

# Generate all charts
generate_financial_projections_chart()
generate_monte_carlo_chart()
generate_scenario_analysis_chart()
generate_sensitivity_analysis_chart()
generate_backtesting_chart()
generate_stress_testing_chart()

# Create the pitch deck PDF
create_pitch_deck()