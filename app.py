import os
import pathlib
from scrapy import *
from robyn import Robyn
from robyn.robyn import Response
from robyn.templating import JinjaTemplate

app = Robyn(__file__)

current_file_path = pathlib.Path(__file__).parent.resolve()
jinja_template = JinjaTemplate(os.path.join(current_file_path, "templates"))



@app.get('/')
def sync_template_render_data():
    context = get_valid_tipi_data()
    data = json.loads(context.to_json(orient='records', force_ascii=False))
    template = jinja_template.render_template(template_name='index.html', data=data)
    return Response(200, {"Content-Type":"text/html; charset=urf-8"}, template)


@app.get('/api/all/ncm/:search')
def sync_ncm_search(request):
    search = request['params']['search']
    context = get_valid_tipi_data()
    search = search_ncm(context, search, identical=False)
    data = json.loads(search.to_json(orient='records', force_ascii=False))
    template = jinja_template.render_template(template_name='index.html', data=data)
    return Response(200, {"Content-Type":"text/html; charset=urf-8"}, template)


@app.get('/api/ncm/:search')
def sync_ncm_search(request):
    search = request['params']['search']
    context = get_valid_tipi_data()
    search = search_ncm(context, search)
    data = json.loads(search.to_json(orient='records', force_ascii=False))
    template = jinja_template.render_template(template_name='index.html', data=data)
    return Response(200, {"Content-Type":"text/html; charset=urf-8"}, template)




if __name__ == "__main__":
    app.add_request_header("server", "robyn")
    app.start(port=65000)