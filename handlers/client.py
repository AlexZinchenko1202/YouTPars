#from DICTS import *
from buttons import *
#from funcs import *
from aiogram import types, Dispatcher
from create_bot import dp, bot

from string import punctuation as pnt
import json, os
from funcs import w



#print(dir())
#@dp.message_handler()
async def send_mess(message:types.Message):
    global Temp, query1, RU2


    #print('text')
    #print(message.text)
    colection = [
        "category", 
        "topics", 
         "lang", 
         "country", 
         "ru_category", 
         "ru_topics", 
         "ru_lang", 
         "ru_country", 
         "creation_date_min", 
         "creation_date_max", 
         "subscribers_min", 
         "subscribers_max", 
         "total_views_min", 
         "total_views_max", 
         "total_videos_min", 
         "total_videos_max", 
         "lastest_video_min", 
         "lastest_video_max"]
    all_values = [i2 for i in colection for i2 in list(eval(i).values())]    
         
    new_vars ={}    
    #NOT(message.text, rus_words)
    params ={'язык':'lang', 'тема':'topics','страна':'country','категория':'category','подписчиков от':'subscribers_min',
        "подписчиков до": 'subscribers_max', 'просмотров от':'total_views_min','просмотров до':'total_views_max',
        'всего видео от':'total_videos_min','всего видео до':'total_videos_max','видео не позднее':'creation_date_min',
        'видео не ранее':'creation_date_max', 'последнее от':'lastest_video_min', 'последнее до':'lastest_video_max'}

    #print(494, message)
    if message.text=="ОТМЕНА": 
        await bot.send_message(message.from_user.id, 'Отмена операции')   
        que = [(k, []) if isinstance(v, list) else (k,v) for k, v in query1.items()]
        # query1 ={k:v for (k, v) in que}
        # print(que)           
        query1 =query.copy()
        print(query1)

    elif message.text=="ПРОВЕРКА": 
        #print(s_tr)
        #print('\n'.join([f"{RU[q]} \n{'\n'.join(query1[q])}\n\n" for q, v in list(query1.items()) if v!='' ]))
        #print('QUERY\n', '\n'.join([f'{q} = {v}' for q, v in list(query1.items()) if v!='']))
        RU2 = {k.strip(): v for k, v in RU2.items()}
        # text = '\n'.join([RU[q]+'\n'+',\t'.join([RU2[e.strip()].capitalize() if e in RU2.keys() else e for e in query1[q]]) \
        #     if isinstance(query1[q], list) and  query1[q]!=[] and  query1[q]!='' else query1[q] \
        #     for q in list(query1.keys())])
        text = []
        print(query1)
        for q in query1.keys():
            text.append(RU[q])
            if isinstance(query1[q], list) and  query1[q]!=[] and  query1[q]!='':
                t=[]
                for e in query1[q]:                    
                    if e in RU2.keys():
                        t.append(RU2[e.strip()].capitalize())
                    else:
                        t.append(e) 
                text.append(',\t'.join(t))
            else:
                text.append(query1[q])                    
        text = '\n'.join(['\n'.join(text[text.index(t)-1:][:2]) for x, t in enumerate(text[1::2]) if len(t)>0])   

        #print(text)
        if 'имя канала' in text.split('\n'):                 
            text = text.replace(text.split('\n')[text.split('\n').index('имя канала')+1], query1['name_chanell']) 

        if 'ключевые слова' in text.split('\n'):   
            text = text.replace(text.split('\n')[text.split('\n').index('ключевые слова')+1], query1['keywords']) 
        try:
            await bot.send_message(message.from_user.id, text)
        except:
            await bot.send_message(message.from_user.id, 'Запрос пуст')
    elif message.text=="ПОИСК":
        if query1['name_chanell']!='':     
            res =CALL(query=query1)
            if res!=None:
                print(res)
                r = res.split(' ')[0]+' '+res.split('.com/')[1] # .split(',')[1]
                # r = '50 asd'
                # res=r
                try:   
                    #print(103, f"Найдено {res.split(' ')[0]} каналов продолжить?")             
                    await bot.send_message(message.from_user.id, f"Найдено {res.split(' ')[0]} каналов.\n Продолжить?", reply_markup = add_buttons4(r)) 
                except Exception as e:
                    print(e)
                    await bot.send_message(message.from_user.id, f"Ничего не найдено 001", reply_markup = None)        
        else:
            await bot.send_message(message.from_user.id, f"Необходимо ввести название канала", reply_markup = None) 
    

    elif message.text in params.keys():
        print(message.text, params[message.text])
        markup = add_buttons2(params[message.text])
        await bot.send_message(message.from_user.id, f'{message.text.capitalize()}: выбор параметров', reply_markup=markup)
  

    elif message.text.lower().split(' ')[0].split('_')[0].split('.')[0].split(',')[0] in ' '.join(all_values) or \
        'канал' in message.text.lower():
        if message.text.strip().lower().startswith('канал') and len(message.text.replace('канал','').strip())>2: 
            m_txet =message.text.lower().replace('канал','')
        else: 
            m_text = message.text.lower()
        req = m_text.split(' ')[0].split('_')[0].split('.')[0].split(',')[0]
        #posible_answers = [i for i in all_values if message.text in i.lower()]            
        posible_answers = [i2 for i in colection for i2 in list(eval(i).values()) if req in i2.lower()]
        #print(posible_answers )
        for r in ' ,._;':                            
            if r in message.text:
                posible_answers = [p_a for p_a in posible_answers for r2 in m_text.split(r)[1:] if r2 in p_a.lower()]
        
        vars_ = {p_a:i for i in colection for p_a in posible_answers if p_a in list(eval(i).values())}
        I = list(set(vars_.values()))
        #new_vars ={}
        for i in I: 
            temp=[] 
            for k in vars_.keys():
                if vars_[k]==i:    
                    temp.append(k)
            new_vars[i]=temp  

        nv2={}
        for i, v1 in new_vars.items():
            
            temp=[]
            for j, v2 in eval(i).items():
                for v0 in v1:
                    if v0==v2:                        
                        if 'ru_' not in i: 
                            temp.append(eval('ru_'+i)[j])
                        else: 
                            temp.append(eval(i)[j])
            nv2[i]=temp
        text = '\n'.join([i+':\n/'+'\n/'.join([n.replace(' ', '_') for n in new_vars[i]]) for i in new_vars.keys()])
        #print(nv2)
        #print('nv2',nv2)
        #print('new_vars', new_vars)
        await bot.send_message(message.from_user.id, f"Возможные варианты", reply_markup = add_buttons5(new_vars, nv2))
    # elif message.text.replace('/','') in ' '.join(all_values):
    #     bot.send_message(message.from_user.id, f"Вариант {message.text} выбран")
    

    elif NOT(message.text, rus_words):
        #print("OK")
        
        new_vars = {arg[3:]:[] for arg in ['ru_country','ru_lang', 'ru_topics','ru_category']}
        nv2 = {arg[3:]:[] for arg in ['ru_country','ru_lang', 'ru_topics','ru_category']}
        #print(new_vars)
        [new_vars[arg[3:]].append(w) for arg in ['ru_country','ru_lang', 'ru_topics','ru_category'] for i, w in eval(arg).items() for n in NOT(message.text, rus_words) if w==n ]
        [nv2[arg[3:]].append(eval(arg[3:])[i]) for arg in ['ru_country','ru_lang', 'ru_topics','ru_category'] for i, w in eval(arg).items() for n in NOT(message.text, rus_words) if w==n ]

        # print('nv2',nv2) # eng
        # print('new_vars', new_vars)
        await bot.send_message(message.from_user.id, f"Возможные варианты", reply_markup = add_buttons5(nv2, new_vars))
                    
        
                    
        
    elif not message.text.startswith('/') and message.text not in ['ПРОВЕРКА', 'ОТМЕНА', 'ПОИСК', "страна",'язык','категория','тема', "подписчиков от ",   
        "подписчиков до", "просмотров от", "просмотров до", "всего видео от", "всего видео до", "видео не позднее", "видео не ранее", "последнее от", 
        "последнее до"] and not NOT(message.text, rus_words):      
        
        #print(eval('ru_country').values())
        #print(message.text)  
        Temp = message.text                
        await bot.send_message(message.from_user.id, message.text, reply_markup=add_buttons3())
    #bot.send_message(message.from_user.id, message.text)


