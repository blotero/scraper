import re
from bs4 import BeautifulSoup
import json
from libretranslatepy import LibreTranslateAPI

translator_api = "http://44.201.42.242:5000/"
translator = LibreTranslateAPI(translator_api)

class HtmlTextGetter:
    def __init__(self, path):
        self.path = path
    def translate(self):
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

            with(open("output.html", "w")) as fout:
                fout.write(html_text)
                fout.close()


if __name__ == '__main__':
    path = "/home/brandon/My Web Sites/classcentral/index.html"
    htg = HtmlTextGetter(path)
    htg.translate()
