from subprocess import CalledProcessError
from quart import Quart, request
from scraper.scraper.spiders.website_crawler import run_spider
from utils import save_file, pdf_to_html, convert_ebook

INPUT_EBOOK_TYPES = ["azw", "azw3", "azw4", "azw8", "cb7", "cbc",
        "cbr", "cbz", "chm", "djvu", "docx", "doc", "epub", "fb2",
        "fbz", "html", "htmlz", "kfx", "kfx-zip", "kpf", "lit", "lrf",
        "mobi", "odt", "opf", "pdb", "pml", "prc", "rb", "rtf", "snb",
        "tcr", "txt", "txtz"]

OUTPUT_EBOOK_TYPES = [ "azw3", "docx", "epub", "fb2", "htmlz",
        "kfx", "lit", "lrf", "mobi", "oeb", "pdb", "pdf", "pmlz",
        "rb", "rtf", "snb", "tcr", "txt", "txtz", "zip"]

app = Quart(__name__)

@app.route("/article", methods=['POST'])
async def upload_article():
    '''
    Scrapes and converts a website into a single, static HTML file
    w/o exploring outgoing links.

    url: url for a website
    '''
    try:
        url = request.form['url']
        run_spider(url)
    except KeyError:
        return {"status": 400, "error": "must provide a url"}
    except:
        return {"status": 500, "error": "unexpected error while scraping url or saving output"}
    
@app.route("/ebook", methods=['POST'])
async def upload_ebook():
    '''
    Saves an ebook, converting it into any file type listed in 
    `OUTPUT_EBOOK_TYPES`

    file: Python file object
    name: name of the output file
    input_type: input file type
    output_type: output file type
    '''
    try:
        f, name, input_type, output_type = \
            request.files['file'], request.form['name'], request.form['input_type'], request.form['output_type']
        
        if (input_type not in INPUT_EBOOK_TYPES or output_type not in OUTPUT_EBOOK_TYPES):
            return {"status": 400, "error": "invalid input or output file type"}
        
        if (input_type == output_type):
            save_file(f, name, input_type)
        elif (input_type == 'pdf' and output_type == 'html'):
            pdf_to_html(f, name)
        else:
            convert_ebook(f, name, input_type, output_type)
        
        return {"status": 200}
    except KeyError:
        return {"status": 400, "error": "must provide a file, id, and ebook type"}
    except CalledProcessError:
        return {"status": 500, "error": "error occured while converting"}
    except:
        return {"status": 500, "error": "unexpected internal error"}

if __name__ == "__main__":
    app.run()