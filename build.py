pages = [
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "Home",
    "active_page_placeholder": "{{active_home}}",
    },
    {
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "Projects",
    "active_page_placeholder": "{{active_projects}}",
    },
    {
    "filename": "content/resume.html",
    "output": "docs/resume.html",
    "title": "Resume",
    "active_page_placeholder": "{{active_resume}}",
    },
    {
    "filename": "content/blog.html",
    "output": "docs/blog.html",
    "title": "Blog",
    "active_page_placeholder": "{{active_blog}}",
    },
    {
    "filename": "content/contact.html",
    "output": "docs/contact.html",
    "title": "Contact",
    "active_page_placeholder": "{{active_contact}}"
    },
]

# function to use for reading all input files
def read_file(file):
    template = open(file).read()
    return template       

# function to use for replacement of both placeholders in HTML template
def insert_content(content_file, title, current_page):
    template = read_file('./templates/base.html')
    full_page = template.replace('{{title}}', title).replace('{{content}}',content_file).replace(current_page, 'active') 
    return full_page

# function to use for output file creation
def write_file(output_file, full_page):
    open(output_file, 'w+').write(full_page)
    return output_file

# function that iterates through list of pages, uses earlier defined functions 
# to open all input files, replace placeholders and to create output files         
def main():
    for page  in pages:
        content_file = page["filename"]
        output_file = page["output"]
        title = page["title"]
        current_page = page["active_page_placeholder"]
        replacement = insert_content(read_file(content_file), title, current_page)
        final = write_file(output_file, replacement)
    return final


if __name__ == "__main__":
    main()