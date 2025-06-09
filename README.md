# Assignment-for-ML

Here's a **line-by-line explanation** of your code from the file `invoice_extractor.py`:

---

### 🔹 **1. Import Libraries**

```python
import pandas as pd
import pdfplumber
import os
```

* `pandas`: To store extracted data in a structured table (DataFrame) and export it to Excel.
* `pdfplumber`: To open and extract text from PDF invoice files.
* `os`: To interact with the file system (navigate folders, get file names, etc.).

---

### 🔹 **2. Define Input and Output Paths**

```python
input_folder = "E:\Assignment for invoices"
output_excel_path = "Output/invoices_output.xlsx"
invoice_data = []
```

* `input_folder`: Location where your PDF invoice files are stored. 
* `output_excel_path`: Where the Excel file will be saved.
* `invoice_data`: A list to hold data extracted from each invoice.

---

### 🔹 **3. Function to Extract Data from Each PDF**

```python
def extract_data_from_pdf(pdf_path):
    data = {"Invoice File": os.path.basename(pdf_path)}
```

* Defines a function that takes the path of a PDF and initializes a dictionary with the file name.

---

### 🔹 **4. Extract Text from All Pages of PDF**

```python
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"
```

* Opens the PDF and reads text from each page.
* Combines all text into a single string (`text`).

---

### 🔹 **5. Extract Specific Fields from the Text**

```python
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
```

* Goes line-by-line through the text and looks for key phrases like `"Order ID"`, `"Product"`, etc.
* Extracts the value after the `:` and stores it in the `data` dictionary.

---

### 🔹 **6. Return Extracted Data**

```python
    return data
```

* Returns the dictionary containing extracted values.

---

### 🔹 **7. Loop Through All PDFs in the Input Folder**

```python
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        full_path = os.path.join(input_folder, filename)
        invoice_data.append(extract_data_from_pdf(full_path))
```

* Goes through every file in the input folder.
* If the file is a PDF, it extracts data using the function and appends it to `invoice_data`.

---

### 🔹 **8. Save Extracted Data to Excel**

```python
df = pd.DataFrame(invoice_data)
os.makedirs("Output", exist_ok=True)
df.to_excel(output_excel_path, index=False)
print("✅ Invoice data saved to:", output_excel_path)
```

* Converts the `invoice_data` list to a pandas DataFrame.
* Ensures the output folder exists using `os.makedirs`.
* Saves the DataFrame to an Excel file.
* Prints a success message.

---

### ✅ Example Output Excel

| Invoice File           | Order ID     | Order Date | Product Name                 | Seller                    | Total Amount |
| ---------------------- | ------------ | ---------- | ---------------------------- | ------------------------- | ------------ |
| amazon\_invoice\_1.pdf | AMZ123456789 | 2025-05-10 | Logitech Wireless Mouse M235 | Cloudtail India Pvt. Ltd. | Rs. 799      |

---

