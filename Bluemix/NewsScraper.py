
# coding: utf-8

# In[1]:

from apiclient.discovery import build
import csv
import string

f = open('RedCross.csv', 'a')

writer = csv.writer(f, delimiter=",")

def main():
    service = build("customsearch", "v1", developerKey="AIzaSyBcPPP97y2UMiqz-5IyyEc03PEdJ8B9t7U")

    for i in range(1, 51, 10):
        res = service.cse().list(q='red cross',cx='004738432725228603787:meerig-7ppg',start=i, num=10).execute()
        
        for obj in res.get("items"):
            strLink = obj.get("link")
            writer.writerow([strLink])
    
    f.close()

if __name__ == '__main__':
    main()

