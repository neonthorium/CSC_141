from employee import Employee

def test_give_default_raise():
    employee = Employee('susan', 'doe', 55_000)
    employee.give_raise()
    assert employee.salary == 60_000

def test_give_custom_raise():
    employee = Employee('susan', 'doe', 55_000)
    employee.give_raise(10000)
    assert employee.salary == 65_000