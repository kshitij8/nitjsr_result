from selenium import webdriver
from selenium.webdriver.support.ui import Select

url="http://117.211.91.61/web/Default.aspx"
semester="V"

subjects={}
score={}

browser=webdriver.Firefox()

branch='cs'
batch='11'

for i in range(1,600):
    browser.get(url)
    regno=browser.find_element_by_id("txtRegno")
    rollno='0'*(3-len(str(i)))+str(i)
    
    registration=branch+'1'+batch+rollno
    
    regno.send_keys(registration)
    
    show=browser.find_element_by_id("btnimgShow")
    show.click()

    try:
        sem=Select(browser.find_element_by_id("ddlSemester"))
    except:
        continue
    
    #sem.deselect_all()
    sem.select_by_visible_text(semester)

    result=browser.find_element_by_id("btnimgShowResult")
    result.click()

    data=browser.find_element_by_id("PnlShowResult").text.split('\n')

    score[registration]={"name": browser.find_element_by_id("lblSName").text}
    score[registration]["data"]=data
    score[registration]["grades"]={}
    
    j=5
    while j<len(data):
        #print data[j].split()
        if data[j].split()[0]=="Result":
            score[registration]["SGPA"]=data[j].split()[-3]
            score[registration]["CGPA"]=data[j].split()[-1]
            break
            
        sub_code=data[j].split()[0]
        sub_name=" ".join(data[j].split()[1:-1])
        subjects[sub_code]=sub_name

        find=j+1
        while True:
            try:
                int(data[find][0])
            except:
                break
            find+=1

        score[registration]["grades"][sub_code]=data[find-1].split()[-1]
        
        j=find
   
    print "RollNo:%-3s Name:%-30s"%(rollno,score[registration]["name"]),
    
    for j in sorted(score[registration]["grades"].keys()):
        print j+":"+score[registration]["grades"][j],
        
    print "SGPA:"+score[registration]["SGPA"],"CGPA:"+score[registration]["CGPA"]

print "\nSubject Code Keys:"
for j in sorted(subjects.keys()):
    print "%s: %s"%(j,subjects[j])
    



