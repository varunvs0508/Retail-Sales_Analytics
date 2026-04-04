def perform_eda(df):
    monthly_sales = df.groupby('Month')['total_amount'].sum()
    category_revenue = df.groupby('category')['total_amount'].sum().sort_values(ascending=False)
    city_revenue = df.groupby('city')['total_amount'].sum().sort_values(ascending=False)
    discount_analysis = df.groupby('discount_pct')['total_amount'].mean()
    customer_spending = df.groupby('customer_id')['total_amount'].sum().sort_values(ascending=False)

    return monthly_sales, category_revenue, city_revenue, discount_analysis, customer_spending