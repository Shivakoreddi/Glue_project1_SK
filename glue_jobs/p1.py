import csv
import json
import re
import io

def readFile(file):
    with open(file,'r') as f:
        data = csv.reader(f)
    for row in data:
        print(row)


path = '/Users/sravss/Documents/PyScripts/annual_survey_2021.csv'


def readFive(file):
    with open(file,'r') as f:
        data = csv.reader(f)
    counter = 0
    for row in data:
        print(row)
        if counter<5:
            counter+=1
        else:
            break


def readHead(file):
    with open(file,'r') as f:
        data = csv.reader(f)
    header = next(data)
    return header




raw_data1 = """[{"id":101,"name":"john_snow","marks":[10,20,30]},
{"id":102,"name":"cersy_lansiter","marks":[10,10,10]},
{"id":103,"name":"arya_stark","marks":[15,10,30]},
{"id":104,"name":"sansa_stark","marks":[10,20,20]}]"""

def readRaw1(raw):
    data = json.loads(raw)
    for i in data:
        print(i)

#readRaw1(raw_data1)




def readRaw2(raw):
    data = json.loads(raw)
    for i in data:
        first,last = i['name'].split("_")
        print(first,last)

#readRaw2(raw_data1)


def readRaw3(raw):
    data = json.loads(raw)
    print("First","Total_Marks")
    for i in data:
        total_marks = sum(i['marks'])
        first,last = i['name'].split("_")
        print("____________________")
        print(first,total_marks)

readRaw3(raw_data1)


raw_data2 = """[{"id":101,"name":"cersy$lansiter","marks":[10,20,30]},
{"id":102,"name":"cersy$lansiter","marks":[10,10,10]},
{"id":103,"name":"arya_stark","marks":[15,10,30]},
{"id":104,"name":"sansa_stark","marks":[10,20,20]}]"""

def readRaw4(raw):
    data = json.loads(raw)
    for i in data:
        first,last = re.split("_",i['name'])
        print(first,last)

#readRaw4(raw_data2)





#*problemss:
#1. read strings in row and try to verify if string is not having any special char











        
        
    
        
