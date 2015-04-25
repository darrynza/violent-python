from anonBrowser import *
ab = anonBrowser(proxies=[], \
     user_agents=[('User-gent', 'superSecretBrowser')])
for attempt in range(1, 15):
    ab.anonymize()
    print '[*] Fetching page'
    response = ab.open('http://kittenwar.com')
    for cookie in ab.cookie_jar:
        print cookie
        
