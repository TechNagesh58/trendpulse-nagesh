
import pandas as pd
import numpy as np

# Load the clean CSV
df = pd.read_csv("/content/data/trends_clean.csv")

print(f"Loaded data: {df.shape}")

# Show first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Average score and comments
print(f"\nAverage score: {df['score'].mean()}")
print(f"Average comments: {df['num_comments'].mean()}")

# NumPy statistics
print("\n--- NumPy Stats ---")
print(f"Mean score: {np.mean(df['score'])}")
print(f"Median score: {np.median(df['score'])}")
print(f"Std deviation: {np.std(df['score'])}")
print(f"Max score: {np.max(df['score'])}")
print(f"Min score: {np.min(df['score'])}")

# Category with the most stories
category_counts = df["category"].value_counts()
print(f"\nMost stories in: {category_counts.idxmax()} ({category_counts.max()} stories)")

# Story with the most comments
most_commented = df["num_comments"].idxmax()
print(f"Most commented story: {df.loc[most_commented, 'title']} — {df.loc[most_commented, 'num_comments']} comments")

# Add engagement column
average_score = df["score"].mean()
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# Add popular column
df["is_popular"] = df["score"] > average_score

# Save analysed data
df.to_csv("/content/data/trends_analysed.csv", index=False)

print(f"\nSaved {len(df)} rows to data/trends_analysed.csv")
