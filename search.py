#Search.py
#validating values:
phone="=49-176-12345"
print(phone.startswith("+49"))

email="baraa@gmail.com"
print(email.endswith("gmail.com"))

print("@" in email) 

url="https://api.company.com/v1/data"
print("/api" in url)

#find() is great hen combined ith other methods to add dynamics
phone1="+48-176-12345"
phone2="48-654-16548"
phone3="0048-654-16548" 
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])
#find returns the starting position of a ord in the string

print(phone1.find("-"))
print(phone1[phone1.find("-"):])
print(phone1[phone1.find("-")+1:])