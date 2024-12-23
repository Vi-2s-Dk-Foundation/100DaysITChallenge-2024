import PyPDF2

def print_first_10_lines_pypdf2(pdf_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            lines = text.splitlines()
            for i in range(min(10, len(lines))):  # Print up to 10 lines
                print(lines[i])
            return "Printed first 10 lines."

    except FileNotFoundError:
        return "File not found."
    except PyPDF2.errors.PdfReadError:
        return "Error reading PDF. It might be corrupted or encrypted."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

result = print_first_10_lines_pypdf2("2024-GCE-Ordinary-Level-Results.pdf")
print(result)