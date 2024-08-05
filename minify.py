import htmlmin
import os

# read the html file
html = None
with open("out/columns.spire.html", "rb") as file:
    html = file.read()

minified = htmlmin.minify(html.decode("utf-8"), remove_empty_space=False)
#print(minified)
# write the minified html file
with open("out/columns.spire.min.html", "wb") as file:
    file.write(minified.encode("utf-8"))