def create_features(df):
    df['Month'] = df['order_date'].dt.month
    df['Quarter'] = df['order_date'].dt.quarter
    df['Year'] = df['order_date'].dt.year

    metro_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Hyderabad', 'Pune']
    df['city_type'] = df['city'].apply(lambda x: 'Metro' if x in metro_cities else 'Non-Metro')

    return df