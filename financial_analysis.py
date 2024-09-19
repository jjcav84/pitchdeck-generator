import numpy as np
from tam_sam_som import generate_tam_sam_som_data, generate_tam_sam_som_chart
from financial_projections import generate_financial_projections_chart
from monte_carlo import generate_monte_carlo_chart
from stress_test import generate_stress_testing_chart
from gradient_descent_optimization import generate_optimization_results_chart
from milestones import generate_milestones_chart
from backtesting import generate_backtesting_chart
from scenario_analysis import generate_scenario_analysis_chart
from sensitivity_analysis import generate_sensitivity_analysis_chart
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_input(data, expected_keys):
    for key in expected_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")

def generate_financial_data(tam_sam_som_data):
    financial_data = {}
    years = range(1, 16)  # 15-year projection
    financial_data['years'] = list(years)
    
    initial_som = tam_sam_som_data['SOM']
    growth_rates = [1.5, 1.4, 1.3, 1.25, 1.2] + [1.15] * 5 + [1.1] * 4  # 14 rates for 15 years
    
    revenue_projections = [initial_som]
    for rate in growth_rates:
        revenue_projections.append(revenue_projections[-1] * rate)
    
    financial_data['revenue_projections'] = revenue_projections
    financial_data['ebitda_projections'] = [revenue * 0.15 for revenue in revenue_projections]
    financial_data['npv_projections'] = [revenue / (1.12 ** year) for year, revenue in enumerate(revenue_projections, start=1)]
    financial_data['dcf_projections'] = [ebitda / (1.12 ** year) for year, ebitda in enumerate(financial_data['ebitda_projections'], start=1)]

    financial_data['growth_rates'] = growth_rates

    initial_value = financial_data['revenue_projections'][0]
    final_value = financial_data['revenue_projections'][-1]
    num_years = len(financial_data['years']) - 1
    financial_data['cagr'] = (final_value / initial_value) ** (1 / num_years) - 1

    financial_data['ev_multiples'] = [4, 5, 6, 7, 8]  # Conservative EV/EBITDA multiples

    return financial_data

def generate_stress_test_data(financial_data):
    revenues = financial_data['revenue_projections']
    return {
        'scenarios': ['Economic Downturn', 'Regulatory Changes', 'Increased Competition'],
        'impacts': [-0.2 * revenues[-1], -0.15 * revenues[-1], -0.1 * revenues[-1]],
        'stress_tests': ['Economic Downturn', 'Regulatory Changes', 'Increased Competition']
    }

def generate_scenario_data(financial_data):
    base_revenue = financial_data['revenue_projections'][-1]
    base_cost = base_revenue * 0.7  # Assuming 70% cost
    base_profit = base_revenue * 0.3  # Assuming 30% profit
    return {
        'scenarios': ['Best Case', 'Base Case', 'Worst Case'],
        'revenues': [base_revenue * 1.5, base_revenue, base_revenue * 0.7],
        'costs': [base_cost * 0.8, base_cost, base_cost * 1.2],
        'profits': [base_profit * 2, base_profit, base_profit * 0.4]
    }

def generate_sensitivity_data(financial_data):
    return {
        'parameters': ['Customer Acquisition Cost', 'Churn Rate', 'Conversion Rate', 'Pricing'],
        'base_values': [200, 0.1, 0.05, 1.0],
        'sensitivities': [0.2, 0.05, 0.02, 0.1]
    }

def generate_milestones_data():
    return {
        'milestones': ['Product Launch', 'Market Expansion', 'Series A Funding', 'International Expansion', 'IPO/Unicorn Status'],
        'milestone_years': [1, 2, 3, 5, 7]
    }

def generate_backtesting_data(financial_data):
    actual_values = financial_data['revenue_projections']
    forecasted_values = [val * 1.1 for val in actual_values]  # Slightly overestimate for forecasted values
    return {
        'actual_values': actual_values,
        'forecasted_values': forecasted_values
    }

def calculate_sensitivity_metrics(financial_data):
    financial_data['cac_sensitivity'] = 0.15  # 15% EBITDA impact for 10% CAC change
    financial_data['retention_sensitivity'] = 0.10  # 10% revenue impact for 5% retention rate change
    financial_data['pricing_sensitivity'] = 0.20  # 20% NPV impact for 5% pricing change

def calculate_optimization_results(financial_data):
    financial_data['initial_growth_rate'] = 0.50  # 50% initial growth rate
    financial_data['initial_ev_ebitda'] = 12  # Set a default value
    financial_data['optimized_growth_rate'] = min(2.00, financial_data['initial_growth_rate'] * 1.5)  # Cap at 200%
    financial_data['optimized_ev_ebitda'] = max(8, min(20, financial_data['initial_ev_ebitda'] * 1.2))  # Ensure it's within 8x-20x range
    financial_data['optimization_improvement'] = (financial_data['optimized_growth_rate'] - financial_data['initial_growth_rate']) / financial_data['initial_growth_rate']

