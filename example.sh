hold=$(cat ./templates/bottom.html)
sed -e "s|\${content}|$(echo $hold)|g" ./templates/top.html > new_html.html