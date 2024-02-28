import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def import_dataset():
    df_hour = pd.read_csv('data/hour.csv')
    df_day = pd.read_csv('data/day.csv')
    return df_hour, df_day

def generate_data(df_hour, df_day):
    # no 1
    df_day_1 = df_day[['yr', 'mnth', 'cnt']]
    df_day_1['yr'] = df_day_1['yr'].replace({0: 2011, 1: 2012})
    avg_count = df_day_1.groupby(['yr', 'mnth'])['cnt'].mean()
    avg_count.index = avg_count.index.map('{0[0]}-{0[1]}'.format)

    # no 2
    df_day_2 = df_day[['temp', 'cnt']]
    df_day_2['temp'] = df_day_2['temp'] * 41
    corr = df_day_2.corr()

    # no 3
    df_hour_3 = df_hour[['hr', 'cnt']]
    avg_cnt_hr = df_hour_3.groupby(['hr'])['cnt'].mean()
    sorted_avg_cnt_hr = avg_cnt_hr.sort_values()

    return avg_count, corr, sorted_avg_cnt_hr

df_hour, df_day = import_dataset()
no1, no2, no3 = generate_data(df_hour, df_day)

st.title('Analisis Data Penyewaan Sepeda')
st.caption('oleh Jaycent Gunawan Ongris')

tab0, tab1, tab2, tab3 = st.tabs(["Dataset", "Pertanyaan 1", "Pertanyaan 2", "Pertanyaan 3"])

with tab0:
    st.header("Gambaran Dataset")
    st.write("Terdapat dua dataset yang akan digunakan, yaitu dataset hari dan jam. Berikut adalah atribut-atribut yang digunakan pada dataset.")
    st.write(
        """
        - **instant**: record index
- **dteday**: date
- **season**: season (1\: springer, 2\: summer, 3\: fall, 4\: winter)
- **yr**: year (0: 2011, 1:2012)
- **mnth**: month (1 to 12)
- **hr**: hour (0 to 23)
- **holiday**: weather day is holiday or not (extracted from [holiday schedule](http://dchr.dc.gov/page/holiday-schedule))
- **weekday**: day of the week
- **workingday**: if day is neither weekend nor holiday is 1, otherwise is 0.
- **weathersit**:
  - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
  - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
  - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
  - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- **temp**: Normalized temperature in Celsius. The values are divided to 41 (max)
- **atemp**: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
- **hum**: Normalized humidity. The values are divided to 100 (max)
- **windspeed**: Normalized wind speed. The values are divided to 67 (max)
- **casual**: count of casual users
- **registered**: count of registered users
- **cnt**: count of total rental bikes including both casual and registered
        """
    )
    st.write("Berikut adalah cuplikan kedua dataset.")
    col1, col2 = st.columns(2)

    with col1:
        st.header("Dataset Hari")
        st.write(df_day.head(10))

    with col2: 
        st.header("Dataset Jam")
        st.write(df_hour.head(10))

def plot_line_graph(data):
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data.values, marker='o', linestyle='-')
    plt.xlabel('Tahun-Bulan')
    plt.ylabel('Rata-Rata Penyewaan')
    plt.title('Tren Rata-Rata Penyewaan per Bulan')
    plt.xticks(rotation=45)
    return plt

def plot_scatter_plot(data):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(data['temp'], data['cnt'])
    ax.set_xlabel('Temperatur')
    ax.set_ylabel('Jumlah Penyewa')
    ax.set_title('Hubungan Jumlah Penyewa dan Temperatur')
    return fig

def plot_heatmap(data):
    plt.figure(figsize=(8, 4))
    sns.heatmap(data, annot=True)
    plt.title('Heatmap Korelasi Temperatur dengan Jumlah Penyewa')
    return plt

def plot_bar_chart(data):
    fig, ax = plt.subplots(figsize=(10, 8))
    data.plot(kind='barh', ax=ax)
    ax.set_xlabel('Rata-Rata Penyewa')
    ax.set_ylabel('Jam')
    ax.set_title('Jumlah Rata-Rata Penyewa')
    return fig

with tab1:
    st.header("Tren Rata-Rata Jumlah Penyewa Sepeda per Hari")
    st.write("Bagaimana tren rata-rata jumlah pelanggan per hari yang menyewa sepeda termasuk casual users dan registered users per bulan dari tahun 2011 hingga tahun 2012?")
    st.pyplot(plot_line_graph(no1))
    st.write("Dapat dilihat bahwa tren rata-rata jumlah penyewa sepeda per bulan semakin meningkat hingga mencapai puncaknya pada sekitar pertengahan bulan (bulan 6 pada 2011 dan bulan 9 pada 2012). Setelah melalui puncak tersebut, tren rata-rata penyewaan sepeda menurun di sisa tahun dan kemudian meningkat lagi di awal tahun. Pola tersebut dapat dilihat untuk tahun 2011 dan 2012.")

with tab2:
    st.header("Hubungan Temperatur dengan Jumlah Penyewa Sepeda")
    st.write("Bagaimana hubungan temperatur dengan jumlah total penyewa sepeda per hari pada tahun 2011?")
    st.pyplot(plot_scatter_plot(df_day))
    st.pyplot(plot_heatmap(no2))
    st.write("Dapat dilihat bahwa antara temperatur dan jumlah penyewa sepeda per harinya memiliki korelasi yang cukup kuat, yaitu sekitar 0.63. Hal ini juga dapat diobservasi pada scatterplot, di mana terdapat adanya kecenderungan linear dari persebaran kedua variabel tersebut.")

with tab3:
    st.header("Waktu Puncak Rata-Rata Penyewaan Sepeda per Hari")
    st.write("Pada jam berapa sajakah rata-rata penyewaan sepeda mencapai puncaknya?")
    st.pyplot(plot_bar_chart(no3))
    st.write("Dapat dilihat bahwa jumlah rata-rata penyewa sepeda mencapai puncaknya pada pukul 17.00, yang kemudian diikuti oleh pukul 18.00 dan 08.00.")