import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the dataset
df = pd.read_csv("Data_set 2 - Copy.csv")
# Step 2: Extract the gender column
gender = df["gender"]

# Step 3: Count the number of people in each gender
gender_counts = gender.value_counts()

# Display the gender distribution
print("Gender Distribution:")
print(gender_counts)

# Step 4: Create a bar chart
plt.figure(figsize=(8, 5))

gender_counts.plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of People")

plt.xticks(rotation=0)

plt.tight_layout()

# Display the chart
plt.show()