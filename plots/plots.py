import os
import matplotlib.pyplot as plt

# Data for each category
categories = ['Ce', 'Ba', 'No', 'Va']

# Data points
time_points = ['It1', 'It2', 'It3', 'It4']
ce_data = {
    'WAR': [87, 90, 92, 93],
    'PAR': [96.2, 96.5, 98.4, 98.7],
    'PER*': [99.0, 99.2, 99.2, 99.2],
    'Levenshtein Ratios': [0.9881, 0.9904, 0.9911, 0.9924],
    'Levenshtein Ratios (excl. dist 1)': [0.8991, 0.9974, 0.9973, 0.9977]
}

ba_data = {
    'WAR': [82, 86, 88, 90],
    'PAR': [96.4, 96.6, 98.8, 99.0],
    'PER*': [99.1, 99.4, 99.2, 99.3],
    'Levenshtein Ratios': [0.9909, 0.9909, 0.9939, 0.9950],
    'Levenshtein Ratios (excl. dist 1)': [0.9980, 0.9091, 0.9002, 0.9022]
}

no_data = {
    'WAR': [75, 83, 92, 93],
    'PAR': [93.8, 94.8, 98.5, 98.6],
    'PER*': [98.4, 99.0, 98.9, 99.9],
    'Levenshtein Ratios': [0.9859, 0.9913, 0.9924, 0.9930],
    'Levenshtein Ratios (excl. dist 1)': [0.9062, 0.9038, 0.9013, 0.8980]
}

va_data = {
    'WAR': [85, 87, 92, 94],
    'PAR': [94.7, 95.2, 95.8, 98.8],
    'PER*': [98.6, 99.0, 98.9, 99.1],
    'Levenshtein Ratios': [0.9874, 0.9910, 0.9928, 0.9940],
    'Levenshtein Ratios (excl. dist 1)': [0.9085, 0.9086, 0.9030, 0.8985]
}

# Combine all data
all_data = {
    'Ce': ce_data,
    'Ba': ba_data,
    'No': no_data,
    'Va': va_data
}

# Create a folder to save the plots
output_folder = 'plots'
os.makedirs(output_folder, exist_ok=True)

# Function to plot the data and save as PNG
def plot_evolution(category, measure, data):
    plt.figure(figsize=(10, 6))
    
    plt.plot(time_points, data, label=measure)
    
    plt.title(f'Evolution of {measure} for {category}', fontsize=16)
    plt.xlabel('Iterations', fontsize=14)
    plt.ylabel(f'{measure}', fontsize=14)
    plt.legend()
    plt.grid(True)
    
    # Adjusting tick parameters
    plt.tick_params(axis='both', which='major', labelsize=12)
    
    # Save the plot as a PNG file
    plt.savefig(os.path.join(output_folder, f'{category}_{measure}.png'))
    plt.close()

# Function to plot combined data for each measure across categories
def plot_combined_measures(measure, combined_data):
    plt.figure(figsize=(10, 6))
    
    for category, values in combined_data.items():
        plt.plot(time_points, values, label=category)
    
    plt.title(f'Evolution of {measure} across iterations', fontsize=16)
    plt.xlabel('Iterations', fontsize=14)
    plt.ylabel(f'{measure}', fontsize=14)
    plt.legend()
    plt.grid(True)
    
    # Adjusting tick parameters
    plt.tick_params(axis='both', which='major', labelsize=12)
    
    # Save the combined plot as a PNG file
    plt.savefig(os.path.join(output_folder, f'Combined_{measure}.png'))
    plt.close()

# Plotting the data for each category and each measure, and saving the plots
combined_measures_data = {measure: {} for measure in ce_data.keys()}

for category, data in all_data.items():
    for measure, values in data.items():
        plot_evolution(category, measure, values)
        combined_measures_data[measure][category] = values

# Plotting combined measures across all categories
for measure, combined_data in combined_measures_data.items():
    plot_combined_measures(measure, combined_data)
