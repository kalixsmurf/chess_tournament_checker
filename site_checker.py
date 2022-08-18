import time, hashlib
from urllib.request import urlopen, Request
from pathlib import Path
home_dir = Path.home()
print(f"Process started at {time.ctime()}")
print("Welcome to site checker")
city_list = ["adana",
"adiyaman",
"afyon",
"agri",
"amasya",
"ankara",
"antalya",
"artvin",
"aydin",
"balikesir",
"bilecik",
"bingol",
"bitlis",
"bolu",
"burdur",
"bursa",
"canakkale",
"cankiri",
"corum",
"denizli",
"diyarbakir",
"edirne",
"elazig",
"erzincan",
"erzurum",
"eskisehir",
"gaziantep",
"giresun",
"gumushane",
"hakkari",
"hatay",
"isparta",
"mersin",
"istanbul",
"izmir",
"kars",
"kastamonu",
"kayseri",
"kirklareli",
"kirsehir",
"kocaeli",
"konya",
"kutahya",
"malatya",
"manisa",
"kahramanmaras",
"mardin",
"mugla",
"mus",
"nevsehir",
"nigde",
"ordu",
"rize",
"sakarya",
"samsun",
"siirt",
"sinop",
"sivas",
"tekirdag",
"tokat",
"trabzon",
"tunceli",
"sanliurfa",
"usak",
"van",
"yozgat",
"zonguldak",
"aksaray",
"bayburt",
"karaman",
"kirikkale",
"batman",
"sirnak",
"bartin",
"ardahan",
"igdir",
"yalova",
"karabuk",
"kilis",
"osmaniye",
"duzce"]
cache = open(f"{home_dir}/Desktop/checker/storing.txt", "w", encoding="utf-8")
hash_logs = open(f"{home_dir}/Desktop/checker/hash_logs.txt", "a", encoding="utf-8")
hash_logs.write("\nNew hashes\n")
hash_logs.write(f"Date:{time.ctime()}"+'\n')
for i in city_list:
    url_to_check = Request(f"http://{i}.tsf.org.tr/", headers={"User-Agent": "Chrome/91.0.4472.124"})
    response = urlopen(url_to_check).read()
    currentHash = hashlib.sha224(response).hexdigest()
    print("Hash is added.")
    time.sleep(0.5)
    cache.write(currentHash+"\n")
    hash_logs.write(currentHash+"\n")
hash_logs.close()
cache = open(f"{home_dir}/Desktop/checker/cache.txt", "r")
storing = open(f"{home_dir}/Desktop/checker/storing.txt", "r")
#storing should exist before the process.#
current_lines_list = cache.readlines()
old_lines_list = storing.readlines()
for i in range(0, 81):
    if len(old_lines_list) == 0:
        pass
    elif current_lines_list[i] == old_lines_list[i]:
        pass
    elif current_lines_list[i] != old_lines_list[i]:
        print("There is a change in %s" % city_list[i])
print("Collecting data for further requests!")
cache.close()
storing.close()
storing = open(f"{home_dir}/Desktop/checker/storing.txt", "w", encoding="utf-8")
for i in city_list:
    url_to_check = Request(f"http://{i}.tsf.org.tr/", headers={"User-Agent": "Chrome/91.0.4472.124"})
    response = urlopen(url_to_check).read()
    currentHash = hashlib.sha224(response).hexdigest()
    storing.write(currentHash+"\n")
print("Data for the next run have been prepared.")
print("Necessary calculations are done!")
print("\nThank you for using my programme!")
#This programme is written by Kalixsmurf.