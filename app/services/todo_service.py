from app.data_access.todo_dba import dataGetTodoList, dataGetTodo, dataAddTodo, dataUpdateTodo, dataDeleteTodo
from app.models.todo import ToDo

# get list of todos from data
def getAllTodos() :
    return dataGetTodoList()

# add new todo using data access
def addTodo(item : str) :    
    # add todo to the list (via dataaccess)
    new_todo = dataAddTodo(item)

    # return new todo
    return new_todo
    
def getTodo(id : int) :
       todo : ToDo = dataGetTodo(id)
       return todo

def updateTodo(id: int, details : str, completed : str) :
     
     comp : bool = False
     
     if completed == 'completed' :
          comp = True

     item = ToDo(id=id, details=details, completed=comp)     

     updated = dataUpdateTodo(item)
     return updated


def deleteTodo(id : int) :
    result = dataDeleteTodo(id)

