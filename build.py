pages = [
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "Home",
    },
    {
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "Projects",
    },
    {
    "filename": "content/resume.html",
    "output": "docs/resume.html",
    "title": "Resume",
    },
    {
    "filename": "content/blog.html",
    "output": "docs/blog.html",
    "title": "Blog",
    },
    {
    "filename": "content/contact.html",
    "output": "docs/contact.html",
    "title": "Contact",
    },
]

def read_file(file):
    template = open(file).read()
    return template       

def insert_content(content_file, title):
    template = read_file('./templates/base.html')
    full_page = template.replace('{{title}}', title).replace('{{content}}',content_file)
    return full_page

def write_file(output_file, full_page):
    open(output_file, 'w+').write(full_page)
    return output_file
        
def main():
    for page  in pages:
        content_file = page["filename"]
        output_file = page["output"]
        title = page["title"]
        replacement = insert_content(read_file(content_file), title)
        final = write_file(output_file, replacement)
    return final


if __name__ == "__main__":
    main()