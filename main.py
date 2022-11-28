from faker import Faker
from aiohttp import web
import os
'''main classes'''
fake = Faker()
app = web.Application()
'''make an asynchronous function and pass fake user parameters'''
async def fake_user(request):
    data = {'name':fake.name(),'email':fake.email()}
    #json
    return web.json_response(data)
'''we transfer host data to the router (specify your path) or if you have your own host, then specify it'''
app.add_routes([web.get(f'{os.getcwd()}',fake_user)])


#main activate
if __name__ == '__main__':
    web.run_app(app)



