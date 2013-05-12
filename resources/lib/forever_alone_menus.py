import xbmc,xbmcplugin,xbmcgui,xbmcaddon
import urllib,urllib2,re,os,sys
import lxml.html
from BeautifulSoup import BeautifulStoneSoup 

IMAGE_PATH = xbmc.translatePath('special://home/addons/plugin.image.9gag/resources/images/')

__settings__ = xbmcaddon.Addon(id='plugin.image.9gag')
__language__ = __settings__.getLocalizedString

class MenuHandler:

   	def __init__(self):
		print 'Menu instantiated'

	def display_HOT_menu(self):
		print 'display_HOT_menu'
		tags = self.getImageTags('http://9gag.com/')
		for tag in tags:
			try:
				style = tag['style']
				print style	
       				title = tag['alt']
                        	print title
                        	url = tag['src']
                        	print url

				listitem = xbmcgui.ListItem( title, iconImage="DefaultPicture.png", thumbnailImage = url )
				xbmcplugin.addDirectoryItem( handle=int(sys.argv[ 1 ]), url = url, listitem=listitem, isFolder=False)		
			except:
				pass
	        xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )


	def display_TRENDING_menu(self):
		print 'display_TRENDING_menu'
                tags = self.getImageTags('http://9gag.com/trending/')
                for tag in tags:
                        try:
                                style = tag['style']
                                print style
                                title = tag['alt']
                                print title
                                url = tag['src']
                                print url

                                listitem = xbmcgui.ListItem( title, iconImage="DefaultPicture.png", thumbnailImage = url )
                                xbmcplugin.addDirectoryItem( handle=int(sys.argv[ 1 ]), url = url, listitem=listitem, isFolder=False)
                        except:
                                pass
                xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )


	def display_VOTE_menu(self):
		print 'display_VOTE_menu'
                tags = self.getImageTags('http://9gag.com/vote/')
                for tag in tags:
                        try:
                                style = tag['style']
                                print style
                                title = tag['alt']
                                print title
                                url = tag['src']
                                print url

                                listitem = xbmcgui.ListItem( title, iconImage="DefaultPicture.png", thumbnailImage = url )
                                xbmcplugin.addDirectoryItem( handle=int(sys.argv[ 1 ]), url = url, listitem=listitem, isFolder=False)
                        except:
                                pass
                xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )


	def display_SAVES_menu(self):
		print 'display_SAVES_menu'

	def display_SEARCH_menu(self):
		print 'display_SEARCH_menu'

	def display_MOTHER_OF_MENUS(self):
		print 'display_MOTHER_OF_MENUS'
		self.addDir('hot',1,os.path.join(IMAGE_PATH,'hot.png'))
                self.addDir('trending',2,os.path.join(IMAGE_PATH,'trending.png'))
                self.addDir('vote',3,os.path.join(IMAGE_PATH,'vote.png'))
                self.addDir('saves',4,os.path.join(IMAGE_PATH,'saves.png'))
                self.addDir('search',5,os.path.join(IMAGE_PATH,'search.png'))
		xbmcplugin.endOfDirectory( handle=int( sys.argv[ 1 ] ), succeeded=True )


	##
	# handy funtions to create menus
	#

	def addDir(self,name,mode,iconimage):
    		plugin_url=sys.argv[0]+"?mode="+str(mode)
    		list_item=xbmcgui.ListItem(unicode(name), iconImage="DefaultFolder.png",thumbnailImage=iconimage)
    		list_item.setInfo( type="pictures", infoLabels={ "Title": name })
    		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),
			url=plugin_url,
			listitem=list_item,
			isFolder=True)
    		return ok

	def getImageTags(self,url):
		page = urllib2.urlopen(url)
		soup = BeautifulStoneSoup(page)
 		tags = soup.findAll('img', {'src' : re.compile(r'(jpe?g)|(png)$')})
		return tags
