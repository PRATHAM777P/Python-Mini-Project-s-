# 🌍 ChoroplethMapper

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue?logo=python)](https://www.python.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Maps-orange?logo=plotly)](https://plotly.com/python/)

> **ChoroplethMapper** is a Python project to visualize real-world datasets on a world map using beautiful, interactive choropleth maps built with Plotly. Instantly explore global data like population, COVID-19 cases, and more!

---

## 🚀 Features
- 📊 **Dynamic dataset loading** (Population, COVID-19, Temperature)
- 🌐 **Interactive choropleth maps** with Plotly
- 🖱️ **Hover tooltips** for country-level insights
- 🔄 **Auto-update datasets** with a single script
- 🧩 **Easily expandable** to more datasets

---

## 📦 Project Structure
```
ChoroplethMapper/
├── data/
│   ├── population.csv
│   ├── covid.csv
│   └── temperature.csv
├── choropleth_mapper.py
├── update_data.py
├── README.md
└── .gitignore
```

---

## 🛠️ Requirements
```bash
pip install pandas plotly requests
```

## 📂 Sample Datasets
**population.csv**
```
Country,Code,Population
India,IND,1400000000
United States,USA,331000000
China,CHN,1440000000
Brazil,BRA,213000000
Russia,RUS,146000000
```
**covid.csv**
```
Country,Code,Covid_Cases
India,IND,45000000
United States,USA,102000000
China,CHN,9800000
Brazil,BRA,37000000
Russia,RUS,22000000
```
**temperature.csv**
```
Country,Code,Avg_Temp_C
India,IND,24.5
United States,USA,13.2
China,CHN,7.8
Brazil,BRA,25.4
Russia,RUS,-5.1
```

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License
Apache-2.0 license
