import socket
import pandas as pd

df=pd.read_csv("top-1m.csv",names=['sno','websites'])
df = pd.DataFrame(df.websites.str.split('.',1).tolist(),columns = ['name','domain'])
ls=df.name.values.tolist()
pop=False


def find_ip(url):
    try:
        res=socket.gethostbyname(url)
        return res
    except Exception as e:
        print(e)
        return 'IP not Found'

def popular(url):
    #df.drop_duplicates(subset ="name",keep = False, inplace = True) 
    s=url.strip('www., .com,.co,.in, en.,.en')
    if  s in ls:
        pop=True
        return pop
    else:
        pop=False
        return pop

def domain(url):
    sub=url.split('.')
    if 'www' in sub:
        return 'www'
    else :
        return "no domain"

#def typo(url):
    #a = set(map(str,url.split[1]))
    #for url in ls:
        #b=set(map(str,url.split('.')[1]))
        #print(b)
    # b = set(map(str,word2))
    # c = a.intersection(b)
    # return float(len(c)) / (len(a) + len(b) -  len(c))

def typo(url):
    lk=url.split('.')[1]
    l=[i for i in ls if len(lk)==len(i)]
    l=list(set(l))
    lst=[]
    a = set(map(str,url.split('.')[1]))
    for k in l:
        b=set(map(str,k))
        c = a.intersection(b)
        lst.append(float(len(c)) / (len(a) + len(b) -  len(c)))
    print(max(lst))
    return max(lst)

def check(url):
    lst=url.split('.')
    if len(lst)<=3:
        return "no"
    else:
        return "yes"

