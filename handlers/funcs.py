from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from random import choice
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from create_bot import bot
from fake_useragent import UserAgent
import os
import asyncio


#from DICTS import query 
driver = None
links = []

titles2 = []
urls2   = []
texts2  = []
images2 = []
LINKS   = []

wscrib = False

fa ={UserAgent(verify_ssl=False).random}

def op(adr):
    with open(adr) as file:
        return file.read() 

def CALL(**args):
    global URL, w , driver


    url = 'https://www.channelcrawler.com'
    ask = args    
    

    #print(326, ask)    
    # options = Options()
    # #options = webdriver.FirefoxOptions()
    # #options.add_argument("--headless")
    # user_agent = UserAgent().random
    # #options.set_preference("general.useragent.override", user_agent)
    # options.add_argument(f'user-agent={user_agent}')
    # path = f"{os.getcwd()}/geckodriver"   
    
    
    # # executable_path=path, 
    # driver = webdriver.Firefox(options=options) #, firefox_profile=_profile)

    driver = dr()
    driver.get(url)
    #==========================================
    while driver.current_url=='https://www.channelcrawler.com/banned/scraping' and wscrib==True:
        w.connect
        print(driver.current_url)
        #print(w.account)
        sleep(2)
        # change IP
        driver.get(url)  
    URL = url       
    name_1 = '//*[@id="queryName"]'
    name_4 = '/html/body/div[1]/div[3]/div/div[1]/div[1]/form/div[2]/div[1]/div[4]/div/div/div[1]/div/span[2]/input'
    #f'/html/body/div[1]/div[3]/div/div[1]/div[1]/form/div[2]/div[1]/div[{i}]/div/div/div[1]/div/span/input'

    def el(driver, i):   
        line =  f'/html/body/div[1]/div[3]/div[1]/form/div[2]/div[1]/div[2]/div/div[1]/div[{i}]/div/div/div[1]/div/span/input'
        answ = ''
        #print(line.split('/'))
        for l in line.split('/'):
            if l!='':
                #print(l)
                a = answ
                answ +='/'+l   
                try:
                    driver.find_element_by_xpath(answ) 
                except:
                    # print(driver.find_element_by_xpath(a).get_attribute('outerHTML'))
                    break
        return driver.find_element_by_xpath(line)
    

    def press(driver, a, q):    
        a.clear()
        a.send_keys(q)
        try:
            [i.send_keys(Keys.ENTER) for i in driver.find_elements_by_xpath('//li[contains(text(), "'+q+'")]') if q in i.text]
        except:
            print(a, q)
            print([ i.text for i in driver.find_elements_by_xpath('//li[contains(text())]')])
        #[i.send_keys(Keys.ENTER) for i in driver.find_elements_by_class_name('dropdown-option ') if q in i.text]
    
    

    NAME_CHANELL     = driver.find_element_by_xpath(name_1)
    KEYWORDS         = driver.find_element_by_css_selector('#queryDescription')
    #print(379, query)
    qu = ask['query']
    if qu['name_chanell']!='':NAME_CHANELL.send_keys(qu['name_chanell']) #.send_keys(webdriver.common.keys.Keys.ENTER)
    #if qu['topics']!=[]:[press(driver, el(driver, 3), q) for q in qu['topics']]
    if qu['lang']!=[]:[press(driver, driver.find_element_by_xpath(name_4), q) for q in qu['lang']]
    #print(qu['country'])
    if qu['country']!=[]:[press(driver, el(driver, 4) , q) for q in qu['country']]
    if qu['category']!=[]:[press(driver, el(driver, 2), q) for q in qu['category']]  
    if qu['creation_date_min']!='':driver = click(driver, '//*[@id="queryMinPublishedOn"]', qu['creation_date_min'])
    if qu['creation_date_max']!='':driver = click(driver, '//*[@id="queryMaxPublishedOn"]', qu['creation_date_max'])
    if qu['subscribers_min']!='':  driver = click(driver, '//*[@id="queryMinSubs"]', qu['subscribers_min'])
    if qu['subscribers_max']!='':  driver = click(driver, '//*[@id="queryMaxSubs"]', qu['subscribers_max'])
    if qu['total_views_min']!='':  driver = click(driver, '//*[@id="queryMinViews"]', qu['total_views_min'])
    if qu['total_views_max']!='':  driver = click(driver, '//*[@id="queryMaxViews"]', qu['total_views_max'])
    if qu['total_videos_min']!='': driver = click(driver, '//*[@id="queryMinVideos"]', qu['total_videos_min'])        
    if qu['total_videos_max']!='': driver = click(driver, '//*[@id="queryMaxVideos"]', qu['total_videos_max'])
    if qu['lastest_video_min']!='':driver = click(driver, '//*[@id="queryMinLastVideoDate"]', qu['lastest_video_min'])
    if qu['lastest_video_max']!='':driver = click(driver, '//*[@id="queryMaxLastVideoDate"]', qu['lastest_video_max'])
    if qu['keywords']!='':KEYWORDS.send_keys(qu['keywords'])
    sleep(2.1)
    #driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[1]/div[2]/div/button').click()

    driver.find_element_by_css_selector('.submitbutton').click()
    driver.implicitly_wait(5)
    #driver.switch_to_window(driver.window_handles[-1])
    #print(594, driver.current_url)
    try:
        driver.find_element_by_css_selector('.col-xs-12 > h3:nth-child(1) > b:nth-child(1)').text
        
        #bot.send_message(message.from_user.id, 'Совпадений не обнаружено')
        return
    except:
        #print(595)
        # print(driver.find_element_by_css_selector('.results-title').text)
        # print(driver.current_url) #print(THDI(driver))
        try:
            
            
            #driver.implicitly_wait(5)
            r =    driver.find_element_by_css_selector('.results-title').text
            url_ = driver.current_url
            driver.quit()
            
            return f'{r},{url_}'#, THDI(driver)
        except:            
            print('results-title has no text')            
            driver.quit()
            return ''


