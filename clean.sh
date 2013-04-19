find ./ -name ".DS_Store" -depth -exec rm {} \; -exec echo {} \;
find ./ -name "*.pyc" -depth -exec rm {} \; -exec echo {} \;