import pandas as pd

df = pd.read_csv("clean_jobs_data.csv")
print(df.head())

print(df.shape)
print(df.columns)
print(df.dtypes)

titles = df["title"]
print(titles.head())

subset = df[["title", "country", "salary_min"]]
print(subset.head())

# Keep only rows where country is "fr"
france_jobs = df[df["country"] == "fr"]
print(france_jobs.shape)

# Keep only rows where salary_min is above 50000
high_salary = df[df["salary_min"] > 50000]
print(high_salary.shape)

# Combine two conditions: country is "de" AND salary_min above 50000
germany_high_salary = df[(df["country"] == "de") & (df["salary_min"] > 50000)]
print(germany_high_salary.shape)

# Sort by salary, descending (highest first)
sorted_df = df.sort_values("salary_min", ascending=False)
print(sorted_df[["title", "country", "salary_min"]].head(10))