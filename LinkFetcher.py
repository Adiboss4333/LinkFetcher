import re,urllib
data = urllib.request.urlopen("https://thelowendgpugames.000webhostapp.com/")
data = data.read().decode()
ls = re.findall('href="https://.+?"',data)
DATA = ""
for i in ls:
    DATA+="<a "+i+">Link</a>"+"\n"
DATA = DATA.strip()
with open("HTML.html",'w') as file:
    file.write(DATA)
    file.close()
print("All the links have been saved in a html file in the same directory")