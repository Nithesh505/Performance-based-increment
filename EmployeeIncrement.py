class Employee:
    #class variable
    company_name="TCS"
    employee=0

    def __init__(self,emp_id,name,salary,performance):
        self.details={"Emp_id":emp_id,"name":name,"salary":salary,"performance":performance}
        Employee.employee+=1
    #instance method
    def detail(self):
        print(f"\n{self.details['name']}'s original salary:{self.details['salary']}") 
        print("Performance Score:",self.details["performance"])
        self.increment=self.details["salary"]*Employee.performance_sc(self.details["performance"])/100
        if self.increment>0:

         print(f"Increment Apllied:{Employee.performance_sc(self.details["performance"])}%")
         
         self.details["salary"]+=self.increment
         print("New Salary:",self.details["salary"])
        else:
            print("NO INCREMENT DUE TO LOW PERFORMANCE")
    #static method
    @staticmethod
    def performance_sc(score):
        
        if score>=90:
            return 30
        elif score>=75:
            return 20 
        elif score>=60:
            return 10
        else:
            return 0
        
     
    #class method
    @classmethod
    def company(cls):
        print("Company name:",cls.company_name)
        print("No.of Employees:",Employee.employee)
emp1=Employee(102,"Vinay",50000,90)
emp2=Employee(103,"Dillip",60000,78)
emp3=Employee(104,"Nithesh",45000,59)

Employee.company()

emp1.detail()
emp2.detail()
emp3.detail()






        
