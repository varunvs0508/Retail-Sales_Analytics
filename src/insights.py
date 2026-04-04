def generate_insights(df, category_revenue, city_revenue, customer_spending):
    total_revenue = df['total_amount'].sum()

    print("\n=== Insights ===")

    print(f"Top Category: {category_revenue.index[0]}")
    print(f"Top City: {city_revenue.index[0]}")

    top_20 = int(len(customer_spending) * 0.2)
    top_rev = customer_spending.head(top_20).sum()

    print(f"Top 20% customers contribute {(top_rev/total_revenue)*100:.2f}% revenue")