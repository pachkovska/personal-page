hold=$(cat ./content/index.html)
sed -e "s|{{title}}|Home|" -e "s|{{content}}|$(echo $hold)|g" ./templates/base.html > ./docs/index.html

hold=$(cat ./content/projects.html)
sed -e "s|{{title}}|Projects|" -e "s|{{content}}|$(echo $hold)|" ./templates/base.html > ./docs/projects.html 

hold=$(cat ./content/resume.html)
sed -e "s|{{title}}|Resume|" -e "s|{{content}}|$(echo $hold)|" ./templates/base.html > ./docs/resume.html 

hold=$(cat ./content/blog.html)
sed -e "s|{{title}}|Blog|" -e "s|{{content}}|$(echo $hold)|" ./templates/base.html > ./docs/blog.html 

hold=$(cat ./content/contact.html)
sed -e "s|{{title}}|Contact|" -e "s|{{content}}|$(echo $hold)|" ./templates/base.html > ./docs/contact.html 