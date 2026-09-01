import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the analysed data from Task 3
df = pd.read_csv("data/trends_analysed.csv")

# Create outputs folder if it does not already exist
os.makedirs("outputs", exist_ok=True)

# --------------------------------------------------
# Chart 1: Top 10 Stories by Score
# --------------------------------------------------

top10 = df.nlargest(10, "score").sort_values("score")

# Shorten titles longer than 50 characters
top10["short_title"] = top10["title"].apply(
    lambda x: x[:50] + "..." if len(x) > 50 else x
)

plt.figure(figsize=(10, 6))
plt.barh(top10["short_title"], top10["score"])

plt.title("Top 10 Stories by Score")
plt.xlabel("Score")
plt.ylabel("Story Title")

plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.show()

# --------------------------------------------------
# Chart 2: Stories per Category
# --------------------------------------------------

category_counts = df["category"].value_counts()

colors = ["red", "blue", "green", "orange", "purple"]

plt.figure(figsize=(8, 5))
plt.bar(category_counts.index, category_counts.values, color=colors)

plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Number of Stories")

plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.show()

# --------------------------------------------------
# Chart 3: Score vs Comments
# --------------------------------------------------

popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure(figsize=(8, 6))

plt.scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)

plt.scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular"
)

plt.title("Score vs Comments")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.legend()

plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.show()

# --------------------------------------------------
# Bonus: TrendPulse Dashboard
# --------------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# Chart 1
axes[0, 0].barh(top10["short_title"], top10["score"])
axes[0, 0].set_title("Top 10 Stories by Score")
axes[0, 0].set_xlabel("Score")
axes[0, 0].set_ylabel("Story Title")

# Chart 2
axes[0, 1].bar(
    category_counts.index,
    category_counts.values,
    color=colors
)
axes[0, 1].set_title("Stories per Category")
axes[0, 1].set_xlabel("Category")
axes[0, 1].set_ylabel("Number of Stories")

# Chart 3
axes[1, 0].scatter(
    popular["score"],
    popular["num_comments"],
    label="Popular"
)

axes[1, 0].scatter(
    not_popular["score"],
    not_popular["num_comments"],
    label="Not Popular"
)

axes[1, 0].set_title("Score vs Comments")
axes[1, 0].set_xlabel("Score")
axes[1, 0].set_ylabel("Number of Comments")
axes[1, 0].legend()

# Remove unused fourth subplot
fig.delaxes(axes[1, 1])

# Overall dashboard title
fig.suptitle("TrendPulse Dashboard", fontsize=16)

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.show()

print("All charts saved successfully.")
