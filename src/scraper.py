import requests

if __name__ == '__main__':
    url = "https://classcentral.com"
    headers = {
        'User-Agent': 'Python',
        'cookie': 'PHPSESSID=ecjovktb0s9i0l74u9kkj4p'
    }
    # res = requests.get(target_url, headers=headers)
    session = requests.Session()
    session.cookies.set('default','PHPSESSID=ecjovktb0s9i0l74u9kkj4p')
    print(session.headers)
    res = session.get(url)
    print(res)
    
