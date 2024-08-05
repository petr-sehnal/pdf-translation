import fitz  # PyMuPDF
import pprint
import os
import re 

def extract_text_with_formatting(pdf_path):
    document = fitz.open(pdf_path)
    pages = []
    
    for page_num in range(document.page_count):
        print("Processing page: " + str(page_num))
        page = document.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]
        page_content = []
        b=0
        for block in blocks:                        
            print("Block: " + str(b))
            b+=1
            l=0
            pprint.pprint(block)
            if "lines" in block:
                for line in block["lines"]:                    
                    print("Line: " + str(l))
                    l+=1
                    for span in line["spans"]:
                        page_content.append({
                            "text": span["text"],
                            "bbox": span["bbox"]
                        })
        pages.append(page_content)
    return pages


def extract_text_with_bounding_boxes(pdf_path):
    document = fitz.open(pdf_path)
    pages = []
    
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]
        page_content = []
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        page_content.append({
                            "text": span["text"],
                            "bbox": span["bbox"]
                        })
        pages.append(page_content)
    return pages


def draw_bounding_boxes(pdf_path, formatted_text, output_pdf_path):
    document = fitz.open(pdf_path)
    
    for page_num, page_content in enumerate(formatted_text):
        page = document.load_page(page_num)
        
        for item in page_content:
            bbox = item["bbox"]
            rect = fitz.Rect(bbox)
            # Draw the bounding box with a specified color and width
            page.draw_rect(rect, color=(1, 0, 0), width=0.5)  # Red color, adjust width as needed
    
    document.save(output_pdf_path)


def extract_text(pdf_path):
    document = fitz.open(pdf_path)
    img_tag_pattern = re.compile(r'<img\b[^>]*>', re.IGNORECASE)
    pages = []
    html = """
      <!DOCTYPE html>
      <html><head><title>converted PDF</title>
      <style>
      body {
            position: relative;
            width: 595.3pt;
            height: 841.9pt;
            border: 1px solid #ddd; /* Just for visual aid */
            margin: 20px auto;
      }
      p {
            position: relative;
            margin: 0;
            display:block;
      }
      </style>
      </head><body>"""
    
    for page_num in range(document.page_count):
        page = document.load_page(page_num)
        text = page.get_text()        
        pages.append(text)
        xhtml = page.get_text("html")
        xhtml_no_img = re.sub(img_tag_pattern, '', xhtml)
        # get rid of img tag
        #xhtml = xhtml.replace("<img src=\"data:image/png;base64,", "")
        
        html += xhtml_no_img
        print("------",page_num)
        print(xhtml_no_img)

    return pages, html



#pdf_path = "path_to_your_pdf.pdf"
#pdf_path = "data/single.pdf"
#output_pdf_path = "out/pictures.pdf"
pdf_path = "data/pictures.pdf"

draw_bounding_boxes(pdf_path, extract_text_with_bounding_boxes(pdf_path), "out/pictures.boundingbox.pdf")

exit(0)

for filename in os.listdir("data"):
    pdf_path = "data/" + filename
    output_pdf_path = "out/" + filename
    pages, xhtml = extract_text(pdf_path)

    # write xhtml to file
    with open("out/"+filename+".fitz.html", "w", encoding="utf8") as file:
      for page in pages:
            file.write(xhtml)

    with open("out/"+filename+".fitz.txt", "w", encoding="utf8") as file:
        for page in pages:
            file.write(page)

#formatted_text = extract_text_with_formatting(pdf_path)
# do this for each pdf in data folder
# for pdf in os.listdir("data"):
#     pdf_path = "data/" + pdf
#     output_pdf_path = "out/" + pdf
#     #formatted_text = extract_text_with_bounding_boxes(pdf_path)
#     #draw_bounding_boxes(pdf_path, formatted_text, output_pdf_path)
#     extract_text(pdf_path)


