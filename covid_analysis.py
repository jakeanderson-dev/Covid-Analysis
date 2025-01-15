import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Step 1: Load the dataset
data = pd.read_csv('owid-covid-data.csv')

# Step 2: Filter the data for the United States
us_data = data[data['location'] == 'United States']

# Step 3: Select relevant columns for analysis
us_data = us_data[['date', 'new_cases', 'total_cases']]

# Step 4: Convert the 'date' column to datetime format
us_data['date'] = pd.to_datetime(us_data['date'])

# Step 5: Handle missing data
# Drop rows with missing values
us_data = us_data.dropna()

# Define a function to format numbers
def format_numbers(x, pos):
    """ Format the numbers with commas and avoid scientific notation. """
    return f'{int(x):,}'

# Step 6: Plotting new cases over time
plt.figure(figsize=(12, 6))  # Set the size of the plot
plt.plot(us_data['date'], us_data['new_cases'], label='New Cases', color='blue')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.title('New COVID-19 Cases Over Time in the United States')

# Rotate the x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Format the y-axis with custom function
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_numbers))

# Add a legend
plt.legend()

# Save the new cases plot as a PNG image
plt.tight_layout()  # Adjust the layout to prevent clipping
plt.savefig('new_cases_plot.png')  # For the new cases plot

# Display the plot (optional, this is just for visualization)
plt.show()

# Step 7: Plotting total cases over time
plt.figure(figsize=(12, 6))  # Set the size of the plot
plt.plot(us_data['date'], us_data['total_cases'], label='Total Cases', color='red')

# Adding labels and title
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('Total COVID-19 Cases Over Time in the United States')

# Rotate the x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Format the y-axis with custom function
plt.gca().yaxis.set_major_formatter(FuncFormatter(format_numbers))

# Add a legend
plt.legend()

# Save the total cases plot as a PNG image
plt.tight_layout()  # Adjust the layout to prevent clipping
plt.savefig('total_cases_plot.png')  # For the total cases plot

# Display the plot (optional, this is just for visualization)
plt.show()

# Save the filtered dataset to a new CSV file
us_data.to_csv('us_covid_data.csv', index=False)






