import re
import sys
def finisher(str):
    calc_out = open("calc.out", "w+")
    calc_out.write(str)
    calc_out.close()
    sys.exit()
fhand=open("calc.in")
line_lst=[]
for line in fhand:
    line_lst.append(line.rstrip())
fhand.close()
counter={}
counter2={"AnaDegiskenler": 0,"YeniDegiskenler": 0,"Sonuc": 0}
keywords=["0","1","2","3","4","5","6","7","8","9","sifir","bir","iki","uc","dort","bes","alti","yedi","sekiz","dokuz",
          "degeri","nokta","ac-parantez","kapa-parantez","(",")","dogru","yanlis","+","*","-","arti",
          "eksi","carpi","ve","veya","olsun"]
converter={"sifir":"0","bir": "1","iki":"2","uc":"3","dort":"4","bes":"5","alti":"6","yedi":"7","sekiz":"8",
           "dokuz":"9"," nokta ":".","arti":"+","eksi":"-","carpi":"*"}
for line in line_lst:
    if line in ["AnaDegiskenler","YeniDegiskenler","Sonuc"]:
        counter2[line]+=1
        if line=="Sonuc":
            break
    if len(line.split())!=0 and (line not in ["AnaDegiskenler","YeniDegiskenler","Sonuc"]):
        counter[line.split()[0]]=counter.get(line.split()[0],0)+1
for k in counter.keys():
    x=re.search(r".{11,}|\W|_",k)
    if k in keywords or x!=None :
        finisher("Dont Let Me Down")
for k,v in counter.items():
    if v!=1:
        finisher("Dont Let Me Down")
for k,v in counter2.items():
    if v!=1:
        finisher("Dont Let Me Down")
syn_lst=[x for x in line_lst if x!=""]
ad_end=syn_lst.index("YeniDegiskenler")
yd_end=syn_lst.index("Sonuc")
s_end=len(syn_lst)
ad=[syn_lst[i] for i in range(1,ad_end)]
yd=[syn_lst[i] for i in range(ad_end+1,yd_end)]
s=[syn_lst[i] for i in range(yd_end+1,len(syn_lst))]
for el in ad:
    x=re.search(r"\s+degeri\s+(?:\d|sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)\s+olsun\s*",el)
    y=re.search(r"\s+degeri\s+(?:dogru|yanlis)\s+olsun\s*",el)
    z=re.search(r"\s+degeri\s+(?:\d\.\d|(?:sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz)\s+nokta\s+(?:sifir|bir|iki|uc|dort|bes|alti|yedi|sekiz|dokuz))\s+olsun\s*",el)
    if (x or y or z) == None:
        finisher("Dont Let Me Down")
conf_yd=[]
for el in yd:
    x = re.search("ac-parantez|\(",el)
    y = re.search("kapa-parantez|\)",el)
    if (x!=None and y != None) and (x.span()>y.span()):
        finisher("Dont Let Me Down")
    x=re.findall(r"ac-parantez|\(",el)
    y=re.findall(r"kapa-parantez|\)",el)
    if len(x)!=len(y):
        finisher("Dont Let Me Down")
    el = re.sub("ac-parantez|\(","(", el)
    el = re.sub("kapa-parantez|\)",")", el)
    check=re.search(r"\(\s*\)",el)
    if check!=None:
        finisher("Dont Let Me Down")
    el = re.sub("ac-parantez|\(", "", el)
    el = re.sub("kapa-parantez|\)", "", el)
    el = re.sub(r"(?<=\W)sifir(?=\W)", f"{converter['sifir']}", el)
    el = re.sub(r"(?<=\W)bir(?=\W)", f"{converter['bir'] }", el)
    el = re.sub(r"(?<=\W)iki(?=\W)", f"{converter['iki'] }", el)
    el = re.sub(r"(?<=\W)uc(?=\W)", f"{converter['uc'] }", el)
    el = re.sub(r"(?<=\W)dort(?=\W)", f"{converter['dort'] }", el)
    el = re.sub(r"(?<=\W)bes(?=\W)", f"{converter['bes'] }", el)
    el = re.sub(r"(?<=\W)alti(?=\W)", f"{converter['alti'] }", el)
    el = re.sub(r"(?<=\W)yedi(?=\W)", f"{converter['yedi'] }", el)
    el = re.sub(r"(?<=\W)sekiz(?=\W)", f"{converter['sekiz'] }", el)
    el = re.sub(r"(?<=\W)dokuz(?=\W)", f"{converter['dokuz'] }", el)
    el = re.sub(r"\s+nokta\s+", f"{converter[' nokta '] }", el)
    el = re.sub(r"(?<=\W)arti(?=\W)", f"{converter['arti'] }", el)
    el = re.sub(r"(?<=\W)eksi(?=\W)", f"{converter['eksi'] }", el)
    el = re.sub(r"(?<=\W)carpi(?=\W)", f"{converter['carpi'] }", el)
    conf_yd.append(el)
