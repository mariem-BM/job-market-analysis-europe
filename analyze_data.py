import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("clean_jobs_data.csv")

# Count how many job offers per country
print("\n--- Job offers per country ---")
print(df["country"].value_counts())

# Count how many job offers per searched keyword
print("\n--- Job offers per keyword ---")
print(df["search_keyword"].value_counts())

# List of skill columns (all columns starting with "skill_")
skill_columns = [col for col in df.columns if col.startswith("skill_")]

# Count how often each skill appears (sum of True values), sorted descending
print("\n--- Skill demand (overall) ---")
print(df[skill_columns].sum().sort_values(ascending=False))

# Skill demand broken down by country
print("\n--- Skill demand by country ---")
print(df.groupby("country")[skill_columns].sum())

# Average minimum salary by country (ignoring missing values automatically)
print("\n--- Average minimum salary by country ---")
print(df.groupby("country")["salary_min"].mean())