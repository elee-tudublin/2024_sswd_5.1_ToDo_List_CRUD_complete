# import the model class
from app.models.todo import ToDo

# declare an emppty list to store todo items
todos_list = []

# define some sample data to display
t0 = ToDo(id=1, details="Add my 2 questions to PeerWise, then answer 10 leaving feedback.")
t1 = ToDo(id=2, details="Watch week 4 lab video.")
t2= ToDo(id=3, details="Complete week 4 lab and push to GitHub Classroom.")
t3 = ToDo(id=4, details="Learn the parts of Python I have forgotten.")

# add the same objects to the list
todos_list.append(t0)
todos_list.append(t1)
todos_list.append(t2)
todos_list.append(t3)

# returns the todo list
def dataGetTodoList() :
    return todos_list

def dataGetTodo(id : int) :
    return todos_list[id - 1]

# add a new item to the list
def dataAddTodo(details : str) :
    # generate id based on list length and set details = the param value
    new_todo = ToDo(id = len(todos_list) + 1, details = details)
    
    # add the new item to the list
    todos_list.append(new_todo)

    # return the new todo object
    return new_todo


def dataUpdateTodo(todo) :
    print(todo.model_dump())
    todos_list[todo.id - 1] = todo
    return todo
    

def dataDeleteTodo(id : int) :
    result : bool = True
    try:
        del todos_list[id - 1]
        print('deleted item with index: ' + str(id-1))
    except:
        print('error deleting item with index: ' + str(id-1))
        result = False

    return result

