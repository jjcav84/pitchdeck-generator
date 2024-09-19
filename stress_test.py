import matplotlib.pyplot as plt

def generate_stress_testing_chart(image_path, financial_data):
    stress_tests = financial_data['stress_test_data']['scenarios']
    impacts = financial_data['stress_test_data']['impacts']

    plt.figure(figsize=(10, 6))
    plt.bar(stress_tests, impacts, color=['blue', 'orange', 'green'])
    plt.xlabel('Stress Test')
    plt.ylabel('Impact on Profitability (%)')
    plt.title('Stress Testing Analysis')
    plt.savefig(f'{image_path}/stress_testing_chart.png')
    plt.close()
