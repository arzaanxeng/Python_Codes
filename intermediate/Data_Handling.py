import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    'Name': ['Rahul', 'Priya', ' Amit', 'Neha', 'Vikram', 'Rohan', 'Sneha'],
    'Role': ['Developer', 'Designer', 'Developer', 'Designer', 'Marketing', 'Developer', 'Marketing'],
    'Age': [20, 21, 999, 20, 22, 19, 21],
    'Stipend': [10000, 12000, np.nan, 11000, 15000, 85000, 10500]
}

df = pd.DataFrame(data)
print("\n--- Original Raw Data ---\n")
print(df)

df['Name'] = df['Name'].str.strip()
median_age = df[df['Age'] != 999]['Age'].median()
df['Age'] = df['Age'].replace(999, median_age)
overall_median_stipend = df['Stipend'].median()
df['Stipend'] = df['Stipend'].fillna(overall_median_stipend)

print("\n--- Cleaned & Preprocessed Dataset ---\n")
print(df)

mean_stipend = df['Stipend'].mean()
median_stipend = df['Stipend'].median()
print("\n--- Statistical Metrics ---\n")
print(f"Mean Stipend:   ₹{mean_stipend:,.2f}")
print(f"Median Stipend: ₹{median_stipend:,.2f}")
print(f"Variance (Mean - Median Difference): ₹{mean_stipend - median_stipend:,.2f}")

print("\n>Observations:")
print("The high variance between the Mean and the Median highlights the heavy distortion")
print("caused by Rohan's stipend (₹85,000). While the typical intern makes ₹11,000 (Median),")
print("the single extreme outlier artificially inflates the company average (Mean) to over ₹22,000.")

# visualization of the data processed

sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 4))
sns.boxplot(x=df['Stipend'], color='blue')
plt.title('Distribution of Intern Stipends (Identifying Outliers)', fontsize=14, pad=15)
plt.xlabel('Stipend Amount (₹)', fontsize=12)
plt.tight_layout()
plt.savefig("Data_Visualization_1")
plt.show()

plt.figure(figsize=(8, 6))
colors = {'Developer': 'red', 'Designer': 'yellow', 'Marketing': 'orange'}

for role in df['Role'].unique():
    role_data = df[df['Role'] == role]
    plt.scatter(role_data['Age'], role_data['Stipend'],
                s=100, alpha=0.8, label=role, color=colors[role], linewidth=1)

for i, row in df.iterrows():
    plt.annotate(row['Name'], (row['Age'], row['Stipend']),
                 xytext=(5, 5), textcoords='offset points', fontsize=9)

plt.title('Intern Compensation Analysis: Age vs. Stipend', fontsize=14, pad=15)
plt.xlabel('Age of Intern', fontsize=12)
plt.ylabel('Stipend Amount (₹)', fontsize=12)
plt.legend(title='Role')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig("Data_Visualization_2")
plt.show()
