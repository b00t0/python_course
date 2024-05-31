

def func(**kwargs):
    return f"Employee: {kwargs['name']}, {kwargs['surname']}, {kwargs['age']}"

print(func(name="Ivan", surname="Ivanov", age=18))