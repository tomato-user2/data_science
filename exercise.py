import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a pandas DataFrame
data = pd.read_csv('umsatzdaten_gekuerzt.csv')

# Convert the 'Datum' column to datetime format
data['Datum'] = pd.to_datetime(data['Datum'])

# Create a new column for the weekday from the 'Datum' column
data['Wochentag'] = data['Datum'].dt.day_name()

# Group data by weekday and calculate mean turnover
mean_turnover_per_weekday = data.groupby('Wochentag')['Umsatz'].mean()

# Reorder the index to maintain the correct weekday order
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
mean_turnover_per_weekday = mean_turnover_per_weekday.reindex(weekday_order)

# Create a bar graph of the mean turnover per weekday
plt.figure(figsize=(10, 6))
mean_turnover_per_weekday.plot(kind='bar')
plt.xlabel('Wochentag')  # X-axis label
plt.ylabel('Mean Turnover')  # Y-axis label
plt.title('Mean Turnover per Weekday')  # Title
plt.show()  # Display the bar graph