def href(link):
        global LINKS

        ii=0
        #print('href ',link)
        while ii<5 and link not in LINKS:
            
            driver = dr()
            driver.get(link)  
            res =  THDI(driver) 
            driver.quit()
            

            # print(res)
            # print()
            # print('='*100)
            
            if res!=[]:                
                #driver, m = contact(mess, id_, link)     
                LINKS.append(link)           
                  
                return res
                #print('href OK')                

            elif ii<5:                
                if wscrib==True:
                    w.connect 
                    sleep(4)
                else:
                    ii=5                
                ii+=1
        '''
        except Exception as e:
            print('Error CALL ', e)
            print()
            if ii<5:
                #sleep(2)
                print(186, link)
                if w is not None: w.connect
                
                options = Options()
                #options = webdriver.FirefoxOptions()
                options.add_argument("--headless")
                user_agent = UserAgent().random
                #options.set_preference("general.useragent.override", user_agent)
                options.add_argument(f'user-agent={user_agent}')
                driver = webdriver.Firefox(options=options) #, firefox_profile=_profile)  
                
                #driver = dr()
                print('winscribe ok')
                ii+=1
            else:
                #print('BAD')
                #return [],[],[],[]
                pass
        '''


def HREFS(mess, id_,link, num):
    from time import sleep
    from multiprocessing import Pool, cpu_count


    global w

    print(f'site {link} opening')   
    driver = dr()       
    links = [link]+[f'{link}/page:{i+2}' for i in range(int(num/20)-1) if num>20]
    print(links)
    with Pool(processes = 4) as pool:  res = pool.map(href, links)
    #[href(i) for i in links]
    
    k = res[0]
    for i in res[1:]:
        for x, i2 in enumerate(i):
            k[x]+=i2
    res = k
    print(res)
    
    print('Hrefs OK')  
    return res


def dr():
    options = Options()
    options.add_argument(f'user-agent={UserAgent(verify_ssl=False).random}')
    #options = webdriver.FirefoxOptions()
    #options.add_argument("--headless")
    options.set_preference('dom.webbdiver.enable', False)
    driver = webdriver.Firefox(options = options) #executable_path=path)

    return driver


# async def mn(links):#, driver):
#     global driver

