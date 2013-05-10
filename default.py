import xbmcgui,xbmcplugin,xbmcaddon
import os,re,urllib,urllib2

IMAGE_PATH = xbmc.translatePath('special://home/addons/plugin.image.9gag/resources/images/')

class menuHandler:
	def addDir(self,name,url,mode,iconimage):
    		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"name="+urllib.quote_plus(name)
    		liz=xbmcgui.ListItem(unicode(name), iconImage="DefaultFolder.png",thumbnailImage=iconimage)
    		liz.setInfo( type="Video", infoLabels={ "Title": name })
    		return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)

        def CATEGORIES(self):
                self.addDir('hot','http://dummyurl.org',1,os.path.join(IMAGE_PATH,'hot.png'))
                self.addDir('trending','http://dummyurl.org',2,os.path.join(IMAGE_PATH,'trending.png'))
                self.addDir('vote','http://dummyurl.org',3,os.path.join(IMAGE_PATH,'vote.png'))
                self.addDir('saves','http://dummyurl.org',4,os.path.join(IMAGE_PATH,'saves.png'))
                self.addDir('search','http://dummyurl.org',5,os.path.join(IMAGE_PATH,'search.png'))

	def HOT(self):
		return True;

	def TRENDING(self):
		return True;

	def VOTE(self):
		return True;

	def SAVES(self):
		return True;

	def SEARCH(self):
		return True;

def runPlugin():

	# initialize variables	
	addon = xbmcaddon.Addon(id='plugin.image.9gag')
	thisPlugin = int(sys.argv [1])
        update_dir = False
        success = True
        cache = True
        mode=None

	# get memes URLs for all categories
	main_webpage = urllib2.urlopen("http://9gag.com",timeout=6).read()
	trending_webpage = urllib2.urlopen("http://9gag.com/trending",timeout=6).read()
	vote_webpage = urllib2.urlopen("http://9gag.com/trending",timeout=6).read()

	main_memes = re.findall('img .*?src="(.*?)"',main_webpage)
	trending_memes = re.findall('img .*?src="(.*?)"',trending_webpage)
	vote_memes = re.findall('img .*?src="(.*?)"',vote_webpage)

	menu = menuHandler()

	if mode==None or url==None or len(url)<1:
        	menu.CATEGORIES()
	elif mode==1:
        	success = menu.HOT(main_memes)
	elif mode==2:
                success = menu.TRENDING(trending_memes)
	elif mode==3:
                success = menu.VOTE(vote_memes)
	elif mode==4:
                success = menu.SAVES()
	elif mode==5:
		success = menu.SEARCH()

	xbmcplugin.endOfDirectory(thisPlugin,succeeded=success,updateListing=update_dir,cacheToDisc=cache)


### Begin of time ###
runPlugin()

