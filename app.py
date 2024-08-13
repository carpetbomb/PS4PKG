#####################################################
print('=============')
print('Importing Modules')
import os
import FreeSimpleGUI as sg
import requests
from bs4 import BeautifulSoup
import webbrowser
import pyperclip as pc
from datetime import date
import cloudscraper
from PIL import Image
import io
import base64
import json


#sys.path.append("bin")
#from notif import display_notification
print('Done.')
MasterList = []
MasterCidList = []

if os.path.isfile("./bin/cache/list.json") == False:
	os.system("python "+"./bin/download.py")
	os.system("python "+"./bin/csv2json.py")

if os.path.isfile("./bin/apikey.txt") == False:
	with open("./bin/apikey.txt", "w") as write_file:
		write_file.write("")
	with open("./bin/apiselection.txt", "w") as write_file:
		write_file.write("")

if os.path.isfile("./bin/psxc.txt") == False:
	with open("./bin/psxc.txt", "w") as write_file:
		write_file.write("")

class Item(): # Defining item for metatable
    def __init__(self, GameName, TitleID, Region, Genre, VREnabled, DumpDate):
        self.GameName = GameName
        self.TitleID = TitleID
        self.Region = Region
        self.Genre = Genre
        self.VREnabled = VREnabled
        self.DumpDate = DumpDate
    def __str__(self):
        return self.GameName

class Item2(): # Defining item for metatable
    def __init__(self, TitleID, ContentID, icon0):
        self.TitleID = TitleID
        self.ContentID = ContentID
        self.icon0 = icon0

    def __str__(self):
        return self.GameName
def notif(ttl, message, img, time):
	if img == 'success':
		img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAAEKAAABCgEWpLzLAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAHJQTFRF////ZsxmbbZJYL9gZrtVar9VZsJcbMRYaMZVasFYaL9XbMFbasRZaMFZacRXa8NYasFaasJaasFZasJaasNZasNYasJYasJZasJZasJZasJZasJZasJYasJZasJZasJZasJZasJaasJZasJZasJZasJZ2IAizQAAACV0Uk5TAAUHCA8YGRobHSwtPEJJUVtghJeYrbDByNjZ2tvj6vLz9fb3/CyrN0oAAADnSURBVDjLjZPbWoUgFIQnbNPBIgNKiwwo5v1fsQvMvUXI5oqPf4DFOgCrhLKjC8GNVgnsJY3nKm9kgTsduVHU3SU/TdxpOp15P7OiuV/PVzk5L3d0ExuachyaTWkAkLFtiBKAqZHPh/yuAYSv8R7XE0l6AVXnwBNJUsE2+GMOzWL8k3OEW7a/q5wOIS9e7t5qnGExvF5Bvlc4w/LEM4Abt+d0S5BpAHD7seMcf7+ZHfclp10TlYZc2y2nOqc6OwruxUWx0rDjNJtyp6HkUW4bJn0VWdf/a7nDpj1u++PBOR694+Ftj/8PKNdnDLn/V8YAAAAASUVORK5CYII='
	else:
		img=b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAA3NCSVQICAjb4U/gAAAACXBIWXMAAADlAAAA5QGP5Zs8AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAIpQTFRF////20lt30Bg30pg4FJc409g4FBe4E9f4U9f4U9g4U9f4E9g31Bf4E9f4E9f4E9f4E9f4E9f4FFh4Vdm4lhn42Bv5GNx5W575nJ/6HqH6HyI6YCM6YGM6YGN6oaR8Kev9MPI9cbM9snO9s3R+Nfb+dzg+d/i++vt/O7v/fb3/vj5//z8//7+////KofnuQAAABF0Uk5TAAcIGBktSYSXmMHI2uPy8/XVqDFbAAAA8UlEQVQ4y4VT15LCMBBTQkgPYem9d9D//x4P2I7vILN68kj2WtsAhyDO8rKuyzyLA3wjSnvi0Eujf3KY9OUP+kno651CvlB0Gr1byQ9UXff+py5SmRhhIS0oPj4SaUUCAJHxP9+tLb/ezU0uEYDUsCc+l5/T8smTIVMgsPXZkvepiMj0Tm5txQLENu7gSF7HIuMreRxYNkbmHI0u5Hk4PJOXkSMz5I3nyY08HMjbpOFylF5WswdJPmYeVaL28968yNfGZ2r9gvqFalJNUy2UWmq1Wa7di/3Kxl3tF1671YHRR04dWn3s9cXRV09f3vb1fwPD7z9j1WgeRgAAAABJRU5ErkJggg=='
	sg.popup_quick_message(message, title=ttl, auto_close_duration=time,no_titlebar=True, keep_on_top=True, image=img)

	#display_notification(ttl, message, img, time*1000, use_fade_in=True)