#     tasks = [asyncio.create_task(ML(url, driver)) for url in links]    
#     #result = await asyncio.gather(*tasks); print(result)
#     return await asyncio.gather(*tasks)

def ML(link): 
    global w

    def A(text):
        from bs4 import BeautifulSoup as bs

        #print(text)
        soup = bs(text, "lxml")            
        RES = soup.find_all('a', class_="yt-simple-endpoint style-scope ytd-channel-about-metadata-renderer")
        #print(['http'+r.attrs['href'].split('q=http')[1].replace('%3A',':').replace('%2F','/') for r in RES])

        if RES == None or RES==[]:             
            return []
        else:
            return ['http'+i.attrs['href'].split('q=http')[1].replace('%3A',':').replace('%2F','/') for i in RES ]

    def res(l):
        # from selenium.webdriver.support.ui import WebDriverWait
        # from selenium.webdriver.support import expected_conditions as EC
        # from selenium.webdriver.common.by import By
        from time import sleep


        driver = dr()

        n=0
        if l!='':
            try:
                driver.get(l+'/about')
                wait = WebDriverWait(driver, 15); n=1                
                pool_0 = wait.until(EC.presence_of_element_located((By.ID, "link-list-container"))).get_attribute('outerHTML'); n=8
                #print(pool_0)
                if 'selenium.webdriver.remote.webelement.WebElement' in str(pool_0): 
                    try:
                        pool_0 = pool_0.text; n=9
                        print('text pool_0 = ',pool_0)
                    except Exception as e:
                        print(n, e)
                        print(pool_0)
                        print()
                    #pool_0 = pool_0.get_attribute('outerHTML')    

                soc = A(pool_0); n=12
                exs = ['https://twitter.com/', 
                        'https://www.twitch.tv/', 
                        'https://t.me/', 
                        'https://vk.com/', 
                        'https://www.instagram.com/', 
                        'https://wa.me/',
                        'www.facebook.com/', 
                        'https://discord.gg/']
                print([e for s in soc for e in exs if s.startswith(e)])
                soc = list(set([s for s in soc for e in exs if s.startswith(e) or '@' in s]))  
                try:
                    pool_ = wait.until(EC.presence_of_element_located((By.ID, "description-container"))); n=2
                    pool_=pool_.find_element_by_id('description'); n=3
                    print(277, pool_)
                except Exception as e: 
                    driver.quit() 
                                                  
                    return  soc
                    # print('Error !!!', 250,pool_)
                    # print(e)
                    # print()

                    try:
                        pool_.get_attribute('outerHTML'); n=4
                        print('='*50)
                    except Exception as e:
                        print('ERROR ',255, e)

                if pool_:
                    try:
                        pool_ = pool_.text; n=5
                        #print(294, pool_)
                        if pool_=='':
                            driver.quit()
                            return soc
                    except:                    
                        try:
                            
                            if type(pool_)!=str:
                                pool_ = pool_.get_attribute('outerHTML')
                                #print(300 , pool_)
                                pool_=pool_.split('</yt-formatted-string> ')[0].split('>')[-1]; n=6
                            else:                                
                                if ('id="description"' and '</yt-formatted-string>') in pool_:
                                    pool_=pool_.split('</yt-formatted-string>')[0].split('>')[-1]; n=7
                                print(264, pool_)
                        except Exception as e:
                            print(255, type(pool_), e)
                            if type(pool_)!=str: print(pool_.get_attribute)
                            print('='*50)
                    #pool_ = wait.until(EC.presence_of_element_located((By.ID, "description-container"))).find_element_by_id('description').text#.get_attribute('outerHTML')
                    #print(259, 'p1', pool_, '\n /p1') # .find_element_by_id('description').text
                    
                    #if type(pool_)!=str:  print(pool_.get_attribute)
                        
                    sleep(2)

                    #print(268, pool_0)
                    
                    
                    if pool_!='' and type(pool_)==str:
                        pool_2=pool_.replace('\n',' ').split(' '); n=10       
                        #.text.replace('\n',' ').split(' ')

                        # pool_ = driver\
                        # .find_element(By.ID, "description-container")\
                        # .find_element(By.ID, "description")\
                        # .text.replace('\n',' ').split(' ')
                        #print('pool_',driver.find_element(By.ID, "link-list-container").text)
                        #print('pool_0',pool_2)
                        
                        #print('Pool_2',pool_2)
                        mails = [i for i in pool_2 for e in exs if i.startswith(e)]+[i for i in pool_2 if '@' in i] ; n=11
                        driver.quit()
                        print('mails = ', mails)                          
                        print('soc = ', soc)  
                                  
                        if mails!=[] or soc!=[]:
                            print('ml', mails+ soc)                   
                            return  list(set(soc+mails))
                        # except Exception as e:
                        #     print(l, e) 
                        else:
                            return []
            except Exception as e:
                print('Invailid URL', l)
                driver.quit()
                #print(wait.until(EC.presence_of_element_located((By.ID, "description-container"))).find_element_by_id('description'))
                print(n+1, e)

        
    #if isinstance(links, list): L = await {l: res(l,WebDriverWait(driver, 5).until( driver) for l in links}
    res = res(link)
    
    if res: 
        return {link: res}
    else: 
        return {link: ['']}


