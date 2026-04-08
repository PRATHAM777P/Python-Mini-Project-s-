import requests
import pandas as pd
import os

data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# --------- COVID-19: Our World In Data ---------
def update_covid_data():
    url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
    print("Fetching COVID-19 data...")
    df = pd.read_csv(url)
    df_latest = df[df['date'] == df['date'].max()]
    df_out = df_latest[["location", "iso_code", "total_cases"]]
    df_out.columns = ["Country", "Code", "Covid_Cases"]
    df_out = df_out.dropna(subset=["Covid_Cases"])
    df_out.to_csv(f"{data_dir}/covid.csv", index=False)
    print("✅ COVID data updated.")

# --------- Population: World Bank ---------
def update_population_data():
    url = "http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv"
    print("Fetching World Bank Population data...")
    r = requests.get(url)
    import zipfile, io
    z = zipfile.ZipFile(io.BytesIO(r.content))
    file_name = [f for f in z.namelist() if f.endswith('.csv') and "Metadata" not in f][0]
    df = pd.read_csv(z.open(file_name), skiprows=4)
    latest_year = df.columns[-2]
    df_out = df[["Country Name", "Country Code", latest_year]].dropna()
    df_out.columns = ["Country", "Code", "Population"]
    df_out.to_csv(f"{data_dir}/population.csv", index=False)
    print("✅ Population data updated.")

# --------- Temperature (Optional Manual) ---------
def generate_temperature_data():
    print("Generating sample average temperature data...")
    country_data = {
        "Country": ["India", "United States", "China", "Brazil", "Russia"],
        "Code": ["IND", "USA", "CHN", "BRA", "RUS"],
        "Avg_Temp_C": [24.5, 13.2, 7.8, 25.4, -5.1]
    }
    df = pd.DataFrame(country_data)
    df.to_csv(f"{data_dir}/temperature.csv", index=False)
    print("✅ Sample temperature data saved.")

if __name__ == "__main__":
    update_covid_data()
    update_population_data()
    generate_temperature_data()
    print("\n🌍 All datasets are updated in the 'data/' folder.") 
