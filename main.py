import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Download and load the dataset
file_path = 'data.csv'
df = pd.read_csv(file_path)

# 2. Filter valid prices (> 0)
df_clean = df[df['price'] > 0].copy()

# ---------------------------------------------------------
# FIGURE 1: More expensive cities in average price
# ---------------------------------------------------------
# Sorted average price by city of top 10 cities
top_cities = df_clean.groupby('city')['price'].mean().sort_values(ascending=False).head(10)

# Basic 
plt.figure(figsize=(10, 5))
sns.barplot(x=top_cities.values, y=top_cities.index, palette='viridis')
plt.title('Top 10 Ciudades con Precios Promedio Más Altos')
plt.xlabel('Precio Promedio ($)')
plt.ylabel('Ciudad')
plt.savefig('top_cities_price.png', dpi=300, bbox_inches='tight')
plt.close() # Free memory and clear canvas
print("Saved: top_cities_price.png")


# ---------------------------------------------------------
# FIGURE 1: Bedrooms vs. Bathrooms Price Comparison
# ---------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Plot 1A: Median Price by Bedrooms
sns.barplot(
    data=df_clean[df_clean['bedrooms'] <= 8], 
    x='bedrooms', 
    y='price', 
    estimator=lambda x: pd.Series(x).median(),
    ax=axes[0], 
    palette='Blues_d'
)
axes[0].set_title('Median Price by Number of Bedrooms')
axes[0].set_xlabel('Bedrooms')
axes[0].set_ylabel('Median Price ($)')
axes[0].grid(axis='y', linestyle='--', alpha=0.7)

# Plot 1B: Median Price by Bathrooms
sns.barplot(
    data=df_clean[df_clean['bathrooms'] <= 5], 
    x='bathrooms', 
    y='price', 
    estimator=lambda x: pd.Series(x).median(),
    ax=axes[1], 
    palette='Greens_d'
)
axes[1].set_title('Median Price by Number of Bathrooms')
axes[1].set_xlabel('Bathrooms')
axes[1].set_ylabel('Median Price ($)')
axes[1].tick_params(axis='x', rotation=45)
axes[1].grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()

# Save Figure 1 to the project root directory
plt.savefig('bedrooms_vs_bathrooms_price.png', dpi=300, bbox_inches='tight')
plt.close() # Free memory and clear canvas
print("Saved: bedrooms_vs_bathrooms_price.png")

# ---------------------------------------------------------
# FIGURE 2: Heatmap Matrix (Bedrooms vs. Bathrooms)
# ---------------------------------------------------------
df_filtered = df_clean[
    (df_clean['bedrooms'].between(1, 6)) & 
    (df_clean['bathrooms'].between(1, 4))
]

pivot_price = df_filtered.pivot_table(
    index='bedrooms', 
    columns='bathrooms', 
    values='price', 
    aggfunc='median'
)

plt.figure(figsize=(10, 6))
sns.heatmap(
    pivot_price, 
    annot=True, 
    fmt=",.0f", 
    cmap="YlGnBu", 
    cbar_kws={'label': 'Median Price ($)'}
)
plt.title('Median Price Matrix: Bedrooms vs. Bathrooms')
plt.xlabel('Bathrooms')
plt.ylabel('Bedrooms')

# Save Figure 2 to the project root directory
plt.savefig('bedrooms_bathrooms_heatmap.png', dpi=300, bbox_inches='tight')
plt.close() # Free memory and clear canvas
print("Saved: bedrooms_bathrooms_heatmap.png")