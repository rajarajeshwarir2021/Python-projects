import streamlit as st
import plotly.express as px
from backend import get_data


# Add widgets
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get the data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]

            # Add dynamic graph
            label = {"x": "Date", "y": "Temperature (deg C)"}
            figure = px.line(x=dates, y=temperatures, labels=label)
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/1.png", "Clouds": "images/2.png", "Rain": "images/3.png", "Snow": "images/4.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_condition]

            # Add dynamic sky condition images
            st.image(image_paths, width=115)
    except KeyError:
        st.write("The place does not exist.")