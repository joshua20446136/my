from time import sleep
import time
import requests
import datetime

url = "https://rf.eefocus.com/module/forum/plugin.php"

querystring = {"id":"xbigwheel:data","bigwheel_id":"59","formhash":"8b82053c"}

headers = {
    'cookie': "_rollupGa=GA1.2.250903795.1639115002; _pk_id.4.2179=ee4d9a0cef02cb0c.1640071465.; eef_uid=3343318; o20a_2132_smile=1D1; o20a_2132_nofavfid=1; _pk_ref.4.2179=%5B%22%22%2C%22%22%2C1662512258%2C%22https%3A%2F%2Fwww.moore8.com%2Fcourses%2F504%22%5D; o20a_2132_saltkey=H0I0OgZ4; o20a_2132_lastvisit=1663890983; o20a_2132_visitedfid=1247; __utmz=18405754.1664157762.218.9.utmcsr=sso.eefocus.com|utmccn=(referral)|utmcmd=referral|utmcct=/module.php/core/login_wechat.php; o20a_2132_editormode_e=1; _gid=GA1.2.1104416918.1665374068; _rollupGa_gid=GA1.2.981162801.1665374068; __utma=141874342.250903795.1639115002.1664256738.1665489536.28; __utmz=141874342.1665489536.28.20.utmcsr=newsletter|utmccn=Sep_New_article|utmcmd=email; Hm_lvt_644a837956e91928688d4a74b9917d47=1665194438,1665363463,1665489537,1665553024; Hm_lpvt_644a837956e91928688d4a74b9917d47=1665553024; _ga=GA1.2.250903795.1639115002; Hm_lvt_499fb657bc8d23f354f717419c9b0f83=1665194440,1665374068,1665489538,1665553025; Hm_lpvt_499fb657bc8d23f354f717419c9b0f83=1665553025; _clck=vrub60|1|f5n|0; _clsk=1vb1lu5|1665553026933|1|1|i.clarity.ms/collect; _ga_EEZL06BJ1P=GS1.1.1665553025.491.0.1665553028.57.0.0; SimpleSAMLSessionID=8312eb6092f1e9039ecde892f70e627e; o20a_2132_sid=yTtS65; o20a_2132_viewid=tid_626644; o20a_2132_sendmail=1; __utma=18405754.250903795.1639115002.1665537049.1665554583.248; __utmc=18405754; __utmt=1; Hm_lvt_53163e366c6c8be624063c944dc0857a=1665194762,1665363430,1665537049,1665554583; pisess=kccdkk8ph0q5tih2calbesl5d1; SimpleSAMLAuthToken=_3b0a4c299768590cc375388a9382b51c4e1c88a257; o20a_2132_ulastactivity=9794oL9msTI8G7TDxrxvdQQ8xZGOHxE2X03CmjsclZxt8Twd8UTx; o20a_2132_auth=1d45D6abFKS%2FsJ%2Fh0KzGuC%2FUVauo7LjlicxjrN5O%2F9WPCbDFiXpJ3lGvMLFiO7yqcWnI7xSrmBTsBpT0yEVyuJqjOkML; o20a_2132_lastcheckfeed=3343318%7C1665554594; PHPSESSID=dqftuk67hanskig8j56j4aqcn3; o20a_2132_lastact=1665554721%09forum.php%09viewthread; o20a_2132_st_p=3343318%7C1665554721%7Caab431be1dc0fff89bea86d5678b61fa; Hm_lpvt_53163e366c6c8be624063c944dc0857a=1665554714; __utmb=18405754.6.10.1665554583",
    'user-agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'referer': "https://rf.eefocus.com/module/forum/thread-626644-1-1.html"
    }

#response = requests.request("POST", url, headers=headers, params=querystring)

#print(response.text)


#505  10
#516
#50686

# for num in range(100): 
while True:
    # print (num) 
    response = requests.request("POST", url, headers=headers, params=querystring)
    print(response.text)
    time.sleep(2)
    # if '2022-10-12 20:53:00' < datetime.datetime.now().strftime('%Y-%m-%d %X'):
    #     break