def get_cookies():
	csrf = ""
	session = ""
	user = ""

	with open("./bin/psxc.txt", "r", encoding='utf-8-sig') as f: # grab text
		raw = f.read()
		first = raw.find('|')
		csrf = raw[0:first]
		second = raw[first+1:].find('|')	
		session = raw[first+1:first+second+1]
		third = raw[second+1:].find('|')
		user = raw[first+second+2:]
	return {'xf_user':user,'xf_csrf':csrf,'xf_session':session}		

def update_list():
	os.system("python "+"./bin/download.py")
	os.system("python "+"./bin/csv2json.py")
	_gamesList, _length = read_list()
	load_list(_gamesList)

	window['-LB-'].update(MasterList)
	window['-topt-'].update(_length+" [Updated]")
	notif("Updated!", "Updated list Successfully", "success", 3)

def backup_list():
	today = date.today()
	with open("./bin/cache/list.json") as list:
		with open("./bin/cache/list_backup"+str(today.strftime("%d/%m/%Y")).replace('/', '-')+".json", "w") as write_file:
			write_file.write(list.read())
	notif("Backup", "Backup Successful", "success", 3)

def recover_from_backup():
	filepath = sg.popup_get_file('Choose from your backups', no_window=True)
	if filepath[-4:] != "json": notif("Failed", "Invalid file type, json only. you supplied "+str(filepath[-4:]), "fail", 3); return
	with open(filepath) as list:
		with open("./bin/cache/list.json", "w") as write_file:
			write_file.write(list.read())
	_gamesList, _length = read_list()
	load_list(_gamesList)
	window['-LB-'].update(MasterList)
	window['-topt-'].update(_length+" [From Backup]")
	notif("Recovery", "Recovery Successful", "success", 3)	

def read_list():
	dir = './bin/cache/list.json'
	with open(dir, 'r') as data:
			loaded = data.read()
	list = eval(loaded)
	return list, "Got "+str(len(list))+" Games"

def load_list(data):
	count = 0
	for i in data:
		count = count + 1
		#sg.one_line_progress_meter("Loading Games List", count, len(data)) #surprisingly this makes the list load slower :(
		raw = data[i]
		GameName = raw['Title']
		TitleID = raw['Title ID']
		Region = raw['Region']
		Genre = raw['Genre']
		VREnabled = raw['VR']
		DumpDate = raw['Date']

		if TitleID == "": 
			next
		else:
			obj = Item(GameName, TitleID, Region, Genre, VREnabled, DumpDate)
			MasterList.append(obj)

def read_list_cid():
	dir = './bin/cache/list_cid.json'
	with open(dir, 'r') as data:
			loaded = data.read()
	list = eval(loaded)
	return list, "Got "+str(len(list))+" Games"

def load_list_cid(data):
	count = 0
	for i in data:
		count = count + 1
		#sg.one_line_progress_meter("Loading Games List", count, len(data)) #surprisingly this makes the list load slower :(
		raw = data[i]
		TitleID = raw['Title ID']
		ContentID = raw['Content ID']
		icon0 = raw['icon0']
		if TitleID == "": 
			next
		else:
			obj = Item2(TitleID, ContentID, icon0)
			MasterCidList.append(obj)

def search(input,  genre):
	searchElements = []
	finalElements = []
	#--------------------------------#
	if input != "allgames":
		for a in MasterList:
			if a.GameName.lower().find(input.lower()) != -1:
				searchElements.append(a)
	else:
		searchElements = MasterList
	#--------------------------------#
	if genre != "All":
		for game in searchElements:
			if str(game.Genre) == genre:
				finalElements.append(game)
	else:
		finalElements = searchElements
	window['-LB-'].update(finalElements)
	#--------------------------------#

