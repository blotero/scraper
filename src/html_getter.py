from bs4 import BeautifulSoup
from libretranslatepy import LibreTranslateAPI

def translateHtmlFile(path):
    path = path
    print(f"Getting strings for {path}")
    with (open(path)) as f:
        html_text = f.read()
        soup = BeautifulSoup(html_text, 'html.parser')
        elements = {}
        interest_items = ['br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'i', 'a']
        for key in interest_items:
            tags = soup.findAll(key)
            for tag in tags:
                # print(f"Original: {tags[i].string}")
                translated = translator.translate(tag.string, 'en', 'hi') if tag.string else None
                if translated:
                    print(f"Translated: {translated}")
                    html_text = html_text.replace(tag.string,translated)

        f.close()
        return html_text
