from IPython.display import display, HTML
import os


fname = os.path.join(os.path.dirname(__file__), 'tutorial.css')

with open(fname, 'r') as f:
    style = f.read()
html = '<style>\n{style}\n</style>'.format(style=style)
display(HTML(html))
