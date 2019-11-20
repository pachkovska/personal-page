import glob
import os
from jinja2 import Template

content_files = glob.glob('content/*.html')

pages = []

for content_file in  content_files:
    file_name = os.path.basename(content_file)
    name_only, extention = os.path.splitext(file_name)
    pages.append({
        "filename": content_file, 
        "output": os.path.join('docs', file_name), 
        "title": name_only if file_name != 'index.html' else 'home',
    })

# Read all input files
def read_file(file):
    template = open(file).read()
    return template       

# Replace placeholders in HTML template
def insert_content(content, title):
    template_html = read_file('./templates/base.html')
    template = Template(template_html)
    full_page = template.render(
        title=title,
        content=content,
        pages=pages,
    )
    return full_page

# Create output file
def write_file(output_file, full_page):
    open(output_file, 'w+').write(full_page)
    return output_file

# Use earlier defined functions to open all input files, replace placeholders and to create output files         
def main():
    for page  in pages:
        content_file = page["filename"]
        output_file = page["output"]
        title = page["title"]
        replacement = insert_content(read_file(content_file), title)
        final = write_file(output_file, replacement)
    return final

# Create new content page template
def new():
    content_template = """<div class="conatiner p-font">
    <div class="row">

    </div>
</div>"""
    new_template = 'content/new_page_content.html'
    open(new_template, 'w+').write(content_template)
    return new_template