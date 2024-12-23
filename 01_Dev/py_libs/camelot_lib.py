import camelot

try:
    # Extract all the tables in the PDF
    tables = camelot.read_pdf("2024-GCE-Ordinary-Level-Results.pdf", pages="1-end") # pages='1-end' reads all pages. or you can specify which page like pages='1' or pages='1,3,5'

    # Print the number of tables extracted
    print(f"Total Tables Extracted: {tables.n}")

    # Export each table to an Excel file
    for i in range(tables.n):
        tables[i].to_excel(f"camelot_table_{i+1}.xlsx")

    print("PDF converted to Excel successfully!")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")