def CALL2(mess, id_, url, num): 
    import asyncio
    from multiprocessing import Pool, cpu_count


    global w

    print('CALL2 open')
    # proxy = op("IP") #.replace('\t', ', ')}"'     
    # profile = change_ip(choice(proxy).split('\t'))

    #options = Options()
    #options.add_argument("--headless")
    # user_agent = UserAgent().random
    # options.add_argument(f'user-agent={user_agent}')
    # path = f"{os.getcwd()}/geckodriver"
    #path = '/home/alex/Рабочий стол/avito paarsing/geckodriver'
    


    titles, links, texts, images = HREFS(mess, id_, url, num)    

    # text = op('data').split('\n')
    # titles = [i1              for i in text for i1 in eval(i)[0]]
    # links  = [i1              for i in text for i1 in eval(i)[1]]
    # texts  = [i2 for i in text for i1 in eval(i)[2] for i2 in i1]
    # images = [i1              for i in text for i1 in eval(i)[3]]

    # print(titles)
    # print(links)
    # print(texts)

    #titles, links, texts, images = text   

    
    #res = asyncio.run(mn())
    #res = mn(links)
    #print('100', links)
    with Pool(processes = 4) as pool:  res = pool.map(ML, links) 
    

        # try:
        #     loop = asyncio.get_running_loop()
        # except RuntimeError:  # 'RuntimeError: There is no current event loop...'
        #     loop = None

        # if loop and loop.is_running():
        #     print('Async event loop already running. Adding coroutine to the event loop.')
        #     tsk = loop.create_task(mn(links))
        #     # ^-- https://docs.python.org/3/library/asyncio-task.html#task-object
        #     # Optionally, a callback function can be executed when the coroutine completes
        #     tsk.add_done_callback(
        #         lambda t: print(f'Task done with result={t.result()}  << return val of main()'))
        # else:
        #     print('Starting new event loop')
        #     res = asyncio.run(mn(links))

        #print(res)       
    #driver.quit()
    
    print(res)
    return res, titles, links, texts, images
    





def win():
    from config import user, psw
    sl ='server_list'    
    from windscribe import Windscribe    
    w =Windscribe(sl, user=user, password=psw)
    w.login(user=user, password=psw)
    return w


def wdr():
    import json
    ar = []

    with open('cenz.txt', encoding = 'utf-8') as r:    
        #r = ['bitch', 'fuck']
        for n in r:
            i  =i.encode('utf-8')
            n = i.lower().split('\n')[0]
            if n!='':
                ar.append(n)
    #print(ar)
    with open('cenz.json', 'w', encoding = 'utf-8') as e:
        json.dump(ar, e)