def getwp(url, cusa):
	print('Finding Page for: CUSA'+cusa, flush=True)
	links_with_text = []
	page = requests.get(url, cookies=get_cookies()) # NEEDS ACCOUNT XF COOKIES PASSED
	soup = BeautifulSoup(page.content, "html.parser")
	for a in soup.find_all('a', href=True): 
		if a.text and a['href'].find(cusa+".") != -1 and a['href'].find('post') == -1: 
			links_with_text.append(a['href'])
	return links_with_text

def setclipboard(text):
    pc.copy(text)

def getImageData(url:str):
	jpg_data = (
		cloudscraper.create_scraper(browser={"browser": "chrome", "platform": "windows", "mobile": False})
		.get(url)
		.content
	)

	pil_image = Image.open(io.BytesIO(jpg_data))
	png_bio = io.BytesIO()
	pil_image.save(png_bio, format="PNG")
	png_data = png_bio.getvalue()
	return png_data

def GetContent(siteLink, gameObj):
	print('Getting Content of link: '+siteLink, flush=True)
	links = []
	zImage = "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"
	cid = "N/A"
	PCount = "[? player]"
	Rating = '[? / 5 Stars]'
	Release = '[Released: ?]'
	B64 = []

	page = requests.get(siteLink, cookies=get_cookies()) # NEEDS ACCOUNT XF COOKIES PASSED
	soup = BeautifulSoup(page.content, "html.parser")

	tt = soup.find('h1', class_='p-title-value')
	isTested = tt.find('span', class_='label label--green')
	##################################################
	if isTested:
		testedLabel = [sg.Text('Tested', text_color='White', background_color='Green'), sg.Text('Dumped: '+gameObj.DumpDate, font='bold'), sg.Text('(MM-DD-YY)')]
	else:
		testedLabel = [sg.Text('Untested', text_color='White', background_color='Red'), sg.Text('Dumped: '+gameObj.DumpDate, font='bold'), sg.Text('(MM-DD-YY)')]
	TopFrame = [testedLabel]
	##################################################
	allA = soup.find_all('a', href=True)
	count = 0
	for a in allA:
		count = count + 1
		#sg.one_line_progress_meter("Scraping Links", count, len(allA), keep_on_top = True)
		if a['href'].find("1fichier") != -1 or a['href'].find("mediafire") != -1 or a['href'].find("mega.nz") != -1 or a['href'].find("filecrypt") != -1 or a['href'].find("drive.google") != -1:
			links.append(a['href'])
	##################################################
	allb64 = soup.find_all('div', class_='bbCodeBlock-content')
	for a in allb64:
		if isBase64(a.text):
			decoded = base64.b64decode(a.text)
			reencoded = decoded.decode('ASCII')
			B64.append(reencoded)
	##################################################
	for z in MasterCidList:
		if z.TitleID == gameObj.TitleID:
			zImage = z.icon0
			cid = z.ContentID
	if zImage != "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":
		imageLink = getImageData(zImage)
	else: imageLink = zImage

	if cid != "N/A":
		print('Getting Game Info', flush=True)
		page = requests.get("https://store.playstation.com/en-gb/product/"+cid) # NEEDS ACCOUNT XF COOKIES PASSED
		soup = BeautifulSoup(page.content, "html.parser")

		GDR = soup.find('p', class_='psw-c-t-2 psw-p-x-7 psw-p-y-6 psw-p-x-6@below-tablet-s psw-m-sub-x-7 psw-m-auto@below-tablet-s psw-c-bg-card-1')

		if str(GDR) != 'None':
			GameDesc = GDR.text
		else: GameDesc = "N / A"
		
		for item in soup.find_all():
			if "data-qa" in item.attrs:
				if item['data-qa'] == 'mfe-compatibility-notices#notices#notice1#compatText':
					PCount = ("["+item.text+"]")
				if item['data-qa'] == 'mfe-star-rating#overall-rating#average-rating':
					Rating = ("["+item.text + " / 5 Stars]")
				if item['data-qa'] == 'gameInfo#releaseInformation#releaseDate-value':
					Release = ('[Released: '+item.text+"]")


		
	else:
		GameDesc = "N / A"
	#################################################

	layout4 = [
		[sg.Titlebar(gameObj.GameName)],
		[sg.Frame('', TopFrame)],
		[sg.Frame("Game Info", [[sg.Text(PCount), sg.Text(Rating), sg.Text(Release)]])],
		[sg.Frame("Game Icon", [[sg.Image(data=imageLink, s = (175,175), subsample=3, key="-ff-")]]), sg.Frame("Description", [[sg.Multiline(GameDesc, s = (30,10), key="-gdsc-")]])]
	]

	RawFrame = []
	for i in links:
		RawFrame.append([sg.Text(i), sg.Button("Download", key=lambda: download(i))])

	for i in B64:
		RawFrame.append([sg.Text("[b64] "+i), sg.Button("Download", key=lambda: download(i))])

	if len(links) == 0 and len(B64) == 0:
		layout4.append([sg.Text('No Links Found! - Please use Open Page to confirm')])

	layout4.append([sg.Frame('', RawFrame)])
	layout4.append([sg.Frame('Actions:',[[sg.Column([[sg.Button('Exit')]], pad=(0,0))]])])
	window4 = sg.Window('Gamelist', layout4, keep_on_top=True, finalize=True)

