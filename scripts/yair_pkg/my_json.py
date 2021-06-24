# Create a package named as you
# Create a file for json handling
# Create 3 functions read_json(), write_json(), string_to_dict()

import os
import json

class myJSON():

    def __init__(self) -> None:
        pass

    def read_my_json(self, json_name):

        self.myfile = open('./PythonG2/scripts/yair_pkg/json_test.json',"rt")
        self.mycontent = self.myfile.read()
        self.myjson = json.loads(self.mycontent)
        print(self.myjson)
        self.myfile.close()


    def write_my_json(self, json_name,my_data):

        self.myfile = open('./PythonG2/scripts/yair_pkg/json_test.json',"wt")
        self.mycontent = self.myfile.read()
        self.myjson = json.loads(self.mycontent)
        self.myjson['prop1'] = "THIS IS THE WAY (Mandalorian)"
        self.myjson['prop3'] = "another value"
        self.myjson_dict = dict(self.myjson)
        self.myjson_dict.update({"prop5":"New Value 5", "prop6":"New Value 6"})
        self.mycontent = json.dumps(self.myjson_dict,indent=4)
        self.myfile.write(self.mycontent)
        self.myfile.close()


    def string_to_dict(self, json_name, my_string):

        self.myfile = open('./PythonG2/scripts/yair_pkg/json_test.json',"wt")
        self.mycontent = self.myfile.read()
        self.myjson = json.loads(self.mycontent)
        self.myjson_dict = dict(self.myjson)
        self.myjson_dict.update({my_string})
        self.mycontent = json.dumps(self.myjson_dict,indent=4)
        self.myfile.write(self.mycontent)
        self.myfile.close()
