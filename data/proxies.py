import requests

from .theme import C

proxy_urls = [
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=3000&country=all&ssl=all&anonymity=all&simplified=true',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000'
]

def DOWNLOAD(): 
    proxy_file = open('data/proxies.txt', 'w')
    proxies    = []
    while True:
        try:
            for url in proxy_urls:
                scrape = requests.get(url).text.replace('\n', '')
                proxies.append(scrape)
            for proxy in proxies:
                proxy_file.write(proxy)
            proxy_file.close()
        except:
            print(f'{C.red}• {C.white}Error occured while attempting to download proxies.')
            pass
        print(f'{C.lime}• {C.white}Downloaded proxies.')
        break    
