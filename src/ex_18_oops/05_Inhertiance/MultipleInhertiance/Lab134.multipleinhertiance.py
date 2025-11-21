class APIBase:

    def API_auth(self):
        print("Authenction API")


class DBBase:
    def DB_connect(self):
        print("Connecting to DB")


class Hybrid(APIBase, DBBase):
    def run(self):
        self.API_auth()
        self.DB_connect()
        print("Yes")

t1=Hybrid()
t1.run()
