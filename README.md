## Integrated Analysis of Public Transport and Healthcare Facility Utilization in Abu Dhabi

### Overview
This project provides a comprehensive analysis by integrating public transport usage data and healthcare facility utilization data for Abu Dhabi in 2024. The integration aims to offer insights that facilitate urban planning and healthcare service optimization.

### Prerequisites
- Python 3.x
- Pandas
- Matplotlib

### Installation
1. Ensure you have Python installed on your system.
2. Install the required Python packages using pip:
   bash
   pip install pandas matplotlib
   

### Data Preparation
- Download the `public_transport_usage_2024.csv` and `health_facility_utilization_2024.json` datasets and place them in your working directory.

### Running the Analysis
- Use the provided Python script to load and merge the datasets:
  - The script merges the datasets on a common field such as 'location'.
  - It calculates the correlation between public transport usage and healthcare visits.
  - A scatter plot visualizes the relationship between the two variables.

### Interpretation
- The correlation matrix and scatter plot will help identify trends and insights on how transport accessibility impacts healthcare facility utilization.

### Conclusion
- This analysis aids policymakers in creating integrated solutions that improve public service delivery and infrastructure planning in Abu Dhabi.

### Contributing
- Contributions are welcome! Please fork the repository and submit a pull request.

### License
- This project is licensed under the MIT License.