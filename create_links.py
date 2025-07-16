from sys import argv

html = '<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="X-UA-Compatible" content="ie=edge> <title>climate docs</title></head> <body>\n'


for each in argv[1:]:
    if each.endswith('.html'):
        t = each[:-5]
        html += f'<a href="{each}">{t}</a>\n'

html += "</body></html>"
with open('index.html', 'w') as f:
    f.write(html)

