from page_translator import RecursiveHtmlTranslator
import translatehtml
import argostranslate.package, argostranslate.translate

custom_html_trans = True
if __name__ == '__main__':
    page_copy_path = "/home/brandon/My Web Sites/classcentral"
    translator_public_ip = "44.201.42.242"
    app_port = 5000
    translator_api = f"http://{translator_public_ip}:{app_port}"
    rt = RecursiveHtmlTranslator(page_copy_path, translator_api)
    output_dir = "/home/brandon/My Web Sites/python_creations"
    rt.start(output_dir)
