class stud:
    def __init__(self,name,roll,sgpa,cgpa):
        self.name=name
        self.roll=float(roll)
        self.sgpa=float(sgpa)
        self.cgpa=float(cgpa)
    def __lt__(self,other):
        if other.sgpa<self.sgpa:
            return False
        else:
            if other.sgpa>self.sgpa:
                return True
            else:
                return self.roll<other.roll

students=[]        
for line in open('results.in'):
    t=line.split()
    if t==[] or 'Roll' not in t[0]:
        break
    students.append(stud(t[1].split(':')[1]+" "+t[2],t[0].split(':')[1],t[-2].split(':')[1],t[-1].split(':')[1]))
count=0
for i in sorted(students, reverse=True):
    print count,":", i.roll, i.name,i.sgpa, i.cgpa
    count+=1

