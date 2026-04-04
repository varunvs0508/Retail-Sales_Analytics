import matplotlib.pyplot as plt

def create_dashboard(df, monthly_sale, category_revenue, city_revenue, discount_analysis, customer_spending):
    print("\n=== Data Visualization ===")

    plt.style.use('default')
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    fig.suptitle('GMart Retail Sales Analytics Dashboard', fontsize=16, fontweight='bold')

    # Monthly Sales Trend
    axes[0, 0].plot(monthly_sale.index, monthly_sale.values, marker='o', linewidth=2, markersize=6)
    axes[0, 0].set_title('Monthly Sales Trend', fontweight='bold')
    axes[0, 0].set_xlabel('Month')
    axes[0, 0].set_ylabel('Total Sales Amount (M)')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Category-wise Revenue
    bars = axes[0, 1].bar(category_revenue.index, category_revenue.values, color='skyblue', alpha=0.8)
    axes[0, 1].set_title('Category-wise Revenue', fontweight='bold')
    axes[0, 1].set_xlabel('Category')
    axes[0, 1].set_ylabel('Revenue (M)')
    axes[0, 1].tick_params(axis='x', rotation=45)
    for bar in bars:
        height = bar.get_height()
        axes[0, 1].text(bar.get_x() + bar.get_width()/2., height + 500,
                       f'${height:,.0f}', ha='center', va='bottom', fontsize=8)

    # City-wise Revenue
    bars = axes[0, 2].bar(city_revenue.index, city_revenue.values, color='lightgreen', alpha=0.8)
    axes[0, 2].set_title('City-wise Revenue', fontweight='bold')
    axes[0, 2].set_xlabel('City')
    axes[0, 2].set_ylabel('Revenue (M)')
    axes[0, 2].tick_params(axis='x', rotation=45)
    for bar in bars:
        height = bar.get_height()
        axes[0, 2].text(bar.get_x() + bar.get_width()/2., height + 500,
                       f'${height:,.0f}', ha='center', va='bottom', fontsize=8)

    # Discount vs Revenue Analysis
    axes[1, 0].bar(discount_analysis.index.astype(str), discount_analysis.values, color='orange', alpha=0.8)
    axes[1, 0].set_title('Average Sales by Discount Percentage', fontweight='bold')
    axes[1, 0].set_xlabel('Category')
    axes[1, 0].set_ylabel('Average Sales Amount')

    # Customer Spending Distribution
    axes[1, 1].hist(customer_spending.values, bins=30, color='purple', alpha=0.7, edgecolor='black')
    axes[1, 1].set_title('Customer Spending Distribution', fontweight='bold')
    axes[1, 1].set_xlabel('Total Spending')
    axes[1, 1].set_ylabel('Number of Customers')
    axes[1, 1].axvline(customer_spending.mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: ${customer_spending.mean():.0f}')
    axes[1, 1].legend()

    # Payment Mode Distribution
    payment_dist = df['payment_mode'].value_counts()
    axes[1, 2].pie(payment_dist.values, labels=payment_dist.index, autopct='%1.1f%%', startangle=90)
    axes[1, 2].set_title('Payment Mode Distribution', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('gmart_sales_analytics.png', dpi=300, bbox_inches='tight')
    plt.show()

    print("Dashboard saved as 'gmart_sales_analytics.png'")