def download(link):
	with open("./bin/apiselection.txt", "r", encoding='utf-8-sig') as f:
		apisel = f.read()
		if apisel == 'alldebrid':
			with open("./bin/apikey.txt", "r", encoding='utf-8-sig') as f: # grab text
				key = f.read()

			headers = {'User-Agent': 'Mozilla/5.0'}
			page = requests.get('http://api.alldebrid.com/v4/user?agent=myAppName&apikey='+key, headers=headers).text
			soup = BeautifulSoup(page, features='html.parser')
			jsonResponse = json.loads(page)
			#print(jsonResponse)
			print("API Authorisation "+jsonResponse['status'], flush=True)
			if jsonResponse['status'] == 'success':
				URL = 'https://api.alldebrid.com/v4/link/unlock?agent=myAppName&apikey='+key+'&link='+link
				headers = {'User-Agent': 'Mozilla/5.0', 'link': ''}
				page = requests.get(URL, headers=headers).text
				soup = BeautifulSoup(page, features='html.parser')
				jsonResponse = json.loads(page)
				if jsonResponse['status'] == 'success':
					webbrowser.open(jsonResponse['data']['link'])
				else:
					if jsonResponse['status'] == 'error':
						notif("API Error!", jsonResponse['error']['code'] + ' | ' +jsonResponse['error']['message'], "error", 10)

			else:
				notif("API Error!", "[API] - "+jsonResponse['status'], "error", 3)
		elif apisel == 'real-debrid':
			with open("./bin/apikey.txt", "r", encoding='utf-8-sig') as f: # grab text
				key = f.read()
			api_credentials = {'auth_token': key}

			r = requests.post('https://api.real-debrid.com/rest/1.0/unrestrict/link', data={'link': link}, params=api_credentials)
			webbrowser.open(r.json()['download'])
		elif apisel == 'none':
			webbrowser.open(link)

def isBase64(sb):
	try:
		if isinstance(sb, str):
			# If there's any unicode here, an exception will be thrown and the function will return false
			sb_bytes = bytes(sb, 'ascii')
		elif isinstance(sb, bytes):
			sb_bytes = sb
		else:
			raise ValueError("Argument must be string or bytes")
		return base64.b64encode(base64.b64decode(sb_bytes)) == sb_bytes
	except Exception:
		return False
#------------------------------------#

_gamesList, _length = read_list()
gamesList = load_list(_gamesList)
_gamesCidList, _cidLength = read_list_cid()
cidList = load_list_cid(_gamesCidList)

allgenres = []
allgenres.append("All")
for game in MasterList:
	GGenre = game.Genre
	if not GGenre in allgenres and GGenre != "":
		allgenres.append(GGenre)