#@dp.callback_query_handler(lambda x: x.data)
async def query_handler(call:types.CallbackQuery):
    # if call.data == 'category':        
    #     bot.answer_callback_query(callback_query_id=call.id, text='\n'.join(autocomplete(message.text, category)))
    
    #markup2= {}
    #bot.send_message(call.message.chat.id, None, reply_markup=None)
    #bot.answer_callback_query(callback_squery_id=call.id, text='\n'.join(autocomplete(message.text, eval(i))), reply_markup=murkup2)
    global query1, query, Temp, URL, w    
    #print(dir())
    
    if call.message:   
        #print(203, call.data)    
        if 'press' in call.data:   
            _, ch, x  =  call.data.split('#')
            if "ru_" not in ch: 
                #print('chanell = ',ch)
                try:
                    _dict = eval(ch+'2')
                    _d = ch+'2'
                except:
                    _dict = eval(ch)
                    _d = ch

                if x in _dict.keys():
                    #print(ch)
                    #print(_dict[x])
                    try:
                        text = eval('ru_'+ch)[_dict[x]]#; print(219, eval('ru_'+ch))
                    except:
                        text = _dict[x]#; print(221, eval(ch))
                elif x in _dict.values():
                    text = eval('ru_'+ch)[x]#; print(223, eval(ch)[x]) #eval(ch))           
                else:
                    text = eval('ru_'+ch)[x]  

            if "ru_" in ch:                 
                text = eval(ch)[x]
                        
            try:
                c = call.data.split('#')[2]
                t = eval(call.data.split('#')[1])                    
                try:                        
                    if c in t.keys():
                        query1[call.data.split('#')[1]]+=[t[c]]
                    else:
                        query1[call.data.split('#')[1]]+=[c]
                except:
                    query1[call.data.split('#')[1]]=eval(call.data.split('#')[1])[call.data.split('#')[2]]
                #print(654, query1)
                #print(655, query)
                #await bot.send_message(call.message.from_user.id, '', reply_markup=None)
                await bot.edit_message_text( text, call.from_user.id, call.message.message_id)    
            except:
                pass
                #query1[call.data.split('#')[1]] = call.data.split('#')[2]
            #print(query1)
            
        if call.data == 'name_chanell' and  Temp!='':
            query1['name_chanell']= Temp
            Temp = ''
            #bot.send_message(message.chat.id, None, reply_markup=add_buttons())
            #await bot.answer_callback_query(callback_query_id=call.id, text='\n'.join(autocomplete(message.text, latest_video)))
            await bot.answer_callback_query(callback_query_id=call.id, text='')#, reply_markup=None)
            #await bot.edit_message_text( 'name_chanell', call.from_user.id, call.message.message_id, reply_markup=None)    

        if call.data == 'keywords' and  Temp!='':
            query1['keywords']= Temp
            Temp = ''
            #bot.send_message(message.chat.id, None, reply_markup=add_buttons())
            #await bot.answer_callback_query(callback_query_id=call.id, text='\n'.join(autocomplete(message.text, latest_video)))
            await bot.answer_callback_query(callback_query_id=call.id, text='')
            #await bot.edit_message_text( 'keywords', call.from_user.id, call.message.message_id, reply_markup=None)    

            # open ,CALL with query params !!!

        if call.data.strip().startswith('yes'):# and URL!='':   
            #print(273, call.data)            
            mess = bot.send_message
            id_ = call.message.from_user.id
            txt = call.data.split(' ')
            res =txt[1]
            url ='https://www.channelcrawler.com/'+txt[2] 
            emails, titles, hrefs, descrs, images = CALL2(mess, id_, url, int(res))  
            emails = {k:v for e in emails for k, v in e.items()}
            #print(emails) #{urls: descrs}
            #print(titles)
            descrs = ['\n'.join([d2.strip() for d2 in d.split('\n')]) for d in descrs]
            #print(275, descrs)
            #answer = mail_finder(URL)  
            #text = ['\n'.join(l[x]) for l in answer for x, _ in links[0][:-1]]   
            text = [titles[x]+'\n'+descrs[x]+'\n\n'+'\n'.join([e.replace('%3A',':').replace('%2F','/') for e in emails[i]])\
             for x, i in enumerate(hrefs) if emails[i]!=['']] 
                  
            #
            text = '\n\n'.join(text)
            print(text)
            await bot.edit_message_text(text, call.from_user.id, call.message.message_id)
            """
            for x, a in enumerate(hrefs):
                print(text[x])
                #await bot.send_photo(chat_id = message.chat_id, photo = a[-1])
                #await bot.send_message(message.from_user.id, text[x], reply_markup=add_buttons())
                await bot.edit_message_text(text[x], call.from_user.id, call.message.message_id)#, reply_markup=add_buttons())#
                '''
                try:
                    await bot.send_photo(call.from_user.id, photo=hrefs[x])
                except:
                    print('BAD  URL ', hrefs[x])
                '''
                # save as text   with open('photos/AQADBfoYmy4AA588BgAB.jpg', 'rb') as photo:
            """


            #send request(query) get answer number chanells
        if call.data == 'cancel':
            query1 = query            
            try:
                driver.quit()
            except:
                pass

        # print(629, call.message, call.data)
        # if call.message and not call.data.startswith('yes'):
            
        #     #print(call.data.split('#'))
        #     try:
        #         text = eval('ru_'+call.data.split('#')[1])[call.data.split('#')[-1]]
        #     except:
        #         print(call.data)
        #         text = eval(call.data.split('#')[1])[call.data.split('#')[-1]]
        #     print(316,text)
        #     await bot.edit_message_text(
        #         text, 
        #         call.from_user.id,
        #         call.message.message_id)#,  reply_markup=None)
                
    try:
        pass
    except Exception as e:
        print(427)
        print(call.data)
        w.disconnect        
        print(repr(e))

