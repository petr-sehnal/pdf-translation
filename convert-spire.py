from spire.pdf import PdfDocument, FileFormat
import os

# Set conversion options
#convert_options = doc.convert_options
#convert_options.set_pdf_to_html_options(True, True, 1, True)
#SetPdfToHtmlParameter(True, True, 1, True)

# Save the PDF document to HTML format


for filename in os.listdir("data"):
    pdf_path = "data/" + filename
    output_path = "out/" + filename+".html"
    # Create a PdfDocument object
    print(pdf_path + " -> " + output_path)
    doc = PdfDocument()
    # Load a PDF document
    doc.LoadFromFile(pdf_path)
    doc.SaveToFile(output_path, FileFormat.HTML)



# Dispose resources
#doc.dispose()