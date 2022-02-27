import re

na='''
Suraj is 22 and Sura is 21
Muraj is 32 and Mura is 31
Nuraj is 32 and Nura is gh 0
'''
print (na)

age= re.findall(r'\d{1,2}',na)
name= re.findall(r'[A-Z][a-z]*',na)
agedict={}
x=0
for a in age :
    agedict[a]=name[x]
    x+=1
print(agedict)
