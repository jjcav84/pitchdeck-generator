import matplotlib.pyplot as plt

def generate_tam_sam_som_data():
    tam = 100000000000  # Total Addressable Market: $100 billion (global insurance market)
    sam = tam * 0.05    # Serviceable Available Market: 5% of TAM (specific insurance segments)
    som = sam * 0.02    # Serviceable Obtainable Market: 2% of SAM (realistic market capture)
    
    return {
        'TAM': tam,
        'SAM': sam,
        'SOM': som
    }

def generate_tam_sam_som_chart(tam_sam_som_data, image_path):
    sizes = list(tam_sam_som_data.values())
    labels = list(tam_sam_som_data.keys())

    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title('TAM, SAM, SOM Analysis')
    plt.savefig(f'{image_path}/tam_sam_som_chart.png')
    plt.close()