# Import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualisation styles
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Load the Wine Quality dataset from the UCI Machine Learning Repository into a DataFrame
wine_data_url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_data = pd.read_csv(wine_data_url, sep=';')  # The separator in this dataset is a semicolon

# Data Overview
print("First 5 rows of the dataset:")
print(wine_data.head(), "\n")

print("Shape of the DataFrame:")
print(wine_data.shape, "\n")

print("Data types of the columns:")
print(wine_data.dtypes, "\n")

# Check for missing values
print("Missing values in each column:")
print(wine_data.isnull().sum(), "\n")

# Summary Statistics
print("Summary Statistics:")
print(wine_data.describe(), "\n")

# Frequency Distribution of the 'quality' column
print("Frequency Distribution of the 'quality' column:")
quality_counts = wine_data['quality'].value_counts()
print(quality_counts, "\n")

# Data Visualization
# Histogram of the 'quality' column
plt.figure(figsize=(8, 6))
sns.countplot(x='quality', data=wine_data)
plt.title('Frequency Distribution of Wine Quality')
plt.xlabel('Quality')
plt.ylabel('Frequency')
plt.show()

# Box plots for each variable grouped by 'quality'
wine_data_melted = pd.melt(wine_data, id_vars='quality', var_name='variables', value_name='values')
plt.figure(figsize=(12, 6))
sns.boxplot(x='variables', y='values', hue='quality', data=wine_data_melted)
plt.xticks(rotation=90)
plt.title('Box plots of Variables Grouped by Wine Quality')
plt.show()
