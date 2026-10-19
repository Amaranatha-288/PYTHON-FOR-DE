class api_fetch:
    def fetch(self):
        print("Fetching data from API...")

class database_fetch:
    def fetch(self):
        print("Fetching data from Database...")

class s3_fetch:
    def fetch(self):
        print("Fetching data from s3")


obj = api_fetch()
obj.fetch()
        