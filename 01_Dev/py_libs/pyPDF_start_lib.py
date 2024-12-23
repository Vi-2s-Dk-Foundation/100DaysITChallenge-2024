import PyPDF2

def extract_center_lines(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            all_lines = []
            for page in pdf_reader.pages:
                text = page.extract_text()
                lines = text.splitlines()
                for line in lines:
                    if line.lower().startswith("centre no"):  # Case-insensitive check
                        all_lines.append(line.strip())  # Add stripped line
            return all_lines

    except FileNotFoundError:
        return "File not found."
    except PyPDF2.errors.PdfReadError:
        return "Error reading PDF. It might be corrupted or encrypted."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

center_lines = extract_center_lines("2024-GCE-Ordinary-Level-Results.pdf")

if isinstance(center_lines, list):
    if center_lines: #check if the list is not empty
        print("Lines starting with 'center':")
        for line in center_lines:
            print(line)
    else:
        print("No lines starting with 'center' found in the PDF.")
elif isinstance(center_lines, str):
    print(center_lines) #print the error message
else:
    print("An unexpected error occurred.")