# pylint: disable=C0111

from aiohttp import web
import json
from mapped import process, find
import logging

# Hello
async def hello(request):
    text = "Hello World"
    return web.Response(text=text)
  
# Process url param, log it and return
# @APP.route('/post/<int:post_id>') # integer
# def show_post(post_id):
#     mapped_it = process(post_id)
#     logging.warning('Log to terminal post_id %d', post_id)
#     return 'Post %d' % mapped_it


# Process url param, log, JSON return it
# @APP.route('/api/<int:post_id>')
async def api(request):
    post_id = request.match_info.get('post_id', 0)
    foundName = await find(post_id)
    # print(foundName)
    return web.json_response({
        "name": foundName,
        "key": "value"
    })

app = web.Application()
app.router.add_get('/', hello)
app.router.add_get('/api/{post_id}', api)

web.run_app(app)
