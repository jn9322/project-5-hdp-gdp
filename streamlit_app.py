import streamlit as st
import pandas as pd
import math 
from pathlib import Path

# Nastaveni nayvu a ikonky, ktera se zobrazuje v zalozce prohlizece 
st.set_page_config(
    page_title="HDP dashboard",
    page_icon=":earth_americas:"
)

# Definovani funkci

# Get data 
# Tady jsem vic vycistil originalni dataset, jelikoz ten puvodni zobrazoval "Unnamed:68" jako posledni sloupec pri nacteni streamlitem 
@st.cache_data(ttl="1d")
def get_gdp_data():

    # Tady ukazka, ze nemusim jit rovnou pres klasicky read CSV (nacitani z disku), muzi is pres HTTP endpoint pouzivajic Path
    DATA_FILENAME = Path(__file__).parent/'Data/data_gdp_copy_zkousim_vylepsit_dataset.csv'
    raw_gdp_df = pd.read_csv(DATA_FILENAME)

    MIN_YEAR = 1960
    MAX_YEAR = 2023

    #Data maji spoustu slopcu jako: 
    #  Nazev zeme
    #  Kod zeme
    #  a Spoustu, co me nezajima !!!!

    # Ja chci toto:
    # Nazev zeme
    # Kod zeme
    # Rok
    # HDP

    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        # tady to +1 znamená abychom dosli na rok 2023, ze kdyz tam nemam + 1 tak tabulka je jenom 2022
        [str(x) for x in range(MIN_YEAR,MAX_YEAR + 1)],
        "Year",
        "GDP"
    )

    st.write(gdp_df)

    #Převod Year ze stringu na date - povšimnout si, že nyní Streamlit zobrazuje 1,960 místo 1960, což je vedlejší efekt, toho, že to mám číslo -> dává oddělovač
    gdp_df["Year"] = pd.to_numeric(gdp_df["Year"])
    st.write(gdp_df)
    
get_gdp_data()



st.write("done")