conf_ad=[]
for el in ad:
    el = re.sub(r"(?<=\W)sifir(?=\W)", f"{converter['sifir']}", el)
    el = re.sub(r"(?<=\W)bir(?=\W)", f"{converter['bir']}", el)
    el = re.sub(r"(?<=\W)iki(?=\W)", f"{converter['iki']}", el)
    el = re.sub(r"(?<=\W)uc(?=\W)", f"{converter['uc']}", el)
    el = re.sub(r"(?<=\W)dort(?=\W)", f"{converter['dort']}", el)
    el = re.sub(r"(?<=\W)bes(?=\W)", f"{converter['bes']}", el)
    el = re.sub(r"(?<=\W)alti(?=\W)", f"{converter['alti']}", el)
    el = re.sub(r"(?<=\W)yedi(?=\W)", f"{converter['yedi']}", el)
    el = re.sub(r"(?<=\W)sekiz(?=\W)", f"{converter['sekiz']}", el)
    el = re.sub(r"(?<=\W)dokuz(?=\W)", f"{converter['dokuz']}", el)
    el = re.sub(r"\s+nokta\s+", f"{converter[' nokta ']}", el)
    el = re.sub(r"(?<=\W)arti(?=\W)", f"{converter['arti']}", el)
    el = re.sub(r"(?<=\W)eksi(?=\W)", f"{converter['eksi']}", el)
    el = re.sub(r"(?<=\W)carpi(?=\W)", f"{converter['carpi']}", el)
    conf_ad.append(el)
varnames=list(counter.keys())
vartypes=dict()
all_d=conf_ad+conf_yd+s
for varname in varnames:
    x= re.search("[*+-.]|(?:\s+\d\s+)",all_d[varnames.index(varname)])
    y=re.search(" veya | ve | dogru | yanlis ",all_d[varnames.index(varname)])
    if x!=None:
        vartypes[varname]="int_float"
    elif y!=None:
        vartypes[varname]="boolean"
    else:
        vartypes[varname]="undefined"
    if ((x!=None and x.group()!='') and (y!=None and y.group()!='')):
        finisher("Dont Let Me Down")
for el in yd:
    el = re.sub("ac-parantez", "(", el)
    el = re.sub("kapa-parantez", ")", el)
    x=re.search(r"(?:[()]\S)|(?:\S[()])",el)
    y=re.search(r"(?:\S[*+-])|(?:[*+-]\S)",el)
    if ( x or y ) != None:
        finisher("Dont Let Me Down")
for el in conf_yd:
    x = re.search(r"\s+degeri\s+(?:(?:\d|(?:\d\.\d))|\w{1,10})\s+(?:[*+-])\s+(?:(?:\d|(?:\d\.\d))|\w{1,10})(?:\s+(?:[*+-])\s+(?:(?:\d|(?:\d\.\d))|\w{1,10}))*\s+olsun\s*",el)
    y = re.search(r"\s+degeri\s+(?:dogru|yanlis|\w{1,10})\s+(?:veya|ve)\s+(?:dogru|yanlis|\w{1,10})(?:\s+(?:veya|ve)\s+(?:dogru|yanlis|\w{1,10}))*\s+olsun\s*", el)
    z = re.search(r"\s+degeri\s+(?:\d|\d\.\d||\w{1,10})\s+olsun\s*", el)
    k = re.search(r"\s+degeri\s+(?:dogru|yanlis|\w{1,10})\s+olsun\s*", el)
    t= re.findall("\s+degeri(\s+.*\s+)olsun\s*",el)
    for tel in t:
        tel= re.sub(r"[*+-]","  ",tel)
        tel = re.sub(r" \d ", "  ", tel)
        tel = re.sub(r" \d\.\d ", "  ", tel)
        tel = re.sub(r" dogru ", "  ", tel)
        tel = re.sub(r" yanlis ", "  ", tel)
        tel = re.sub(r" veya ", " ", tel)
        tel = re.sub(r" ve ", " ", tel)
        tel=str(tel)
        tel=tel.split()
        if len(tel)==0:
            continue
        line_num=len(ad)+conf_yd.index(el)+1
        for subel in tel:
            if subel not in list(counter.keys())[:line_num]:
                finisher("Dont Let Me Down")
            if vartypes[subel] != vartypes[varnames[line_num-1]]:
                if vartypes[varnames[line_num-1]]=="undefined":
                    vartypes[varnames[line_num-1]]=vartypes[subel]
                else:
                    finisher("Dont Let Me Down")
    if ( x or y or z or k ) == None:
        finisher("Dont Let Me Down")
