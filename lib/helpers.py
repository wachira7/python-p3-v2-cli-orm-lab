from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    '''get all employees stored in the database, then print each employee on a new line.'''
    employees = Employee.find_all()
    for employee in employees:
        print(employee)   

def find_employee_by_name():
    '''prompt for a name and then find the Employee instance with that name and print their information, or print an error message if the employee does not exist.'''
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    print(employee) if employee else print(
        f'Employee {name} not found')
    
def find_employee_by_id():
    '''prompt for an id and then find the Employee instance with that id and print their information, or print an error message if the employee does not exist.'''
    id_ = input("Enter the employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f'Employee {id_} not found')

def create_employee():
    '''prompt for name, job title, and department id, then create a new Employee instance with those values, and save it to the database.'''
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the employee's department id: ")
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f'Success: {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc)
    
def update_employee():
    '''prompt for an id, then find the Employee instance with that id, and update its name, job title, and department id values, and save it to the database.'''
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter the employee's new name: ")
            employee.name = name
            job_title = input("Enter the employee's new job title: ")
            employee.job_title = job_title
            department_id = input("Enter the employee's new department id: ")
            employee.department_id = department_id
            employee.update()
            print(f'Success: {employee}')
        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {id_} not found')


def delete_employee():
    '''prompt for an id, then find the Employee instance with that id, and delete it from the database.'''
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')

def list_department_employees():
    '''prompt for an id, then find the Department instance with that id, and list all the employees in that department.'''
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department.employees) if department else print(f'Department {id_} not found')
    