from requests import get

from .theme   import C

USERAGENTS = open('data/useragents.txt').read().splitlines()
REFERRERS  = open('data/referrers.txt').read().splitlines()

PROXY_URLS = (
    'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=3000&country=all&ssl=all&anonymity=all&simplified=true',
    'https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000'
)

PROXIES    = set()
while True:
    try:
        for url in PROXY_URLS:
            PROXIES.update(get(url).text.splitlines())
    except:
        print(f'{C.red}• {C.white}Error occured while attempting to download proxies.')
        
    print(f'{C.lime}• {C.white}Downloaded proxies.')
    break
