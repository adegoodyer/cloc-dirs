import pandas as pd
import matplotlib.pyplot as plt

# Create empty lists to store the data
data = []
current_section = None # track each section(repo)

# Open the text file and read it line by line
with open('/path/to/file', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue  # Skip empty lines

        # Check if the line contains a section header
        if line.endswith('/'):
            current_section = line.strip('/')
            continue

        # Check if the line contains table headers
        if line.startswith("Language"):
            continue  # Skip table headers

        # Split the line into columns using whitespace as the delimiter
        columns = line.split()

        # Ensure that the line has the expected number of columns
        if len(columns) == 5:
            # Extract data into a dictionary
            entry = {
                "Repo": current_section,
                "Languages": columns[0],
                "Files": int(columns[1]),
                "Blank": int(columns[2]),
                "Comments": int(columns[3]),
                "Code": int(columns[4]),
            }

            # Append the dictionary to the data list
            data.append(entry)

# Create a pandas DataFrame from the data
df = pd.DataFrame(data)

# Display the DataFrame
# print(df)

# Sum the metrics across all repositories
total_metrics = df[['Repo', 'Files', 'Blank', 'Comments', 'Code']].groupby('Repo').sum()

# Plot the stacked bar chart for all repositories
ax = total_metrics.plot(kind='bar', stacked=True)

# Customize the plot
plt.xlabel('Repository')
plt.ylabel('Counts')
plt.title('Code Metrics for All Repositories')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.legend(title='Metrics', loc='upper right')

# Show the plot
plt.show()
