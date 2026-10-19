#import time


#def fetch_data(url:str):

    #print("Fetching data from:",url)
    #time.sleep(5)
    #print("Data fetched from:",url)
    #return "Data from "+ url

#urls_list =["https://www.google.com/data1",
            #"https://www.facebook.com/data2",
            #"https://www.twitter.com/data3",
            # "https://www.linkedin.com/data4",
            #"https://www.instagram.com/data5",]

#for i in urls_list:
 #   fetch_data(i)

# Using ThreadPoolExecutor

import time
from concurrent.futures import ThreadPoolExecutor


def fetch_data(url:str):

    print("Fetching data from:",url)
    time.sleep(5)
    print("Data fetched from:",url)
    return "Data from "+ url

urls_list =["https://www.google.com/data1",
            "https://www.facebook.com/data2",
            "https://www.twitter.com/data3",
            "https://www.linkedin.com/data4",
            "https://www.instagram.com/data5",]


results = []
with ThreadPoolExecutor(max_workers=len(urls_list)) as executor:
    futures = executor.map(fetch_data,urls_list)
    results.extend(futures)

print(results)
  