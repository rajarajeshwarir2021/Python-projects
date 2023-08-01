import inspect

import justpy as jp
from webapp import page
from webapp.about import About
from webapp.dictionary import Dictionary
from webapp.home import Home

imports = list(globals().values())

for obj in imports:
    if inspect.isclass(obj):
        if issubclass(obj, page.Page) and obj is not page.Page:
            jp.Route(obj.path, obj.serve)

jp.justpy(port=8001)