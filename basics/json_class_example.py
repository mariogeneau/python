from JsonClass import JsonClass

obj = JsonClass()
emp = obj.loadjsonFile("basics/employees.json")
emp["Employee"]["phone"] = "734-294-8340"
obj.saveJsonFile("basics/employees.json", emp)