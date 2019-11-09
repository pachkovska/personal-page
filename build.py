from string import Template

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

def main():

    full_template = open('./templates/template.html').read()
    template = Template(full_template)

    for page in pages:
        content_file = page["filename"]
        output_file = page["output"]
        page_content = template.safe_substitute(content=open(content_file).read())
        open(output_file, 'w+').write(page_content)

if __name__ == "__main__":
    main()