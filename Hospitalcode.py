# import required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# define function to plot hospital beds per thousand people for China
def plot_hospital_beds_per_thousand(dataframe):
    """
    Plots a bar graph showing the number of hospital beds per thousand people for China each year.

    Parameters
    ----------
    dataframe : pandas DataFrame
        The DataFrame containing the hospital bed data.

    Returns
    -------
    None.

    """
    # set figure size and plot data
    plt.figure(figsize=(10,6))
    plt.bar(dataframe["Year"], dataframe["China"], label="China")
    plt.title("Hospital Beds per Thousand People for China Each Year")
    plt.xlabel("Time (in years)")
    plt.ylabel("Number of Hospital Beds per Thousand People")
    plt.xticks(np.arange(1990,2019,2.0))
    plt.xlim(1990,2019)
    plt.savefig("bar.png")
    plt.show()
    
# load hospital data and transpose it
df_hospital = pd.read_excel('Hospital.xls')
df_hospital_transposed = pd.DataFrame.transpose(df_hospital)

# set column headers and select relevant data
header = df_hospital_transposed.iloc[0].values.tolist()
df_hospital_transposed.columns = header
df_hospital_transposed = df_hospital_transposed[4:]
df_hospital_transposed = df_hospital_transposed.rename(columns={"Country Name": "Year"})

# call function to plot hospital bed data for China
plot_hospital_beds_per_thousand(df_hospital_transposed)