sg.theme('dark grey 9')
#sg.theme('dark gray 12')
layout = [  
			[sg.Titlebar("PS4 fPKG List")],

    		[sg.MenubarCustom([['&Settings', ['File Download API', 'PSXHAX Credentials', 'Theme']], ['&List Options', ['Update Games', 'View New Games', '---','Backup Games List', 'Recover From Backup']], ['&Tools', ['Base64Decode']]], key = 'menu', bar_text_color = 'White', background_color = 'White')],
			[sg.Text(_length, key="-topt-", justification='center' )],
			[sg.Input(size=(35, 1), enable_events=True, default_text="Input Search...", key='-INPUT-'), sg.Combo(allgenres, expand_x=False, enable_events=True,  readonly=True, default_value = "All", key='-GENRESELECT-'), sg.Button('Clear Search')],
			[sg.Listbox(MasterList, key='-LB-', s=(67,10), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)],
			[sg.Column([[sg.Frame('Actions:',[[sg.Column([[sg.Button('Open Page'), sg.Button('Copy Link'), sg.Button('Get Content'), sg.Button('Exit')]],size=(485,45), pad=(0,0))]])]], pad=(0,0))],
			[sg.StatusBar('Coded by zbombr115', key='-STAT-')],
]

window1 = sg.Window('Coded by zbombr115', layout, keep_on_top=True, finalize=True)


