import fitz
import os
import subprocess

def save_file(file, name, input_type):
    file.save(f"./pages/{name}.{input_type}")

def pdf_to_html(file, name):
    doc = fitz.open(file)
    os.mkdir(f"./pages/{name}.pdf")
    for i, page in enumerate(doc):
        text = page.get_text("html")
        with open(f"./pages/{id}/page-{i}.html", "w") as fp:
            fp.write(text)
    doc.close()

def convert_ebook(file, name, input_type, output_type):
    input_path = f"./pages/{name}.{input_type}"
    file.save(input_path)

    # returns a CalledProcessError if there's a problem
    subprocess.run(['ebook-convert', input_path, f'./pages/{name}.{output_type}'], shell=True, check=True)
    subprocess.run(['rm', input_path], shell=True, check=True)