def perform_detailed_risk_analysis(financial_data):
    risk_factors = {
        'Market Risk': np.random.normal(0.05, 0.02),
        'Competition Risk': np.random.normal(0.04, 0.015),
        'Regulatory Risk': np.random.normal(0.03, 0.01),
        'Operational Risk': np.random.normal(0.035, 0.015),
        'Technology Risk': np.random.normal(0.025, 0.01)
    }
    
    total_risk = sum(risk_factors.values())
    impact_on_revenue = total_risk * financial_data['revenue_projections'][-1]
    impact_on_ebitda = total_risk * financial_data['ebitda_projections'][-1]
    
    risk_mitigation_strategies = {
        'Market Risk': "Diversify product offerings and expand into new markets",
        'Competition Risk': "Invest in R&D and maintain a strong focus on customer experience",
        'Regulatory Risk': "Maintain compliance team and actively engage with regulators",
        'Operational Risk': "Implement robust processes and invest in employee training",
        'Technology Risk': "Continuous technology upgrades and strong cybersecurity measures"
    }
    
    return {
        'risk_factors': risk_factors,
        'total_risk': total_risk,
        'impact_on_revenue': impact_on_revenue,
        'impact_on_ebitda': impact_on_ebitda,
        'risk_mitigation_strategies': risk_mitigation_strategies
    }

def run_financial_analysis(image_path):
    try:
        tam_sam_som_data = generate_tam_sam_som_data()
        generate_tam_sam_som_chart(tam_sam_som_data, image_path)

        financial_data = generate_financial_data(tam_sam_som_data)
        generate_financial_projections_chart(image_path, financial_data)
        generate_monte_carlo_chart(image_path, financial_data)

        financial_data['stress_test_data'] = generate_stress_test_data(financial_data)
        generate_stress_testing_chart(image_path, financial_data)

        calculate_optimization_results(financial_data)  # Move this line here
        generate_optimization_results_chart(image_path, financial_data)

        financial_data['scenario_data'] = generate_scenario_data(financial_data)
        generate_scenario_analysis_chart(image_path, financial_data)

        financial_data['sensitivity_data'] = generate_sensitivity_data(financial_data)
        generate_sensitivity_analysis_chart(image_path, financial_data)

        financial_data.update(generate_milestones_data())
        generate_milestones_chart(image_path, financial_data)

        financial_data.update(generate_backtesting_data(financial_data))
        generate_backtesting_chart(image_path, financial_data)

        calculate_sensitivity_metrics(financial_data)

        print("\nFinancial Projections:")
        print(f"• Year 5 Projections:")
        print(f"  - EBITDA: ${financial_data['ebitda_projections'][4]:,.2f}")
        print(f"  - Revenue: ${financial_data['revenue_projections'][4]:,.2f}")
        print(f"  - NPV: ${financial_data['npv_projections'][4]:,.2f}")
        print(f"  - Discounted Cash Flow: ${financial_data['dcf_projections'][4]:,.2f}")
        print(f"• 5-Year CAGR: {((financial_data['revenue_projections'][4] / financial_data['revenue_projections'][0]) ** (1/5) - 1) * 100:.2f}%")

        print(f"\n• Year 10 Projections:")
        print(f"  - EBITDA: ${financial_data['ebitda_projections'][9]:,.2f}")
        print(f"  - Revenue: ${financial_data['revenue_projections'][9]:,.2f}")
        print(f"  - NPV: ${financial_data['npv_projections'][9]:,.2f}")
        print(f"  - Discounted Cash Flow: ${financial_data['dcf_projections'][9]:,.2f}")
        print(f"• 10-Year CAGR: {((financial_data['revenue_projections'][9] / financial_data['revenue_projections'][0]) ** (1/10) - 1) * 100:.2f}%")

        print(f"\n• Year 15 Projections:")
        print(f"  - EBITDA: ${financial_data['ebitda_projections'][14]:,.2f}")
        print(f"  - Revenue: ${financial_data['revenue_projections'][14]:,.2f}")
        print(f"  - NPV: ${financial_data['npv_projections'][14]:,.2f}")
        print(f"  - Discounted Cash Flow: ${financial_data['dcf_projections'][14]:,.2f}")
        print(f"• 15-Year CAGR: {financial_data['cagr'] * 100:.2f}%")

        return tam_sam_som_data, financial_data
    except Exception as e:
        logging.error(f"Error in run_financial_analysis: {str(e)}")
        raise
