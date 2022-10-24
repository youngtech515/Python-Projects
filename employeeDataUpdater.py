class employee:
    def __init__(self,name,id_number,department):
        self.__name = name
        self.__id_number = id_number
        self.__department = department

    def get_name(self):
        return self.__name

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department
    
    def set_department(self,new_department):
        self.__department = new_department
        return self.__department
    
    def __str__(self):
        return employee.get_name(self)+"\t"+str(employee.get_id_number(self))+"\t\t"+ employee.get_department(self)

def main():
    "This is for displaying the recorded data"
    employee_data = []
    print("Name\t\tID Number\tDepartment")
    #employee 01
    employee_obj1 = employee("Michael Meyers",1264,"Sales")
    print(employee_obj1)
    #employee 02
    employee_obj2 = employee("Steve Jones",6894,"IT")
    print(employee_obj2)
    #employee 03
    employee_obj3 = employee("Gavin Rogers",2390,"Marketing")
    print(employee_obj3)

    while True:
        new_department_employee_3 = input("Enter the new department name for employee 3 : ")
        if len(new_department_employee_3)>0:
            break
        else:
            print("Please enter a department name...")
    employee_obj3.set_department(new_department_employee_3.title())
    
    #display the data again after updating
    employee_data.append(employee_obj1)
    employee_data.append(employee_obj2)
    print()
    print("Name\t\tID Number\tDepartment")
    for emp in employee_data:
        print(emp)
    print(employee_obj3)

#calling out the function 'main'
main()
