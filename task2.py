import pandas as pd

# Read the CSV files
data1 = pd.read_csv(r'C:\Users\Lenovo\quantium-starter-repo\data\daily_sales_data_0.csv')
data2 = pd.read_csv(r'C:\Users\Lenovo\quantium-starter-repo\data\daily_sales_data_1.csv')
data3 = pd.read_csv(r'C:\Users\Lenovo\quantium-starter-repo\data\daily_sales_data_2.csv')

# Concatenate the data
data = pd.concat([data1, data2, data3])

# Filter the data to include only "Pink Morsels"
data = data[data['product'] == 'pink morsel']

# Create a 'sales' column
data['sales'] = data['price'] * data['quantity']

# Select the required columns
formatted_data = data[['sales', 'date', 'region']]

# Save the formatted data to a new CSV file
formatted_data.to_csv(r'C:\Users\Lenovo\quantium-starter-repo\data\formatted_sales_data.csv', index=False)

print("Formatted data saved to 'formatted_sales_data.csv'")