def THDI(driver):
    #from bs4 import BeautifulSoup as bs
    #text =driver.page_source
    titles = []
    hrefs  = []
    descrs = []
    images = []
    #soup = bs(text, 'lxml')
    try:
        element = driver.find_elements_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div')
    except:
        print('TDHI', [d.get_attribute('outerHTML') for d in element])
    try:
        ti = [i.find_element_by_xpath(f'h4/a') for i in element]
    except:
        print('TDHI_2')
        print(485, [t.get_attribute('outerHTML') for t in ti])
    #print(507, str(ti))
    
    titles = []
    hrefs = []
    for i in ti:
        try:
            titles.append(i.attrs['title'])         
        except:
            titles.append(i.get_attribute('outerHTML').split('title=')[1].split('"')[1])
        try:
            hrefs.append(i.attrs['href'])           
        except:
            hrefs.append(i.get_attribute('outerHTML').split('href=')[1].split('"')[1])

    # titles = [t.attrs['title'] for t in ti if t!=None  and 'attrs' in dir(t) and 'title' in t.attrs]
    # hrefs  = [t.attrs['href'] for t in ti if t!=None ]
    css = '.channel > h4:nth-child(1) > a:nth-child(1)'
    path = '/html/body/div[1]/div[1]/div/div[2]/div/h4/a'

    
    d = [d.find_element_by_xpath(f'p[1]/small').get_attribute('outerHTML')\
        .replace('\t',' ').replace('<br>','').replace('<small>','').replace('</small>','').replace('          ','') for d in element]
    #d = [i.find_element_by_xpath(f'p[1]/small').get_text().replace('\t',' ') for i in dr]
    images = [i.find_element_by_xpath(f'a/img').get_attribute('outerHTML').split('src')[1].split('"')[1]   for i in element]
    #images  = [i.find_element_by_xpath(f'a/img').attrs['src']                for i in dr]

    # titles.append(ti.attrs['title'])
    # hrefs.append(ti.attrs['href'])
    if d: descrs+=d
    #if im: images.append(i.attrs['src'])

    '''
    for i in range(1,21):
        try:
            tit = f'/html/body/div[1]/div[1]/div/div[2]/div[{i}]/h4/a'
            des = f'/html/body/div[1]/div[1]/div/div[2]/div[{i}]/p[1]/small'
            im  = f'/html/body/div[1]/div[1]/div/div[2]/div[{i}]/a/img'
            ti = driver.find_elements_by_xpath(tit)
            d = driver.find_elements_by_xpath(des)
            i = driver.find_elements_by_xpath(i)
            if ti: titles.append(ti.attrs['title']); hrefs.append(ti.attrs['href'])
            if d: descrs.append(d.get_text().replace('\t',' '))
            if i: images.append(i.attrs['src'])

            ti = driver.find_element_by_css_selector(f'div.channel:nth-child({i}) > h4:nth-child(1) > a:nth-child(1)')
            if ti: titles.append(ti.attrs['title']); hrefs.append(ti.attrs['href'])
            d = driver.find_element_by_css_selector(f'div.channel:nth-child({i}) > p:nth-child(5) > small:nth-child(1)')
            if d: descrs.append(d.get_text().replace('\t',' ')) 
            i = driver.find_element_by_css_selector(f'div.channel:nth-child({i}) > a:nth-child(4) > img:nth-child(1)')        
            if i: images.append(i.attrs['src'])
            # t = soup.select_one(f'div.channel:nth-child({i}) > h4:nth-child(1) > a:nth-child(1)')            
            # if t: titles.append(t.get_text())
            # h = soup.select_one(f'div.channel:nth-child({i}) > h4:nth-child(1) > a:nth-child(1)')
            # if h: hrefs.append(h.attrs['href'])
            # d = soup.select_one(f'div.channel:nth-child({i}) > p:nth-child(5) > small:nth-child(1)')
            # if d: descrs.append(d.get_text().replace('\t',' ')) 
            # i = soup.select_one(f'div.channel:nth-child({i}) > a:nth-child(4) > img:nth-child(1)')        
            # if i: images.append(i.attrs['src'])
            
        except:
            pass
    '''   
    return [titles, hrefs, descrs, images]

