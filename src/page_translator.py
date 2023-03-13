from libretranslatepy import LibreTranslateAPI
from path_utils import list_html_files,list_non_html_files
from googletrans import Translator
from bs4 import BeautifulSoup
import shutil
import os


class RecursiveHtmlTranslator:
    def __init__(self, root_path, translator_api ):
        self.root_path = root_path
        self.translator = LibreTranslateAPI(translator_api)

    def copy_meta_files(self,output_dir):
        non_html_files = list_non_html_files(self.root_path)
        for file in non_html_files:
            dst = file.replace(self.root_path, output_dir)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copyfile(file, dst)

    def translate_from_root_dir(self, output_dir):
        html_files = list_html_files(self.root_path)
        for i,file in enumerate(html_files):
            end_name = file.replace(self.root_path, output_dir)
            print(f"Writing: {end_name}... ({i}/{len(html_files)})")
            translated_content = self.translateHtmlFile(file)
            os.makedirs(os.path.dirname(file), exist_ok=True)
            f_out = open(end_name, "w")
            f_out.write(translated_content)
            f_out.close()

    def start(self, output_dir):
        print("Copying meta files...")
        self.copy_meta_files(output_dir)
        print("Translating html files...")
        self.translate_from_root_dir(output_dir)

    
    def translateHtmlFile(self,path):
        with (open(path)) as f:
            html_text = f.read()
            soup = BeautifulSoup(html_text, 'html.parser')
            elements = {}
            interest_items = ['br', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'i', 'a',
                              'label','span']
            for key in interest_items:
                tags = soup.findAll(key)
                for tag in tags:
                    translated = self.translator.translate(tag.string, 'en', 'hi') if tag.string else None
                    if translated:
                        # print(f"Original: {tag.string}")
                        # print(f"Translated: {translated}")
                        html_text = html_text.replace(tag.string,translated)

            f.close()
            return html_text