# import PyPDF2
# import re

# def count_occurrences_between_markers(pdf_path, start_marker="cent", end_marker="regis"):
#     try:
#         with open(pdf_path, 'rb') as pdf_file:
#             pdf_reader = PyPDF2.PdfReader(pdf_file)
#             all_text = ""
#             for page in pdf_reader.pages:
#                 all_text += page.extract_text()

#             pattern = re.compile(rf"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", re.IGNORECASE | re.DOTALL)
#             matches = pattern.findall(all_text)
#             return len(matches)

#     except FileNotFoundError:
#         return "File not found."
#     except PyPDF2.errors.PdfReadError:
#         return "Error reading PDF. It might be corrupted or encrypted."
#     except Exception as e:
#         return f"An unexpected error occurred: {e}"

# num_occurrences = count_occurrences_between_markers("2024-GCE-Ordinary-Level-Results.pdf")

# if isinstance(num_occurrences, int):
#     print(f"Number of occurrences between 'cent' and 'regis': {num_occurrences}")
# elif isinstance(num_occurrences, str):
#     print(num_occurrences)  # Print the error message
# else:
#     print("An unexpected error occurred.")

import PyPDF2
import re
import csv

def extract_and_save_matches_to_csv(pdf_path, start_marker="cent", end_marker="regis", output_csv="output.csv"):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            all_text = ""
            for page in pdf_reader.pages:
                all_text += page.extract_text()

            pattern = re.compile(rf"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", re.IGNORECASE | re.DOTALL)
            matches = pattern.findall(all_text)

            with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Extracted Text"])  # Write header row
                for match in matches:
                    writer.writerow([match.strip()])  # Write each match, stripping whitespace

            return f"Matches saved to {output_csv}"

    except FileNotFoundError:
        return "File not found."
    except PyPDF2.errors.PdfReadError:
        return "Error reading PDF. It might be corrupted or encrypted."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

result = extract_and_save_matches_to_csv("2024-GCE-Ordinary-Level-Results.pdf")
print(result)

# Example with custom markers and output file name
result2 = extract_and_save_matches_to_csv("your_pdf_file.pdf", start_marker="start_phrase", end_marker="end_phrase", output_csv="custom_output.csv")
print(result2)