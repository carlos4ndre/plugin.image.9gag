import os
import sys
import urlparse

LIB_DIR = xbmc.translatePath( os.path.join( os.getcwd(), 'resources', 'lib' ) )
sys.path.append (LIB_DIR)

import xbmcaddon
__settings__ = xbmcaddon.Addon(id='plugin.image.9gag')
__language__ = __settings__.getLocalizedString

import forever_alone_menus as plugin

### Extract parameters from argv
def get_params():
	url = sys.argv[2]
	return urlparse.parse_qs(urlparse.urlparse(url).query)

### Begin of time ###
params=get_params()
action=sys.argv[2]
mode=0

try:
	mode=int(params['mode'][0])
except:
	pass

print 'action='+action
print 'mode='+str(mode)

menu = plugin.MenuHandler()

if mode==1:
	menu.display_HOT_menu()
elif mode==2:
	menu.display_TRENDING_menu()
elif mode==3:
	menu.display_VOTE_menu()
elif mode==4:
	menu.display_SAVES_menu()
elif mode==5:
	menu.display_SEARCH_menu()
else:
	menu.display_MOTHER_OF_MENUS()
