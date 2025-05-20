python
import pandas as pd
import matplotlib.pyplot as plt

# Load Public Transport Usage Data
transport_data = pd.read_csv('public_transport_usage_2024.csv')

# Load Healthcare Facility Utilization Data
healthcare_data = pd.read_json('health_facility_utilization_2024.json')

# Merge datasets on a common field, for example, 'location'
merged_data = pd.merge(transport_data, healthcare_data, on='location')

# Analyze the correlation between transport usage and healthcare visits
correlation = merged_data[['passenger_count', 'patient_visits']].corr()
print("Correlation between transport usage and healthcare visits:")
print(correlation)

# Visualize the data
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['passenger_count'], merged_data['patient_visits'], alpha=0.5)
plt.title('Correlation between Public Transport Usage and Healthcare Visits')
plt.xlabel('Passenger Count')
plt.ylabel('Patient Visits')
plt.grid(True)
plt.show()
