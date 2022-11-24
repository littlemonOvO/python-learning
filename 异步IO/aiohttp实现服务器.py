# _*_ coding: utf-8 _*_
# @Time: 2022/11/18 11:40
# @Author: lemon
# @File: aiohttp库
# @Project: learning

import asyncio

from aiohttp import web

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')


@routes.get('/hello/{name}')
async def hello(request):
    await asyncio.sleep(0.5)
    text = f'<h1>Hello, {request.match_info["name"]}</h1>'
    return web.Response(body=text.encode('utf-8'), content_type='text/html')


app = web.Application()
app.add_routes(routes)
web.run_app(app, host='127.0.0.1', port=8000)
