from pickle import dump as pdump
from pickle import load as pload
from facebook import GraphAPI

def read_creds(filename):
    creds = pload(open('fb_creds.pkl','rb'))
    return creds

creds = read_creds('fb_creds.pkl')
graph = GraphAPI(access_token=creds['access_token'])

msg = '''Join us this Friday morning for the next session of Grim Harvest!
With Randy playing PowPow 2.0 the Artificer Warforged,
Kat playing Bash the Party Girl Barbarian Kobold,
Joe playing Grandolith Biltha the Elf Warrior,
James H. playing Gavor Runehammer the Duergar Celestial Warlock,
Matt playing Caius Vesterhoff the Priest of Illmater,
and Zach returning as Luther the Orc Barbarian!'''
lnk = 'https://www.twitch.tv/thisisactionsurge'

## Post to Page
graph.put_object(parent_object=creds['page_id'],connection_name="feed",message=msg,link=lnk)
print(graph,get_connections(creds['page_id'],'feed'))

## Post to Group
graph.put_object(parent_object=creds['group'],connection_name='feed',message=msg,link=lnk)
print(graph.get_connections(creds['group'],'feed'))
