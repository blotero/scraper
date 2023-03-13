import os

def list_html_files(startpath):
    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(startpath) for f in filenames if os.path.splitext(f)[1] == '.html']
    return result

def list_non_html_files(startpath):
    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(startpath) for f in filenames if os.path.splitext(f)[1] != '.html']
    return result