import requests
import json

payload = {
    "filter[>ID]": "0",
    "select[0]": 'ID',
    "select[1]": 'TITLE',
    "select[2]": 'DATE_CREATE'

}
r = requests.post('https://b24-q6xa77.bitrix24.ru/rest/1/5kwccacplmtdw0pp/crm.deal.list.json', data=payload)

if r.status_code == 200:
    j = r.json()
    print(json.dumps(r.json(), indent=4, sort_keys=True))
    print(r.headers)
    for el in j["result"]:
        print(el["TITLE"])

else:
    print("Error with http code: {0}".format(r.status_code))



class JobRegistry:
    def __init__(self):
        self.jobs = {
            "BitrixJob": BitrixJob()
        }

    def getJob(self, name):
        return self.jobs[name]

class Job:
    def run(self):


class Extractor:
    def extract(self):



class Transformer:
    def transfom(self, data):
        return ...

class Loader:
    def load(self):
        print(....)

class ConsoleLoader(Loader):
    def load(self):
        print(....)

class DealsAndCompaniesTransformer(Transformer):
    def transfom(self, data):
        return ...

class DealsExtractor(Extractor):
    def extract(self):

class CompaniesExtractor(Extractor):
    def extract(self):


class BitrixJob(Job):
    def run(self):
        deals_extractor = DealsExtractor()
        companies_extractor = CompaniesExtractor()
        transformer = DealsAndCompaniesTransformer()
        deals = deals_extractor.extract()
        companies = companies_extractor.extract()
        transformed = transformer.transfom([deals, companies])
        loader = ConsoleLoader()
        loader.load(transformed)



"""main"""
JobRegistry().getJob("BitrixJob").run()


