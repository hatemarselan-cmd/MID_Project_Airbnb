
import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

st.set_page_config(layout= 'wide', page_title= 'Airbnb_USA_prices')
html_title = "<h1 style=color:Black;text-align:center;> Airbnb EDA Project </h1>"
st.markdown(html_title, unsafe_allow_html= True)

st.image('data:image/jpeg;base64,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',width=1000)

# Sidebar page selection
page = st.sidebar.radio('Page', ['Home', 'GEO_map', 'CAT_NUM_analysis','other'])

# Load dataset
df = pd.read_csv('cleaned_df.csv', index_col=0)

if page == 'Home':
    st.header('Dataset Overview')
    st.dataframe(df.head(10))
    
    st.header("📝 Column Descriptions")

    with st.expander("📘 Click to view dataset column descriptions"):

        col_desc = {
            "id": "Unique listing identifier.",
            "log_price": "Log-transformed nightly price.",
            "property_type": "Type of property (Apartment, House, etc.).",
            "room_type": "Type of room (Entire home/apt, Private room, etc.).",
            "amenities": "List of amenities provided in the listing.",
            "accommodates": "Maximum number of guests the listing can host.",
            "bathrooms": "Number of bathrooms.",
            "bed_type": "Type of bed provided.",
            "cancellation_policy": "Cancellation policy category (strict, moderate, flexible).",
            "cleaning_fee": "Whether a cleaning fee is charged (TRUE/FALSE).",
            "city": "City where the listing is located.",
            "description": "Text description written by the host.",
            "first_review": "Date of the first guest review.",
            "host_has_profile_pic": "Whether the host has a profile picture.",
            "host_identity_verified": "Whether the host’s identity is verified.",
            "host_response_rate": "Host’s response rate (e.g., 100%).",
            "host_since": "Date the host joined the platform.",
            "instant_bookable": "Whether guests can book instantly.",
            "last_review": "Date of the most recent review.",
            "latitude": "Latitude coordinate of the listing.",
            "longitude": "Longitude coordinate of the listing.",
            "name": "Listing title.",
            "neighbourhood": "Neighborhood name.",
            "number_of_reviews": "Total number of reviews.",
            "review_scores_rating": "Average review rating.",
            "thumbnail_url": "URL of the listing's thumbnail image.",
            "zipcode": "Postal code of the listing location.",
            "bedrooms": "Number of bedrooms.",
            "beds": "Number of beds."
        }

        desc_df = pd.DataFrame(
            list(col_desc.items()), 
            columns=["Column Name", "Description"]
        )

        st.table(desc_df)

    
