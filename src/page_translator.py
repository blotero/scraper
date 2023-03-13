from libretranslatepy import LibreTranslateAPI
from path_utils import list_html_files,list_non_html_files
from googletrans import Translator
import shutil
import os


class RecursiveHtmlTranslator:
    def __init__(self, root_path, translator_api, type):
        self.root_path = root_path
        self.translator = LibreTranslateAPI(translator_api) if type == 'libre' else Translator()
        self.type = type

    def copy_meta_files(self,output_dir):
        non_html_files = list_non_html_files(self.root_path)
        for file in non_html_files:
            dst = file.replace(self.root_path, output_dir)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(file, dst)



    def start(self, output_dir):
        print("Copying meta files...")
        self.copy_meta_files(output_dir)
        print("Copying html files...")
        html_files = list_html_files(self.root_path)
        for file in html_files:
            with open(file) as f:
                print(f"Translating: {file} with {self.type}...")
                contentlines= f.readlines()

                for i,content in enumerate(contentlines):
                    if self.type == 'libre':
                        translated_content = self.translator.translate(content, 'en', 'hi')
                    
                    if self.type == 'google':
                        translated_content = self.translator.translate(content, src='en', dest='hi')

                    end_name = file.replace(self.root_path, output_dir)
                    print(f"Writing: {end_name} (line {i} of {len(content)})...")

                    f_out = open(end_name, "a")
                    f_out.write(translated_content)
                    f_out.close()

    
    def get_strings(self,html_text ):
        print(f"Getting strings for {path}")
        soup = BeautifulSoup(html_text, 'html.parser')
        elements = {}
        interest_items = ['br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'i', 'a']
        for key in interest_items:
            elements[key] = soup.find_all(key)
        self.elements = elements

    def translate(self):
        for key,value_list in self.elements.items():
            print(f"Translating items from {key}...")
            for value in value_list:
                print(f"Original: {value}")
                translated = translator.translate(value, 'en', 'hi')
                print(f"Translated: {translated}")

                    