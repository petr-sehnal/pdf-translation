from spire.pdf import PdfDocument, FileFormat
import os

# Set conversion options
#convert_options = doc.convert_options
#convert_options.set_pdf_to_html_options(True, True, 1, True)
#SetPdfToHtmlParameter(True, True, 1, True)

# Save the PDF document to HTML format

# layout_format = HtmlLayoutFormat()
# layout_format.fit_to_page_width = True
# layout_format.load_image_type = "All"
# layout_format.load_css_type = "All"
# layout_format.load_js_type = "All"


for filename in os.listdir("data"):
      pdf_path = "data/" + filename
      output_path = "out/" + filename+".spire.html"
      # Create a PdfDocument object
      print(pdf_path + " -> " + output_path)
      doc = PdfDocument()
      convertOptions = doc.ConvertOptions

      # useEmbeddedSvg (bool): Indicates whether to embed SVG in the HTML file.
      # useEmbeddedImg (bool): Indicates whether to embed images in the HTML file. (This option only works when useEmbeddedSvg is set to False).
      # maxPageOneFile (bool): Specifies the maximum number of pages contained per HTML file. (This option only works when useEmbeddedSvg is set to False.)
      # useHighQualityEmbeddedSvg (bool): Indicates whether to use high-quality embedded SVG in the HTML file. (This option works when useEmbeddedSvg is set to True).

      #convertOptions.SetPdfToHtmlOptions(True, True, 1, True)
      #convertOptions.SetPdfToHtmlOptions(False, False, 1, False)
      # convert_options = doc.convert_options
      # convert_options.is_embedded_all_fonts = True
      # convert_options.is_embedded_font = True
      # convert_options.is_embedded_image = True
      # convert_options.is_embedded_javascript = True
      # convert_options.is_hidden_text_layer = False

      # convert_options.is_precise_positioning = True

      # Load a PDF document
      doc.LoadFromFile(pdf_path)
      doc.SaveToFile(output_path, FileFormat.HTML)



# Dispose resources
#doc.dispose()