from string import Template

full_template = open('./templates/template.html').read()
template = Template(full_template)

page_content = template.safe_substitute(content=open('./content/index.html').read())
open('./docs/index.html', 'w+').write(page_content)

page_content = template.safe_substitute(content=open('./content/projects.html').read())
open('./docs/projects.html', 'w+').write(page_content)

page_content = template.safe_substitute(content=open('./content/resume.html').read())
open('./docs/resume.html', 'w+').write(page_content)

page_content = template.safe_substitute(content=open('./content/blog.html').read())
open('./docs/blog.html', 'w+').write(page_content)

page_content = template.safe_substitute(content=open('./content/contact.html').read())
open('./docs/contact.html', 'w+').write(page_content)