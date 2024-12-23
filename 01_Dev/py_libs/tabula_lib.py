import tabula

try:
    # # Convert PDF to Excel directly
    tabula.convert_into("2024-GCE-Ordinary-Level-Results.pdf", "output.xlsx", output_format="xlsx", pages='all') # pages='all' reads all pages. or you can specify which page like pages='1' or pages=[1,2,3]

    #Alternatively, extract to dataframe first then to excel
    dfs = tabula.read_pdf("2024-GCE-Ordinary-Level-Results.pdf", pages='all')
    for i, df in enumerate(dfs):
        df.to_excel(f"output_table_{i+1}.xlsx",index=False) #index=False to prevent index from being written to excel

    print("PDF converted to Excel successfully!")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")