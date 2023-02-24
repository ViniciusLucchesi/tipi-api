import os
import json
import pathlib
from scrapy import *
from robyn import Robyn
from robyn.robyn import Response
from robyn.templating import JinjaTemplate

app = Robyn(__file__)

current_file_path = pathlib.Path(__file__).parent.resolve()
jinja_template = JinjaTemplate(os.path.join(current_file_path, "templates"))


# Templates
@app.get('/')
def sync_template_render_data():
    context = load_pickle()
    data = json.loads(context.to_json(orient='records', force_ascii=False))
    template = jinja_template.render_template(template_name='index.html', data=data)
    return Response(200, {"Content-Type":"text/html; charset=urf-8"}, template)


# API routes
@app.get('/api/ncm/all')
def sync_ncm_all():
    context = load_pickle()
    resp = json.loads(context.to_json(orient='records', force_ascii=False))
    return json.dumps(resp, indent=4)


@app.get('/api/ncm/:search')
def sync_ncm_search(request):
    search = request['params']['search']
    context = load_pickle()
    search = search_ncm(context, search)
    resp = json.loads(search.to_json(orient='records', force_ascii=False))
    return json.dumps(resp, indent=4)




if __name__ == "__main__":
    app.add_request_header("server", "robyn")
    app.start(port=6500)