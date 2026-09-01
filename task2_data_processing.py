
import pandas as pd
df= pd.read_json("/content/trends_20260831.json")
print(f"Loaded {len(df)} stories")


print(df['post_id'].duplicated().sum())

df = df.drop_duplicates(subset='post_id')

print(f"After removing duplicates:{len(df)}")

df=df.dropna(subset=['post_id','title','score'])

print(f"After removing null :{len(df)}")

df['score'] = df['score'].astype(int)
df['num_comments'] = df['num_comments'].astype(int)

df[['score', 'num_comments']].dtypes

df = df[df['score']>=5]

print(f"After removing low score : {len(df)}")

df['title'] = df['title'].str.strip()

print(df['title'].head())

import os

os.makedirs("/content/data", exist_ok=True)

df.to_csv("/content/data/trends_clean.csv", index=False)

print(f"Saved {len(df)} rows to data/trends_clean.csv")

print("Stories for categories :")
print(df['category'].value_counts())

