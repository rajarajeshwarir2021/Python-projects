import definition
import json
import justpy as jp


class Api:

    @classmethod
    def serve(cls, req):
        wp = jp.WebPage()
        word = req.query_params.get('w')
        defined = definition.Definition(word).get()
        response = {
            "word": word,
            "definition": defined
        }
        wp.html = json.dumps(response)

        return wp