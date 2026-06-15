import pandas as pd
import matplotlib.pyplot as plt

# Load CSV
df = pd.read_csv("flipkart_sales_enriched.csv")

print(df.columns)   # Check column names

top_products = (
    df.groupby("Product Name")["Total Sales (INR)"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(12,6))
top_products.sort_values().plot(kind='barh')

plt.title("Top 10 Selling Products")
plt.xlabel("Total Sales (INR)")
plt.ylabel("Product Name")

plt.tight_layout()
plt.show()



