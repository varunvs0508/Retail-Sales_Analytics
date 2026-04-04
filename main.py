from src.data_loader import load_data
from src.preprocessing import clean_data
from src.feature_engineering import create_features
from src.eda import perform_eda
from src.visualization import create_dashboard
from src.database import load_to_db
from src.insights import generate_insights

def main():
    df = load_data("data/Gmart_sales_data.csv")

    df = clean_data(df)
    df = create_features(df)

    monthly_sales, category_revenue, city_revenue, discount_analysis, customer_spending = perform_eda(df)

    create_dashboard(df, monthly_sales, category_revenue, city_revenue, discount_analysis, customer_spending)

    load_to_db(df)

    generate_insights(df, category_revenue, city_revenue, customer_spending)

if __name__ == "__main__":
    main()