if len(s)>1:
    finisher("Dont Let Me Down")
conf_s=[]
if len(s)==1:
    s[0] = "degeri " + s[0] + " olsun"
for el in s:
    el = re.sub("ac-parantez|\(","(", el)
    el = re.sub("kapa-parantez|\)",")", el)
    check=re.search(r"\(\s*\)",el)
    if check!=None:
        finisher("Dont Let Me Down")
    el = re.sub("ac-parantez|\(", "", el)
    el = re.sub("kapa-parantez|\)", "", el)
    el = re.sub(r"(?<=\W)sifir(?=\W)", f"{converter['sifir']}", el)
    el = re.sub(r"(?<=\W)bir(?=\W)", f"{converter['bir']}", el)
    el = re.sub(r"(?<=\W)iki(?=\W)", f"{converter['iki']}", el)
    el = re.sub(r"(?<=\W)uc(?=\W)", f"{converter['uc']}", el)
    el = re.sub(r"(?<=\W)dort(?=\W)", f"{converter['dort']}", el)
    el = re.sub(r"(?<=\W)bes(?=\W)", f"{converter['bes']}", el)
    el = re.sub(r"(?<=\W)alti(?=\W)", f"{converter['alti']}", el)
    el = re.sub(r"(?<=\W)yedi(?=\W)", f"{converter['yedi']}", el)
    el = re.sub(r"(?<=\W)sekiz(?=\W)", f"{converter['sekiz']}", el)
    el = re.sub(r"(?<=\W)dokuz(?=\W)", f"{converter['dokuz']}", el)
    el = re.sub(r"\s+nokta\s+", f"{converter[' nokta ']}", el)
    el = re.sub(r"(?<=\W)arti(?=\W)", f"{converter['arti']}", el)
    el = re.sub(r"(?<=\W)eksi(?=\W)", f"{converter['eksi']}", el)
    el = re.sub(r"(?<=\W)carpi(?=\W)", f"{converter['carpi']}", el)
    conf_s.append(el)
for el in conf_s:
    x = re.search(r"degeri\s+(?:(?:\d|(?:\d\.\d))|\w{1,10})\s+(?:[*+-])\s+(?:(?:\d|(?:\d\.\d))|\w{1,10})(?:\s+(?:[*+-])\s+(?:(?:\d|(?:\d\.\d))|\w{1,10}))*\s+olsun\s*",el)
    y = re.search(r"degeri\s+(?:dogru|yanlis|\w{1,10})\s+(?:veya|ve)\s+(?:dogru|yanlis|\w{1,10})(?:\s+(?:veya|ve)\s+(?:dogru|yanlis|\w{1,10}))*\s+olsun\s*", el)
    z = re.search(r"degeri\s+(?:\d|\d\.\d||\w{1,10})\s+olsun", el)
    k = re.search(r"degeri\s+(?:dogru|yanlis|\w{1,10})\s+olsun", el)
    if ( x or y or z or k ) == None:
        finisher("Dont Let Me Down")
if len(conf_s)!=0:
    x = re.search(r"[*+.-]||(?:\s+\d\s+)",conf_s[0])
    y = re.search(" veya | ve | dogru | yanlis ", conf_s[0])
    if x!=None:
        vartyp_sonuc="int_float"
    if y!=None:
        vartyp_sonuc = "boolean"
    if ((x!=None and x.group()!='') and (y!=None and y.group()!='')):
        finisher("Dont Let Me Down")
    conf_s[0]= re.sub(r"[*+-]","  ",conf_s[0])
    conf_s[0]= re.sub(r" \d ", "  ", conf_s[0])
    conf_s[0] = re.sub(r" \d\.\d ", "  ", conf_s[0])
    conf_s[0] = re.sub(r" dogru ", "  ", conf_s[0])
    conf_s[0] = re.sub(r" yanlis ", "  ", conf_s[0])
    conf_s[0] = re.sub(r" veya ", "  ", conf_s[0])
    conf_s[0] = re.sub(r" ve ", "  ", conf_s[0])
    conf_s[0] = re.sub(r"degeri ", "  ", conf_s[0])
    conf_s[0] = re.sub(r" olsun", "  ", conf_s[0])
    conf_s[0]=str(conf_s[0])
    conf_s[0]=conf_s[0].split()
    conf_s=conf_s[0]
    for el in conf_s:
        if el not in list(counter.keys()):
            finisher("Dont Let Me Down")
    for i in range(len(all_d)-(len(ad)+len(yd))+1):
        if len(conf_s) > 1:
            if (vartypes[(conf_s[i])]) != vartyp_sonuc:
                finisher("Dont Let Me Down")
finisher("Here Comes the Sun")