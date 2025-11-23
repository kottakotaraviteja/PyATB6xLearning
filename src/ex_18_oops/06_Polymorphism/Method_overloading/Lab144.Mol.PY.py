class Browser:
    def name(self,url):
        print("Hi,",url)

    def name(self,url,auth="yes"):
        print("Hi,",url,auth)

c=Browser()
c.name("http://google.com","No")