#@dp.callback_query_handler(lambda x: x.data)
async def callback_inline(call:types.CallbackQuery):
    
    #print(629, call.message, call.data)
    if call.message and not call.data.startswith('yes'):
        
        #print(call.data.split('#'))
        try:
            text = eval('ru_'+call.data.split('#')[1])[call.data.split('#')[-1]]
        except:
            text = eval(call.data.split('#')[1])[call.data.split('#')[-1]]
        #print(316,text)
        await bot.edit_message_text(
            text, 
            call.from_user.id,
            call.message.message_id)#,  reply_markup=None)

 

#@dp.message_handler(commands=['start'])
async def welcome(message:types.Message):
    
    #print("Start working telegramm bot <<CONTACT FINDER from YOUTUBE>>")    
    await bot.send_message(message.from_user.id, "Выберите опцию и установите значение\nполе имя канала обязательно!")
    # sti = open('static/welcome.webp', 'rb')
    # bot.send_sticker(message.from_user.id, sti)

    
    await bot.send_message(message.from_user.id, 'WELCOME', reply_markup=add_buttons()) # , parse_mode = 'html'

#@dp.message_handler()
async def echo_send(message:types.Message):
    global query1, RU2

    #print(343, query1)
    if message.text=="ОТМЕНА": 
        for k,v in query1.items():
            if isinstance(v, str): query1[k]=''
            if isinstance(v, list) and v!=[]: query1[k]=[]  
        await bot.send_message(message.from_user.id, 'Отмена операции', reply_markup=add_buttons())               

    elif message.text=="ПРОВЕРКА": 
        RU2 = {k.strip(): v for k, v in RU2.items()}
        text = []
        for q in query1.keys():
            text.append(RU[q])
            if isinstance(query1[q], list) and  query1[q]!=[] and  query1[q]!='':
                t=[]
                for e in query1[q]:
                    if e in RU2.keys():
                        t.append(RU2[e.strip()].capitalize())
                    else:
                        t.append(e) 
                text.append(',\t'.join(t))
            else:
                text.append(query1[q])
                    
        text = '\n'.join(['\n'.join(text[text.index(t)-1:][:2]) for x, t in enumerate(text[1::2]) if len(t)>0])   
        
        if 'имя канала' in text.split('\n'):                 
            text = text.replace(text.split('\n')[text.split('\n').index('имя канала')+1], query1['name_chanell']) 
            print(text)
        if 'ключевые слова' in text.split('\n'):   
            print(query1['keywords'])                        
            text = text.replace(text.split('\n')[text.split('\n').index('ключевые слова')+1], query1['keywords']) 
            print(text)

        await bot.send_message(message.from_user.id, text)
    elif message.text=="ПОИСК":
        #print(query1['name_chanell'])
        if query1['name_chanell']!='':
            print(query1)
            try:
                res, url  = CALL(query=query1)
                await bot.send_message(message.from_user.id, f"000 Найдено {res.split(' ')[0]} каналов продолжить?", reply_markup = add_buttons4(res+''+url.split('.com/')[1])) 

            except:
                await bot.send_message(message.from_user.id, f"Ничего не найдено  000")#, reply_markup = None)
        else:
            await bot.send_message(message.from_user.id, f"Необходимо ввести название канала")#, reply_markup = None) 
    
    elif {i.lower().translate(str.maketrans('','',pnt)) for i in message.text.split(' ')}\
    .intersection(set(json.load(open('cenz.json'))))!=set():
        #await message.reply('')
        await message.delete()
    else:
        #await message.answer(message.text)
        #await message.reply(message.text)
        #print(os.getcwd())
        await bot.send_message(message.from_user.id, message.text, reply_markup = add_buttons3())


def register_handlers_client(dp: Dispatcher):
    
    dp.register_message_handler(welcome, commands=['start', 'help'])
    dp.register_message_handler(send_mess, state="*")
    dp.register_message_handler(echo_send, state="*")
    
    

def register_callback_client(dp:Dispatcher):   
    
    dp.register_callback_query_handler(query_handler, lambda x: x.data)
    dp.register_callback_query_handler(callback_inline, lambda x: x.data)
    #dp.register_callback_query_handler(callback_inline, call: types.CallbackQuery)
    #dp.register_callback_query_handler(callback_inline, lambda callback_query: True)










