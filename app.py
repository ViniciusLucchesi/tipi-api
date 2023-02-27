import json
from scrapy import *
from robyn import Robyn

app = Robyn(__file__)


# API routes
@app.get('/api/ncm/all')
def sync_ncm_all():
    context = ManageData().load_data()
    resp = json.loads(context.to_json(orient='records', force_ascii=False))
    return json.dumps(resp, indent=4)


@app.get('/api/ncm/:search')
def sync_ncm_search(request):
    search = request['params']['search']
    context = ManageData().load_data()
    search = ManageData().search_ncm(context, search)
    resp = json.loads(search.to_json(orient='records', force_ascii=False))    
    return json.dumps(resp, indent=4)
    




if __name__ == "__main__":
    app.add_request_header("server", "robyn")
    app.start(port=6500)