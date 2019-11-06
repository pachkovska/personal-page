hold=$(cat ./content/index.html)
sed -e "s|\${content}|$(echo $hold)|" ./templates/template.html > ./docs/index.html 

hold=$(cat ./content/projects.html)
sed -e "s|\${content}|$(echo $hold)|" ./templates/template.html > ./docs/projects.html 

hold=$(cat ./content/resume.html)
sed -e "s|\${content}|$(echo $hold)|" ./templates/template.html > ./docs/resume.html 

hold=$(cat ./content/blog.html)
sed -e "s|\${content}|$(echo $hold)|" ./templates/template.html > ./docs/blog.html 

hold=$(cat ./content/contact.html)
sed -e "s|\${content}|$(echo $hold)|" ./templates/template.html > ./docs/contact.html 