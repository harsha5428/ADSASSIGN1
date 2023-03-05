# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Define a function to generate a line plot
def generate_population_lineplot(df_population):
    """
    This function takes a dataframe as input and generates a line plot of the population
    of different countries over time.
    """
    plt.figure()
    
    # Add lines to the plot for each country
    plt.plot(df_population["Year"], df_population["Brazil"], label="Brazil")
    plt.plot(df_population["Year"], df_population["China"], label="China")
    plt.plot(df_population["Year"], df_population["United States"], label="United States")
    plt.plot(df_population["Year"], df_population["India"], label="India")
    plt.plot(df_population["Year"], df_population["Switzerland"], label="Switzerland")
    plt.plot(df_population["Year"], df_population["Philippines"], label="Philippines")

    # Set the x and y axis labels and tick formatting
    plt.xlabel("Time (in years)")
    plt.ylabel("Total Population")
    plt.ticklabel_format(style='plain', axis='y')

    # Add a title and legend to the plot
    plt.title("Comparison of Population among different countries")
    plt.legend()

    # Save the plot to a file and display it
    plt.savefig("population_lineplot.png")
    plt.show()


# Read the data from an Excel file and transform it into a dataframe
df_population_raw = pd.read_excel('Population.xls')
df_population = pd.DataFrame.transpose(df_population_raw)
header = df_population.iloc[0].values.tolist()
df_population.columns = header
df_population = df_population[4:]
df_population = df_population.rename(columns={"Country Name": "Year"})

# Save the transformed dataframe to a CSV file
df_population.to_csv("population_dataframe.csv")

# Generate a line plot of the population of different countries over time
generate_population_lineplot(df_population)
