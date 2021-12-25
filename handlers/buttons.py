from aiogram import types
from DICTS import *

def add_buttons():
    
    markup1= types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 7)
    
    item1 = types.KeyboardButton(text = "страна")
    item2 = types.KeyboardButton(text = "тема") 
    item3 = types.KeyboardButton(text = "язык")
    item4 = types.KeyboardButton(text = "категория") 
    item5 = types.KeyboardButton(text = "подписчиков от ")
    item6 = types.KeyboardButton(text = "подписчиков до ")
    item7 = types.KeyboardButton(text = "просмотров от") 
    item8 = types.KeyboardButton(text ="просмотров до")
    item9 = types.KeyboardButton(text = "всего видео от")
    item10 = types.KeyboardButton(text = "всего видео до")
    item11 = types.KeyboardButton(text = "видео не позднее")
    item12 = types.KeyboardButton(text = "видео не ранее")
    item13 = types.KeyboardButton(text = "последнее от")
    item14 = types.KeyboardButton(text = "последнее до")    
    item15 = types.KeyboardButton(text = "ПОИСК")
    item16 = types.KeyboardButton(text = "ОТМЕНА")
    item17 = types.KeyboardButton(text = "ПРОВЕРКА")

    markup1.add(item1, item2, item3) 
    markup1.add(item4, item5, item6)    
    markup1.add(item7, item8, item9)
    markup1.add(item10, item11, item12)
    markup1.add(item13, item14, item17)
    markup1.add(item15, item16)          
    return markup1


def add_buttons2(i):
    try:
        data = eval('ru_'+i)
    except:
        data = eval(i)
    data2 =eval(i) 
    letters = 6
    num_cells=3
    markup=types.InlineKeyboardMarkup(row_width = num_cells)
    x=0
    date = list(data.keys())
    date2 = list(data2.keys())
    n = 0
    item1 =[]
    item = {}
    for x in range(len(date)): # 
        if n<num_cells:
            #print(x, data2[date2[x]], data[date[x]])
            if x  <len(date): item1.append(types.InlineKeyboardButton(data[date[x]],   callback_data=f'press#{i}#{date2[x]}'))
            n+=1
        else:
            markup.row(*item1)
            item1 = []
            n=0
    return markup

def add_buttons3():
    markup0= types.InlineKeyboardMarkup(row_width = 3)        
    item1 = types.InlineKeyboardButton("НАЗВАНИЕ КАНАЛА", callback_data=f'name_chanell')
    item2 = types.InlineKeyboardButton("КЛЮЧЕВЫЕ СЛОВА", callback_data=f'keywords')
    item3 = types.InlineKeyboardButton("ПОРПУСТИТЬ", callback_data=f'cancel')                
    markup0.add(item1, item2, item3)        
    return markup0

def add_buttons4(res):
    #print(type(res))
    #print(res)
    markup5= types.InlineKeyboardMarkup(row_width = 2)        
    item1 = types.InlineKeyboardButton("ДА", callback_data=f'yes {res}')  
    item2 = types.InlineKeyboardButton("НЕТ", callback_data=f'cancel')                
    markup5.add(item1, item2)  
    #print(72, 'ok')        
    return markup5

def add_buttons5(data, nv2=''):    
    markup=types.InlineKeyboardMarkup(row_width = 5)
    

    for key in data.keys():
        date = data[key]
        for x in range(0, len(date)):           
            if x  <len(date): 
                item1 = types.InlineKeyboardButton(nv2[key][x], callback_data=f'press#{key}#{date[x]}')
            markup.add(item1)
    return markup