def  get_contxet(urls):
    import asyncio
    import aiohttp
    

    #print(dir(asyncio))
    async def get_page(session, url): # , proxy=P()
        async with session.get(url) as r:  
            return await r.content.read() # [titles, hrefs, descrs, images]
                       

    async def get_all(session, url):
        tasks = []
        for url in urls:
            task = asyncio.create_task(get_page(session, url))
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results

    async def main(urls):
        from fake_useragent import UserAgent
        headers={'User-Agent': UserAgent().random}
        async with aiohttp.ClientSession(headers=headers) as session:
            data = await get_all(session, urls)
            return data 
    
    results = asyncio.run(main(urls))
    return results


def mail_finder(url):
    import asyncio    
    from bs4 import BeautifulSoup as bs


    num = num_page(url)
    urls = [url]+[f'{url}/page:{i}' for i in range(2, int(num/20)+2)]
    #print(urls)
    data = get_contxet(urls)
    data = [THDI(date) for date in data]
    print('='*50)
    print('='*50)
    
    data  = [d2 for d in data for x, d2 in enumerate(d)]
    title = [_ for d in data[::4] for _ in d ]
    hrefs = [_ for d in data[1::4] for _ in d ]
    descr = [_ for d in data[2::4] for _ in d ]
    imgs  = [_ for d in data[3::4] for _ in d ]
    data = [title, hrefs, descr, imgs]
    #print(data)
    data_ = asyncio.run(emails(data[1]))
    #print(data_)
    links = [LINKS(data[x][1], bs(d, 'lxml')) for x, d in enumerate(data_)]
    print(links)    
    return  links

def DIR(dirs):
    return {k.strip():v.strip() for k, v in dirs.items()}

def rd(adr):
    with open(adr) as file:
        return file.read()


def click(driver, adr, val):     
    if isinstance(val, str):
        print(val)
        [ i.click() for i in driver.find_element_by_xpath(adr).find_elements_by_css_selector('option') if val in i.text]
    # if isinstance(val, list):
    #     [ i.click() for v in val for i in driver.find_element_by_xpath(adr).find_elements_by_css_selector('option') if v in i.text]
    return driver


def NOT(word, _list):
    return [l for l in _list if word.lower() in l.lower()]


def num_page(url):
    import requests
    from bs4 import BeautifulSoup as bs
    from fake_useragent import UserAgent

    #print(url)
    headers={'User-Agent': UserAgent().random}
    # headers = requests.utils.default_headers()
    # headers.update({'User-Agent': UserAgent().random, })
    response = requests.get(url, headers=headers)    
    soup = bs(response.text, "lxml")

    print(soup.find('h3'))
    return int(soup.find('h3',class_='results-title').text.split(' ')[0])



#w = win()
w = None
driver = dr()



'''

while num>(i-1)*20:
        try:        
            if i==1:                
                pass
            else:
                link = f'{link}/page:{i}'             
            driver.get(link)  
            res =  THDI(driver) 
            driver.quit()
            print(156, res)   
            desc, url, text, image = res    ## 
            url = [u+'/about' for u in url]
            if desc!=[] and  url!=[] and  text!=[] and  image!=[]:
                titles+=desc
                urls  +=url
                texts +=text
                images+=image

                #driver, m = contact(mess, id_, link)
                print(num, 'OK')            
                i+=1
            elif ii<5:
                sleep(4)
                w.connect
                options = Options()
                #options = webdriver.FirefoxOptions()
                #options.add_argument("--headless")
                user_agent = UserAgent().random
                #options.set_preference("general.useragent.override", user_agent)
                options.add_argument(f'user-agent={user_agent}')
                driver = webdriver.Firefox(options=options) #, firefox_profile=_profile)  
                ii+=1

        except Exception as e:
            print('Error CALL ', e)
            print()
            if ii<5:
                #sleep(2)
                print(186, link)
                if w is not None: w.connect
                
                options = Options()
                #options = webdriver.FirefoxOptions()
                options.add_argument("--headless")
                user_agent = UserAgent().random
                #options.set_preference("general.useragent.override", user_agent)
                options.add_argument(f'user-agent={user_agent}')
                driver = webdriver.Firefox(options=options) #, firefox_profile=_profile)  
                
                #driver = dr()
                print('winscribe ok')
                ii+=1
            else:
                #print('BAD')
                i=num+1  


'''