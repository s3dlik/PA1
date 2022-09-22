import urllib.request, json
from multiprocessing import Pool

NUMBER_OF_PEOPLE = 10


def readFinalList(IdList):
    for i in range(len(IdList)):
        print(IdList[i])

def fetch(url):
        with urllib.request.urlopen(url) as response:
            html = response.read()
            data = json.loads(html)
            IdList = []
            IdList.append(data["Person"]["Id"])
        
        readFinalList(IdList)     



def toList(val):
    list = []
    for i in range(val):
        list.append('https://name-service.appspot.com/api/v1/names/{}.json'.format(i))
    return list

if __name__ == '__main__':
    with Pool(5) as p:
        p.map(fetch, toList(NUMBER_OF_PEOPLE))
    
