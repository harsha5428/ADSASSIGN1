import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_pie_chart(labels, values):
    """
    Plots a pie chart showing the distribution of values across the given labels.

    Parameters
    ----------
    labels : numpy array
        The labels to be shown on the pie chart.
    values : numpy array
        The values to be distributed across the pie chart.

    Returns
    -------
    None.

    """
    # Create a new figure
    plt.figure()
    
    # Plot the data as a pie chart with the given labels and values
    plt.pie(values, labels=labels, autopct='%1.2f')
    
    # Add a title to the plot
    plt.title("Distribution of Top 10 Online Stores in The Uk")
    
    # Save the plot as an image file
    plt.savefig("pie_chart.png")
    
    # Show the plot
    plt.show()

# Read the data from an Excel file and extract the relevant columns
df_stores = pd.read_excel("top10.xlsx", sheet_name="Data")
df_stores = df_stores[4:]

# Save the extracted data to a new CSV file
df_stores.to_csv("top10_stores.csv")

# Rename the columns to appropriate names
df_stores.columns = [' ', 'Store', 'Value']

# Extract the labels and values as numpy arrays
store_labels = np.array(df_stores['Store'])
store_values = np.array(df_stores['Value'])

# Plot the data as a pie chart
plot_pie_chart(store_labels, store_values)
