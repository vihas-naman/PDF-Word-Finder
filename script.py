import json
import pdfplumber
list1=[]
list2=[]
list3=[]
str=""
with pdfplumber.open(r'C:\Users\Vihas\Desktop\Project\random.pdf') as pdf:
    for page_no in range(len(pdf.pages)):
        curr_page = pdf.pages[page_no]
        for i in curr_page.extract_text().replace("\n",""):
            if(i!=" "):
                str+=i
            else:
                list1.append(str.strip().replace(".",""))
                str=""
        for i in range(len(list1)):
            if(list1[i]!=""):
                list2.append(list1[i])
                list3.append(list1[i])
        list1.clear()
        list2.clear()
dict1={}
for i in range(0,len(list3)):
    dict1[i+1]=list3[i]
y=json.dumps(dict1,indent=0,sort_keys=True)
with open("word.json", "w") as outfile: 
    outfile.write(y) 