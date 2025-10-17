#You want to check whether a web page loads within 3 seconds (performance test condition).

#load_time = 4.2
#⚠️ Page load too slow: 4.2 seconds


load_time=float(input("Load Time:"))

if load_time<=3.0:
    print("Page load fine:",load_time,"seconds")
else:
    print("Page load too slow:",load_time,"seconds")