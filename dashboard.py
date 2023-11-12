import pandas as pd
import streamlit as st
from helpers import excel_template

################################################################################
# Royalty Radar
st.title("Royalty Radar")

"""
Das Royalty Radar bietet einen Vergleich von Ausschüttungsdaten nach Ist und 
Soll an. Die Daten werden als Excel-Datei hochgeladen und richten sich nach dem 
Excel-Template, das über den folgenden Button heruntergeladen werden kann. Zum 
Testn kann das Template direkt, unverändert wieder hochgeladen werden.
"""

# Excel-Template Download-Button
st.download_button(
    label="Download Excel-Template",
    data=excel_template(),
    file_name="Ist-Soll.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)


################################################################################
# Datei-Upload
st.markdown("## Datei-Upload")
uploaded_file = st.file_uploader("Ziehen Sie Ihre Excel-Datei mit Ist- und Sollwerten hierher oder klicken Sie zum Hochladen", type=["xlsx"])

if uploaded_file is not None:
    try:
        # Konvertiere die Excel-Blätter Ist und Soll in DataFrames
        df_ist = pd.read_excel(uploaded_file, sheet_name='Ist')
        df_soll = pd.read_excel(uploaded_file, sheet_name='Soll')

        # Kombinieren Ist und Soll in ein DataFrame
        first_column_name = df_soll.columns[0]
        df = pd.merge(df_ist, df_soll, on=first_column_name)


        ################################################################################
        # Analyse
        st.markdown("## Analyse")
        st.write("Inhalt der hochgeladenen Excel-Datei (Ist/Soll):")
        st.dataframe(df, hide_index=True)
        
    except Exception as e:
        st.error(f"Es gab einen Fehler beim Laden der Datei: {e}")

