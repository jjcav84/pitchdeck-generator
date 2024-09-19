import matplotlib.pyplot as plt

def generate_backtesting_chart(image_path, financial_data):
    actual_values = financial_data['actual_values']
    forecasted_values = financial_data['forecasted_values']
    years = financial_data['years'][:len(actual_values)]  # Use all available years

    plt.figure(figsize=(10, 6))
    plt.plot(years, actual_values, label='Actual Values', marker='o')
    plt.plot(years, forecasted_values[:len(actual_values)], label='Forecasted Values', marker='o')
    plt.xlabel('Year')
    plt.ylabel('Amount (USD)')
    plt.title('Backtesting: Actual vs Forecasted Values')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'{image_path}/backtesting_chart.png')
    plt.close()