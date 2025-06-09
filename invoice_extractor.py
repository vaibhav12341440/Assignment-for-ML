import pandas as pd
import pdfplumber
import os

input_folder = "E:\Assignment for invoices"
output_excel_path = "Output/invoices_output.xlsx"
invoice_data = []

def extract_data_from_pdf(pdf_path):
    data = {"Invoice File": os.path.basename(pdf_path)}
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
        for line in text.split("\n"):
            if "Order ID" in line:
                data["Order ID"] = line.split(":")[-1].strip()
            elif "Order Date" in line:
                data["Order Date"] = line.split(":")[-1].strip()
            elif "Product" in line:
                data["Product Name"] = line.split(":")[-1].strip()
            elif "Sold By" in line:
                data["Seller"] = line.split(":")[-1].strip()
            elif "Total Amount" in line:
                data["Total Amount"] = line.split(":")[-1].strip()
    return data

for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        full_path = os.path.join(input_folder, filename)
        invoice_data.append(extract_data_from_pdf(full_path))

df = pd.DataFrame(invoice_data)
os.makedirs("Output", exist_ok=True)
df.to_excel(output_excel_path, index=False)
print("✅ Invoice data saved to:", output_excel_path)
