import pandas as pd
import matplotlib.pyplot as plt

# Data for the tables NO, VA, CE, and Ba
data_no = {
    'Label': ['1a', '2a', '3a', '4a'],
    '1': [10.07884171, 6.159638868, 4.697218697, 4.545359988],
    '2': [0.954837636, 0.526304841, 0.470137921, 0.472218177],
    '3': [0.16225999, 0.05616692, 0.043685382, 0.035364357],
    '4': [0.01664205, 0.006240769, 0, 0]
}

data_va = {
    'Label': ['1a', '2a', '3a', '4a'],
    '1': [11.50068918, 8.556598897, 6.37706754, 5.349758787],
    '2': [1.249138525, 0.577188146, 0.568573398, 0.547036527],
    '3': [0.131374914, 0.038766368, 0.038766368, 0.051688491],
    '4': [0.006461061, 0.004307374, 0.004307374, 0.002153687]
}

data_ce = {
    'Label': ['1a', '2a', '3a', '4a'],
    '1': [8.470956458, 7.001749056, 5.784774003, 4.952591365],
    '2': [1.450796281, 0.913191568, 1.03286385, 0.55233361],
    '3': [0.097578938, 0.150971187, 0.130718954, 0.055233361],
    '4': [0.073644481, 0.00920556, 0.001841112, 0.001841112]
}

data_ba = {
    'Label': ['1a', '2a', '3a', '4a'],
    '1': [7.619978781, 5.573006594, 4.722181773, 4.383099998],
    '2': [0.95275738, 0.42021177, 0.457656383, 0.418131514],
    '3': [0.07280897, 0.085290508, 0.104012814, 0.066568201],
    '4': [0.002080256, 0.002080256, 0.002080256, 0]
}

# Creating DataFrames
df_no = pd.DataFrame(data_no)
df_va = pd.DataFrame(data_va)
df_ce = pd.DataFrame(data_ce)
df_ba = pd.DataFrame(data_ba)

# Function to plot data
def plot_data(df, title, filename):
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    # Adjusting font sizes
    title_fontsize = 20
    label_fontsize = 15
    tick_fontsize = 12
    general_title_fontsize = 25

    # Titles and ylabel values
    titles = ['1', '2', '3', '4']
    ylabel = '% de paraules sobre el total'

    # Plotting each subplot
    for i in range(2):
        for j in range(2):
            col_name = df.columns[i * 2 + j + 1]  # Column name (1, 2, 3, 4)
            axs[i, j].bar(df['Label'], df[col_name], width=0.4)
            axs[i, j].set_title(f'{titles[i * 2 + j]}', fontsize=title_fontsize)  # Set title
            axs[i, j].set_ylabel(ylabel, fontsize=label_fontsize)  # Set ylabel
            axs[i, j].tick_params(axis='both', which='major', labelsize=tick_fontsize)

    # General title
    fig.suptitle(title, fontsize=general_title_fontsize)

    # Adjust layout
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust rect to make room for suptitle

    # Save the figure as a PNG file
    plt.savefig(filename)

    # Display the plots
    plt.show()

# Plotting each table
plot_data(df_no, 'NO Data Comparison', 'no_data.png')
plot_data(df_va, 'VA Data Comparison', 'va_data.png')
plot_data(df_ce, 'CE Data Comparison', 'ce_data.png')
plot_data(df_ba, 'Ba Data Comparison', 'ba_data.png')
