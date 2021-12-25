from config import *
from create_bot import dp
from aiogram.utils import executor
from sys import path
from os import getcwd
path.insert(1, getcwd())
path.insert(1, getcwd()+'/handlers')
#from handlers import client, admin, other
#from handlers.client import register_handlers_client as reg, register_callback_client as call
# from handlers.admin import 
# from handlers.other import 
from handlers import client

reg = client.register_handlers_client
call =client.register_callback_client
   


async def on_startup(_):
    print('bot begin work online')


reg(dp)
call(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True, on_startup=on_startup)

