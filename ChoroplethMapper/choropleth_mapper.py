import sys
import pandas as pd
import plotly.express as px

def load_data(choice):
    if choice == "population":
        return pd.read_csv("data/population.csv"), "Population", "World Population"
    elif choice == "covid":
        return pd.read_csv("data/covid.csv"), "Covid_Cases", "COVID-19 Confirmed Cases"
    elif choice == "temperature":
        return pd.read_csv("data/temperature.csv"), "Avg_Temp_C", "Average Temperature (°C)"
    else:
        raise ValueError("Invalid dataset choice")

def create_map(df, data_col, title):
    fig = px.choropleth(df,
                        locations="Code",
                        color=data_col,
                        hover_name="Country",
                        color_continuous_scale="Plasma",
                        title=title)
    fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
    fig.write_html("temp-plot.html")
    print("Map saved as temp-plot.html. Open this file in your browser to view the map.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        choice = sys.argv[1].strip().lower()
    else:
        print("Choose a dataset to visualize:")
        print("1. population")
        print("2. covid")
        print("3. temperature")
        choice = input("Enter dataset name: ").strip().lower()

    try:
        df, col, title = load_data(choice)
        create_map(df, col, title)
    except Exception as e:
        print("Error:", e) 
