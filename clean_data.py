import pandas as pd

# Load the raw data we extracted from the API
df = pd.read_csv("raw_jobs_data.csv")
print(f"Rows before cleaning: {len(df)}")

# Remove duplicate job offers based on the URL
# (the same offer can appear under multiple keyword searches)
df = df.drop_duplicates(subset="url")
print(f"Rows after removing duplicates: {len(df)}")

# Convert the 'created' column from text to a real date type
# errors="coerce" means: if a date can't be parsed, put NaT (missing) instead of crashing
df["created"] = pd.to_datetime(df["created"], errors="coerce")

# List of skills we want to detect inside job descriptions
SKILLS = ["python", "sql", "power bi", "excel", "tableau", "spark",
          "airflow", "snowflake", "aws", "azure", "r", "sas"]

# Make sure description is always text, even if some values are missing (NaN)
df["description"] = df["description"].fillna("").str.lower()

# For each skill, create a new column that is True/False
# depending on whether the skill name appears in the description
for skill in SKILLS:
    column_name = "skill_" + skill.strip().replace(" ", "_")
    # \b means "word boundary": ensures we match the whole word only
    pattern = r"\b" + skill + r"\b"
    df[column_name] = df["description"].str.contains(pattern, regex=True, na=False)

# Save the cleaned dataset
df.to_csv("clean_jobs_data.csv", index=False)
print("File saved: clean_jobs_data.csv")