import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        
        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }
        
        for k, v in data.items():
            print(f'{k} : {v}')
        
        area = folium.Map(location=(response.get('lat'), response.get('lon')))

        # Added Marker on location so it is lots easier to see the l
        folium.Marker(location=(response.get('lat'), response.get('lon')), tooltip="Probably the location of the target.").add_to(area)

        area.save(f'{response.get("query")}_{response.get("city")}.html')
        
    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')
        
        
def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))

    ip = input('Please enter a target IP or quit: ')
    # simplest possible menu at 4 a.m.
    
    if ip == 'quit': return
    get_info_by_ip(ip=ip)
    main()
    
    
if __name__ == '__main__':
    res = ''
    while res.lower() not in ('quit', 'q'):
        main()
        while res not in ('quit', 'q', 'again', 'a'):
            res = input('Enter quit/q or again/a: ')

