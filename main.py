from quart import Quart, request
from scraper.scraper.spiders.website_crawler import run_spider
from utils import pdf_to_html, save_as_epub

VALID_EBOOKS = ["azw", "azw3", "azw4", "mobi", "txt"]

app = Quart(__name__)

@app.route("/uploads", methods=['GET', 'POST'])
async def upload_file(): # output html files are written to the pages directory
    '''
    Generates static html files for urls or pdfs, and converts ebooks to
    epubs (if neccesary), saving their outputs in the `pages` directory

    Parameters:
    - `type`: file type
    - `url`: url for an article
    - `file`: file object
    - `id`: identifier for a file
    '''
    if (request.method == 'GET'):
        if (request.form['type'] == 'url'):
            run_spider(request.form['url'])
        elif (request.form['type'] == 'pdf'):
            pdf_to_html(request.files['file'], request.form['id'])
        elif (request.form['type'] == 'epub'):
            f, id = request.files['file'], request.form['id']
            f.save(f"./pages/{id}")
        elif (request.form['type'].lower() in VALID_EBOOKS):
            f, id = request.files['file'], request.form['id']
            save_as_epub(f, id)
        else: # calibre struggles with converting other file types
            raise Exception("File not supported")
    else:
        pass