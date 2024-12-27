import PyPDF2

def extract_center_lines(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            all_lines = []
            all_lines1 = []
            for page in pdf_reader.pages:
                text = page.extract_text()
                lines = text.splitlines()
                for line in lines:
                    all_lines1.append(line.strip())  # Add stripped line - ALL
                    if line.lower().startswith("centre no :"):  # Case-insensitive check
                        all_lines.append(line.strip())  # Add stripped line - Centers ONLY
            return all_lines, all_lines1

    except FileNotFoundError:
        return "File not found."
    except PyPDF2.errors.PdfReadError:
        return "Error reading PDF. It might be corrupted or encrypted."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

center_lines, records = extract_center_lines("2024-GCE-Ordinary-Level-Results.pdf")


if isinstance(center_lines, list):
    if center_lines: #check if the list is not empty
        print("Found Lines starting with 'centre no :':")
        # for line in center_lines:
        #     print(line)
    else:
        print("No lines starting with 'center no :' found in the PDF.")
elif isinstance(center_lines, str):
    print(center_lines) #print the error message
else:
    print("An unexpected error occurred.")
print(f"Number of GCE Centers {len(center_lines)}")
print(f"Number of Lines in PDF {len(records)}")