while True:
	window, event, values = sg.read_all_windows()
	if window == window1 and event == sg.WIN_CLOSED:
		window1.close()
		break
	if window == window1 and event == "Exit":
		window1.close()
		break
	if window != window1 and event == "Exit":
		window.close()
	if event == sg.WIN_CLOSED or event == sg.WINDOW_CLOSED:
		window.close()
	######################################################################
	if window == window1:
		if event == 'Open Page':
			for item in values['-LB-']:
				GameName = item.GameName
				GameCUSA = item.TitleID
				CUSANumbers = GameCUSA[4:]
				a = getwp("https://www.psxhax.com/search/"+CUSANumbers+"/?q="+CUSANumbers+"&t=post&c[child_nodes]=1&c[nodes][0]=83&c[title_only]=1&o=date", CUSANumbers)

				for b in a:
					webbrowser.open("https://psxhax.com"+b)
				#<a href="/threads/05717.12551/"><span class="label label--green" dir="auto">Tested</span><span class="label-append">&nbsp;</span><em class="textHighlight">05717</em></a>
		if event == 'Get Content':
			for item in values['-LB-']:
				GameCUSA = item.TitleID
				CUSANumbers = GameCUSA[4:]
				a = getwp("https://www.psxhax.com/search/"+CUSANumbers+"/?q="+CUSANumbers+"&t=post&c[child_nodes]=1&c[nodes][0]=83&c[title_only]=1&o=date", CUSANumbers)

				for b in a:
					link = "https://psxhax.com"+b
					GetContent(link, item)
		if event == 'Copy Link':
			for item in values['-LB-']:
				GameName = item.GameName
				GameCUSA = item.TitleID
				CUSANumbers = GameCUSA[4:]
				a = getwp("https://www.psxhax.com/search/"+CUSANumbers+"/?q="+CUSANumbers+"&t=post&c[child_nodes]=1&c[nodes][0]=83&c[title_only]=1&o=date", CUSANumbers)
				link = ""
				for b in a:
					link = link+"https://psxhax.com"+b+" "		
				setclipboard(link)
				notif("Success!", "Set Link(s) to clipboard!", "success", 3)	
		if event == 'Clear Search':
			window['-INPUT-'].Update("Input Search...")
			values['-INPUT-']='Input Search...'
			window['-GENRESELECT-'].update(set_to_index = 0)
			window['-LB-'].update(MasterList)
		if event == '-GENRESELECT-':
			if values['-INPUT-'] != '' and values['-INPUT-'] != 'Input Search...':
				search(values['-INPUT-'], values['-GENRESELECT-'])
			else:
				search("allgames", values['-GENRESELECT-'])

		if values['-INPUT-'] != '' and values['-INPUT-'] != 'Input Search...':
			search(values['-INPUT-'], values['-GENRESELECT-'])
	######################################################################

	if event == 'Backup Games List':
		backup_list()
	if event == 'Recover From Backup':
		MasterList = []
		recover_from_backup()
	if event == 'File Download API':
		inp = ""
		last = [sg.Radio('alldebrid', k='-ad-', group_id=1), sg.Radio('real-debrid', k='-rd-', group_id=1), sg.Button('Exit')]
		with open("./bin/apikey.txt", "r", encoding='utf-8-sig') as f: # grab text
			inp = f.read()
		with open("./bin/apiselection.txt", "r", encoding='utf-8-sig') as f:
			sel = f.read()
			if sel == 'alldebrid':
				last = [sg.Radio('alldebrid', k='-ad-', group_id=1, default=True), sg.Radio('real-debrid', k='-rd-', group_id=1), sg.Radio('none', k='-none-', group_id=1), sg.Button('Exit')]
			elif sel == 'real-debrid':
				last = [sg.Radio('alldebrid', k='-ad-', group_id=1), sg.Radio('real-debrid', k='-rd-', group_id=1, default=True), sg.Radio('none', k='-none-', group_id=1), sg.Button('Exit')]
			elif sel == 'none':
				last = [sg.Radio('alldebrid', k='-ad-', group_id=1), sg.Radio('real-debrid', k='-rd-', group_id=1), sg.Radio('none', k='-none-', group_id=1, default=True), sg.Button('Exit')]
		layout3 = [
			[sg.Titlebar("API Key Input")],
			[sg.Column([[sg.Frame('API Key:',[[sg.Column([[sg.Input(inp, key='-API-')]],pad=(0,0))]])]], pad=(0,0))],
			last
        ]
		window4 = sg.Window('API', layout3, keep_on_top=True, finalize=True)
	if event == 'Update Games':
		MasterList = []
		update_list()
	if event == 'View New Games':
		today = date.today()

		foundDifferences = []
		maxCharLength = 0

		#d1 = today.strftime("%d/%m/%Y") #DD MM YYYY
		currentMonth = today.strftime("%m")
		currentYear = today.strftime("%Y")
		for game in MasterList:
			gameDumpDate = game.DumpDate #MM-DD-YY
			if str(gameDumpDate[0:2]) == currentMonth and str("20"+gameDumpDate[6:]) == currentYear:
				#print(game.GameName, gameDumpDate)
				foundDifferences.append("["+gameDumpDate+"] - "+game.GameName)
				if len(game.GameName) > maxCharLength: maxCharLength = len(game.GameName) # gets max length for listbox

		for index in range(1,len(foundDifferences)): # Sorts dates from 1st to last
			currentgame = foundDifferences[index]
			currentvalue = foundDifferences[index][4:6]
			position = index

			while position>0 and foundDifferences[position-1][4:6]>currentvalue:
				foundDifferences[position]=foundDifferences[position-1]
				position = position-1

			foundDifferences[position]=currentgame

		if len(foundDifferences) == 0:
			foundDifferences.append("None! Try Updating The List")
			maxCharLength = 27
		col3 = sg.Column([[sg.Frame('Options:', [[sg.Button('Open Page'), sg.Button('Get Content'), sg.Button('Exit'), sg.Button('<'), sg.Button('>')]])]]),
		layout3 = [
				[sg.Titlebar("Games dumped this month")],
				[sg.Text(str(currentMonth)+"/"+str(currentYear), key='-DATE-')],
				[sg.Listbox(foundDifferences, key='-ListBox-', s=(maxCharLength + 5 + 13,10), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)],
				[col3]
		]

		window3 = sg.Window('Gamelist', layout3, keep_on_top=True, finalize=True)
	if event == 'PSXHAX Credentials':
		inp1 = ""
		inp2 = ""
		inp3 = ""

		with open("./bin/psxc.txt", "r", encoding='utf-8-sig') as f: # grab text
			raw = f.read()
			first = raw.find('|')
			inp1 = raw[0:first]

			second = raw[first+1:].find('|')	
			inp2 = raw[first+1:first+second+1]
			third = raw[second+1:].find('|')
			inp3 = raw[first+second+2:]
		
		layout5 = [
			[sg.Titlebar("PSXHAX Credentials")],
			[sg.Column([[sg.Frame('xf_csrf:',[[sg.Column([[sg.Input(inp1, key='-csrf-')]],pad=(0,0))]])]], pad=(0,0))],
			[sg.Column([[sg.Frame('xf_session:',[[sg.Column([[sg.Input(inp2, key='-ses-')]],pad=(0,0))]])]], pad=(0,0))],
			[sg.Column([[sg.Frame('xf_user:',[[sg.Column([[sg.Input(inp3, key='-usr-')]],pad=(0,0))]])]], pad=(0,0))],
			[sg.Button('Exit'), sg.Button('Save')]
        ]
		window5 = sg.Window('PSXHAX Credentials', layout5, keep_on_top=True, finalize=True)	
	if event == 'Base64Decode':
		layout7 = [
			[sg.Titlebar("Base64")],
			[sg.Column([[sg.Frame('String:',[[sg.Column([[sg.Input('', key='-b64-')]],pad=(0,0))]])]], pad=(0,0))],
			[sg.Column([[sg.Frame('Result:',[[sg.Column([[sg.Input('', key='-b64d-')]],pad=(0,0))]])]], pad=(0,0))],
			[sg.Button('Exit'), sg.Button('Convert'), sg.Button('Download'), sg.Button('Clear')]
        ]
		window7 = sg.Window('Base64Decode', layout7, keep_on_top=True, finalize=True)	
	if event == 'Theme':
		layout6 = [
				[sg.Titlebar("Theme Select (requires restart)")],
				[sg.Text('Default theme is DarkGrey9')],
				[sg.Listbox(sg.theme_list(), key='-ListBox-', s=(20,10), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED)],
				[sg.Column([[sg.Frame('Options:', [[sg.Button('Set'), sg.Button('Exit')]])]])]
		]

		window6 = sg.Window('ThemeW', layout6, keep_on_top=True, finalize=True)			
	if callable(event): event()
	######################################################################
	if 'window3' in globals() and window == window3:
		if event == "Open Page":
			for gname in values['-ListBox-']:
				gname = gname[13:]
				for game in MasterList:
					if game.GameName == gname:
						GameName = game.GameName
						GameCUSA = game.TitleID
						CUSANumbers = GameCUSA[4:]
						a = getwp("https://www.psxhax.com/search/"+CUSANumbers+"/?q="+CUSANumbers+"&t=post&c[child_nodes]=1&c[nodes][0]=83&c[title_only]=1&o=date", CUSANumbers)
						for threadId in a:
							link = "https://www.psxhax.com"+threadId	
							webbrowser.open(link, new=0, autoraise=True)
		if event == 'Get Content':
			for gname in values['-ListBox-']:
				gname = gname[13:]
				for game in MasterList:
					if game.GameName == gname:
						GameObj = game
						GameName = game.GameName
						GameCUSA = game.TitleID
						CUSANumbers = GameCUSA[4:]
						a = getwp("https://www.psxhax.com/search/"+CUSANumbers+"/?q="+CUSANumbers+"&t=post&c[child_nodes]=1&c[nodes][0]=83&c[title_only]=1&o=date", CUSANumbers)

				for b in a:
					link = "https://psxhax.com"+b
					GetContent(link, GameObj)
		if event == '<':
			dt = window3['-DATE-'].get()
			foundDifferences = []
			maxCharLength = 0

			currentMonth = dt[0:2]
			currentYear = dt[3:]
			currentMonth = str(int(currentMonth)-1)

			if len(currentMonth) == 1:
				currentMonth = "0"+str(currentMonth)

			if currentMonth == "00" or currentMonth == "0":
				currentMonth = "12"
				currentYear = int(currentYear)
				currentYear = currentYear - 1
				currentYear = str(currentYear)

			for game in MasterList:
				gameDumpDate = game.DumpDate #MM-DD-YY
				if str(gameDumpDate[0:2]) == currentMonth and str("20"+gameDumpDate[6:]) == currentYear:
					#print(game.GameName, gameDumpDate)
					foundDifferences.append("["+gameDumpDate+"] - "+game.GameName)
					if len(game.GameName) > maxCharLength: maxCharLength = len(game.GameName) # gets max length for listbox

			for index in range(1,len(foundDifferences)): # Sorts dates from 1st to last
				currentgame = foundDifferences[index]
				currentvalue = foundDifferences[index][4:6]
				position = index

				while position>0 and foundDifferences[position-1][4:6]>currentvalue:
					foundDifferences[position]=foundDifferences[position-1]
					position = position-1

				foundDifferences[position]=currentgame
			if len(foundDifferences) == 0:
				foundDifferences.append("None! Try Updating The List")
				maxCharLength = 27
			window3['-ListBox-'].update(foundDifferences)
			window3['-ListBox-'].set_size((maxCharLength + 18, 10))
			window3["-DATE-"].update(currentMonth+"/"+str(currentYear))			
		if event == '>':
			dt = window3['-DATE-'].get()
			foundDifferences = []
			maxCharLength = 0

			currentMonth = dt[0:2]
			currentYear = dt[3:]
			if str(currentMonth) == "9" or str(currentMonth) == "09":
				currentMonth = "10"
			elif currentMonth == "12":
				currentMonth = "01"
				currentYear = int(currentYear)
				currentYear = currentYear + 1
				currentYear = str(currentYear)
			else:
				currentMonth = str(int(currentMonth)+1)

			if len(currentMonth) == 1 and currentMonth != "09": 
				currentMonth = "0"+str(currentMonth) #when month is 09 it still adds the 0 for when it becomes 10 easy fix but cba rn

			for game in MasterList:
				gameDumpDate = game.DumpDate #MM-DD-YY
				if str(gameDumpDate[0:2]) == currentMonth and str("20"+gameDumpDate[6:]) == currentYear:
					#print(game.GameName, gameDumpDate)
					foundDifferences.append("["+gameDumpDate+"] - "+game.GameName)
					if len(game.GameName) > maxCharLength: maxCharLength = len(game.GameName) # gets max length for listbox

			for index in range(1,len(foundDifferences)): # Sorts dates from 1st to last
				currentgame = foundDifferences[index]
				currentvalue = foundDifferences[index][4:6]
				position = index

				while position>0 and foundDifferences[position-1][4:6]>currentvalue:
					foundDifferences[position]=foundDifferences[position-1]
					position = position-1

				foundDifferences[position]=currentgame

			if len(foundDifferences) == 0:
				foundDifferences.append("None! Try Updating The List")
				maxCharLength = 27
			window3['-ListBox-'].update(foundDifferences)
			window3['-ListBox-'].set_size((maxCharLength + 18, 10))
			window3["-DATE-"].update(currentMonth+"/"+str(currentYear))	

	if 'window4' in globals() and window == window4:
		if values['-ad-'] == True:
			with open("./bin/apiselection.txt", "w", encoding='utf-8-sig') as f:
				f.write('alldebrid')
		elif values['-rd-'] == True:
			with open("./bin/apiselection.txt", "w", encoding='utf-8-sig') as f:
				f.write('real-debrid')
		elif values['-none-'] == True:
			with open("./bin/apiselection.txt", "w", encoding='utf-8-sig') as f:
				f.write('none')
		if '-API-' in values and values['-API-'] != "":
			with open("./bin/apikey.txt", "w") as write_file:
				write_file.write(values['-API-'])
	if 'window5' in globals() and window == window5:
		if event == 'Save':
			with open("./bin/psxc.txt", "w") as write_file:
				write_file.write(values['-csrf-']+"|"+values['-ses-']+"|"+values['-usr-'])
	if 'window6' in globals() and window == window6:
		if event == 'Set':
			print(values['-ListBox-'])
	if 'window7' in globals() and window == window7:
		if event == 'Convert':
			bval = values['-b64-']
			decoded = base64.b64decode(bval)
			reencoded = decoded.decode('ASCII')
			window['-b64d-'].update(reencoded)
		if event == 'Clear':
			window['-b64-'].update('')
			window['-b64d-'].update('')
		if event == 'Download':
			download(values['-b64d-'])