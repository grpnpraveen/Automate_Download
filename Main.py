from datetime import datetime
import time
import wget
import os
now = datetime.now()



cu= now.strftime("%H:%M:%S")
# print("Current Time =", cu)
t=True

urls=["url1","url2"]   # in place of url1 place your direct downloadable links  
while t:
    now = datetime.now()
    cu= now.strftime("%H:%M:%S")
    print("Current Time =", cu)
    #time.sleep(3)
    if cu=="24:01:00":
        print("\n $ started Downloadings....")
        for url in range(len(urls)):
            try:
                os.system(f"wget --no-check-certificate {urls[url]}")
            except:
                pass
        print("\n $ ended the task..")
        # wget.download(url)
        t=False
print(type(cu))
print("\n $ Done ..")

