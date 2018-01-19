import webbrowser
import time
print("This program started on"+time.ctime())
loop=0
while (loop<3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=hMiHGkzr3ZQ&list=RDhMiHGkzr3ZQ")
    loop=loop+1
