import re
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


class HtmlTextGetter:
    def __init__(self, path):
        self.path = path
    def get_strings(self):
        print(f"Getting strings for {path}")
        parser = MyHTMLParser()
        with (open(path)) as f:
            html_content = f.read()
            parser.feed(html_content)
            
        

if __name__ == '__main__':
    path = "/home/brandon/My Web Sites/classcentral/index.html"
    htg = HtmlTextGetter(path)
    res = htg.get_strings()
    print(res)


    
