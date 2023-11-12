def excel_template():
    import pandas as pd
    from io import BytesIO

    # Erstellen von Beispieldaten
    df_ist  = pd.DataFrame({'Sparte': ['A', 'B', 'C', 'D', 'E', 'F', 'G'] , 'Tantieme Ist': [1, 1, 2, 3, 4, 8, 13]})
    df_soll = pd.DataFrame({'Sparte': ['A', 'B', 'C', 'D', 'E', 'F', 'G'] , 'Tantieme Soll': [1, 1, 2, 3, 5, 8, 13]})

    # Erstellen einer Excel-Datei mit zwei Tabellenblättern
    to_excel = BytesIO()
    with pd.ExcelWriter(to_excel, engine='xlsxwriter') as writer:
        df_ist.to_excel(writer, sheet_name='Ist', index=False)
        df_soll.to_excel(writer, sheet_name='Soll', index=False)

    # Zurücksetzen des Pointers
    to_excel.seek(0)

    return to_excel
