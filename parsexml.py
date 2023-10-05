import xml.etree.cElementTree as et

tree = et.parse("sample.xml")

root = tree.getroot()

Job_Title = []
Company_Name = []
Category_Name = []
City_Name = []

for title in root.iter('job_title'):
 Job_Title.append(title.text)

for company in root.iter('company_name'):
 Company_Name.append(company.text)

for category in root.iter('category'):
 Category_Name.append(category.text)

for city in root.iter('city'):
 City_Name.append(city.text)


print(Job_Title)
print(Company_Name)
print(Category_Name)
print(City_Name)