if page == 'GEO_map':
   
    st.title("🌍Airbnb Listings Map")

    #  CITY DROPDOWN 
    cities = sorted(df["city"].unique())

    selected_city = st.selectbox(
        "Select City",
        cities
    )

    # Filter dataframe by selected city
    df_city = df[df["city"] == selected_city]

    #  NEIGHBOURHOOD MULTISELECT 
    neighbourhoods = sorted(df_city["neighbourhood"].unique())

    selected_neighbourhoods = st.multiselect(
        "Select Neighbourhood(s)",
        neighbourhoods,
        default=neighbourhoods  # show all by default
    )

    # Filter by neighbourhood
    df_city_nei = df_city[df_city["neighbourhood"].isin(selected_neighbourhoods)]

    #  MAP 
    if len(df_city_nei) == 0:
        st.warning("No listings found for selected city/neighbourhood.")
    else:
        fig = px.scatter_mapbox(
            df_city_nei,
            lat="latitude",
            lon="longitude",
            color="price_original_$",
            size="price_original_$",
            mapbox_style="open-street-map",
            zoom=10,
            height=650,
            title=f"Airbnb Listings in {selected_city}",
            color_continuous_scale="Reds"
        )
    st.plotly_chart(fig, use_container_width=True)
    total_accommodations = len(df_city_nei)
    total_revenue = df_city_nei['price_original_$'].sum()
    avg_price = df_city_nei['price_original_$'].mean()

    st.markdown(
        f"<h3 style='color:#FF4B4B;'>📍 Metrics for <b>{selected_city}</b></h3>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("🏘️ Total units", f"{total_accommodations:,}")
    col2.metric("💰 Total Revenue", f"${total_revenue:,.2f}")
    col3.metric("📊 Average Price per unit", f"${avg_price:,.2f}")
    
    # PRICE OUTLIERS (20% / 80%)
    p20 = df_city_nei["price_original_$"].quantile(0.20)
    p80 = df_city_nei["price_original_$"].quantile(0.80)
    # Under priced units (<20th )
    under_count = df_city_nei[df_city_nei["price_original_$"] < p20]["price_original_$"].count()
    under_avg   = df_city_nei[df_city_nei["price_original_$"] < p20]["price_original_$"].mean()
    # Over priced units (>80th )
    over_count  = df_city_nei[df_city_nei["price_original_$"] > p80]["price_original_$"].count()
    over_avg    = df_city_nei[df_city_nei["price_original_$"] > p80]["price_original_$"].mean()
    # Display outlier KPIs
    if st.checkbox('Price over/under priced Analysis'):
        st.subheader("📊 Price over/under price Analysis")
        col4, col5, col6, col7 = st.columns(4)
        col4.metric("⬇️ No of Under-Priced Units", f"{under_count:,}")
        col5.metric("💵 Avg Under Price", f"${under_avg:,.2f}")
        col6.metric("⬆️ No of Over-Priced Units", f"{over_count:,}")
        col7.metric("💰 Avg Over Price", f"${over_avg:,.2f}")
        
if page=="CAT_NUM_analysis":
    # Number of units per city
    st.subheader("🏙️ Top 5 Cities with the Highest Revenue")
    st.plotly_chart(px.histogram(data_frame=df,x='city',color='city',text_auto=True,title=' The number of units per city').update_xaxes(categoryorder = 'max descending'))
    
    #- What are the top 5 cities with the highest revenue ?
    top_5_city = df.groupby(['city'])['price_original_$'].sum().reset_index().sort_values(by= 'price_original_$', ascending= False).head(5)
    st.subheader("🏙️ Top 5 Cities with the Highest Revenue")
    st.plotly_chart(px.bar(data_frame= top_5_city, x= 'city', y= 'price_original_$',color='city',title= 'Top 5 city with the highest revenue', text_auto= True))
    
    
    #- What are the top 20 neighbourhod per city  with the median prices ?
    st.subheader("📍 Top 20 Neighbourhoods per City (Median Prices)")
    top_20_nei = df.groupby(['city','neighbourhood'])['price_original_$'].median().reset_index().sort_values(by= 'price_original_$', ascending= False).head(20)
    st.plotly_chart(px.bar(data_frame= top_20_nei, x= 'neighbourhood', y= 'price_original_$',color='city',title= 'Top 20 neighborhod with the median price', text_auto= True))
    
    
    #- Which room types have the highest average prices per city ?
    st.subheader("🛏️ Room Types with the Highest Average Prices per City")
    top_city_room=df.groupby(['city','room_type'])['price_original_$'].mean().reset_index().sort_values(by= 'price_original_$', ascending= False)
    st.plotly_chart(px.bar(data_frame=top_city_room,x='city',y='price_original_$',color='room_type',barmode= 'group',text_auto=True,title="room_type vs prices per city ").update_xaxes(categoryorder = 'max descending'))
    
    
    #- Which bed types have the highest average prices per city ?
    top_city_bed_type=df.groupby(['city','bed_type'])['price_original_$'].mean().reset_index().sort_values(by= 'price_original_$', ascending= False)
    st.subheader("🛋️ Bed Types with the Highest Average Prices per City")
    st.plotly_chart(px.bar(data_frame=top_city_bed_type,x='city',y='price_original_$',color='bed_type',barmode= 'group',text_auto=True,title="bed_type vs prices per city ").update_xaxes(categoryorder = 'max descending')) 
      
    #- How do the price will impact cancellation_policy ?
    top_city_cancel=df.groupby(['city','cancellation_policy'])['price_original_$'].mean().reset_index().sort_values(by= 'price_original_$', ascending= False)
    st.subheader("⚖️ Impact of Price on Cancellation Policy")
    st.plotly_chart(px.bar(data_frame=top_city_cancel,x='city',y='price_original_$',color= 'cancellation_policy',barmode='group',text_auto=True,title="cancellation_policy vs prices per city ").update_xaxes(categoryorder = 'max descending'))
    
    
if page == 'other':
    
    # CITY DROPDOWN 
    cities = sorted(df["city"].unique())
    selected_city = st.selectbox("Select City",cities)
    # Filter dataframe by selected city
    df_city = df[df["city"] == selected_city]
    
    #- What are the most common amenities across all units?
    amen_cols = [c for c in df_city.columns if c.startswith('amenity__')] ## list comprehension used to select all columns related to amenities
    amen_counts = df_city[amen_cols].sum() # Count how many  each amenity
    amen_pct = (amen_counts / len(df_city)) * 100
    amen_pct = amen_pct.sort_values(ascending=False).head(20)# Take top 20 amenities
    amen_df = amen_pct.reset_index() ## convert to dataframe
    amen_df.columns = ["Amenity", "Percentage"]
    st.subheader("🧩 Most Common Amenities Across All unites")
    st.plotly_chart(px.bar(data_frame=amen_df,x="Amenity", y="Percentage",title="Top 20 Amenities (Percentage of Listings)",labels={"Percentage": "Percentage (%)"},
    ))
    
    #- which amenity has the highest average price ?
    # Select amenity columns
    amen_cols = [c for c in df_city.columns if c.startswith('amenity__')]
    amen_price = []
    for col in amen_cols:
        count = df[col].sum()  # how many unites have this amenity
        avg_price = df_city[df_city[col] == 1]["price_original_$"].mean().round(2)  # average price
        amen_price.append([col, count, avg_price])
    # Convert to dataframe
    amen_price_df = pd.DataFrame(amen_price, columns=["Amenity", "Count", "Avg_LogPrice($)"])
    # Sort by highest price
    amen_price_df = amen_price_df.sort_values("Avg_LogPrice($)", ascending=False).head(20)
    st.subheader("💎 Amenities Associated with the Highest Average Price")
    st.plotly_chart(px.scatter(data_frame=amen_price_df,y="Avg_LogPrice($)", x="Amenity", size= 'Count' ,title="Top 20 Amenities based on avg price"))
    
    #- heat map to corr between some numerical feature 
    num_cols = df.select_dtypes(include= 'number').columns
    num_cols = num_cols.tolist()
    num_corr = df[num_cols].corr().round(2)
    st.subheader("📊 Numerical Features Correlation Matrix")
    st.plotly_chart(px.imshow(num_corr, text_auto= True, title='correlation matrix', width=1000,height=1000,color_continuous_scale='Reds'))
    
  
