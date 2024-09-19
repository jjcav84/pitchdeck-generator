import matplotlib.pyplot as plt

def generate_milestones_chart(image_path, financial_data):
    milestones = financial_data['milestones']
    years = financial_data['milestone_years']

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(years, milestones, marker='o', linestyle='-', color='blue')
    
    ax.set_title('Key Milestones Over the Next 5 Years')
    ax.set_xlabel('Year')
    ax.set_ylabel('Milestone')
    ax.grid(True)

    plt.savefig(f'{image_path}/milestones_chart.png')
    plt.close()