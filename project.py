# 📌 Required libraries import karna
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 Dataset load karna
url = "https://raw.githubusercontent.com/datablist/sample-csv-files/main/files/people/people-100.csv"
df = pd.read_csv('healthcare_data.csv')


# 📌 Dataset ki basic info check karna
print("🔹 Dataset Information:")
print(df.info())

# 📌 Missing values check karna
print("\n🔹 Missing Values in Dataset:")
print(df.isnull().sum())

# 📌 Age Distribution Analysis
plt.figure(figsize=(10, 6))
sns.histplot(df['Age'], bins=20, kde=True, color='blue')
plt.title('Age Distribution of Patients')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# 📌 Gender Distribution Analysis
plt.figure(figsize=(6, 4))
sns.countplot(x='Gender', data=df, palette="pastel")
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

# 📌 Most Common Medical Conditions
plt.figure(figsize=(12, 6))
sns.countplot(y='Diagnosis', data=df, order=df['Diagnosis'].value_counts().index, palette="coolwarm")
plt.title('Most Common Medical Conditions')
plt.xlabel('Count')
plt.ylabel('Medical Condition')
plt.show()

# 📌 Admission Type Analysis
plt.figure(figsize=(6, 4))
sns.countplot(x='Admission Type', data=df, palette="Set2")
plt.title('Admission Types Distribution')
plt.xlabel('Admission Type')
plt.ylabel('Count')
plt.show()

# 📌 Summary Insights
print("\n🔹 Key Observations:")
print("✅ 1. Patients ka age distribution dekha ja sakta hai.")
print("✅ 2. Male aur Female patients ka ratio show ho raha hai.")
print("✅ 3. Most common diseases ka analysis mil gaya hai.")
print("✅ 4. Admission ka type (Emergency ya Normal) visualize ho gaya hai.")
