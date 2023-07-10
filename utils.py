import fitz
import os

def pdf_to_html(file, id):
    doc = fitz.open(file)
    for i, page in enumerate(doc):
        text = page.get_text("html")
        with open(f"./pages/{id}/page-{i}.html", "w") as fp:
            fp.write(text)
    doc.close()

def save_as_epub(file, id, extension):
    input_path = f"./pages/{id}.{extension}"
    file.save(input_path)
    os.system(f"ebook-convert {input_path} ./pages/{id}.epub")
    os.remove(input_path)