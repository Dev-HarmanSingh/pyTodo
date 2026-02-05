import click
import json

DB_NAME = "todos.json"
def open_db()->dict:
    try:
        with open(DB_NAME, 'r') as db:
            return json.load(db)
    except:
        return {"MISC":[], "DAILY":[]}

def save_db(db_data:dict):
    with open(DB_NAME, 'w') as db:
        json.dump(db_data, db)

@click.group()
def todo():
    pass


# Add your code here while using @todo.command()
def default_list_name_helper(data):
    i = 1
    while True:
        for key in data:
            if key==f"LIST{i}":
                i += 1
                continue
            return i
@todo.command()
@click.option('--name', default="!$$$LOOP-CHECK$$$!", help="adds a new list in your todo list. do not set name as`!$$$LOOP-CHECK$$$!` as it will break internal working")
def add_list(name):
    data = open_db()
    if name=="!$$$LOOP-CHECK$$$!":
        data[f"LIST{default_list_name_helper(data)}"] = []
    else:
        data[name.upper()] = []
    save_db(data)
    return

@todo.command()
@click.option('--list','todolist', default="MISC", type=str)
@click.argument('todo', type=str)
def add_todo(todo:str, todolist:str,):
    data = open_db()
    new_todo = {
        'item' : todo,
        'done' : False,
    }
    data[todolist.upper()].append(new_todo)
    save_db(data)


@todo.command()
@click.option('--list', 'listname', default=None, type=str)
def list_todos(listname):
    data = open_db()

    if not listname:
        click.echo("\nTODOS\n")
        for i, l in enumerate(data, start=1):
            click.echo(f"{i}. {l}")
        return
    
    click.echo(f"\n{listname.upper()}\n")
    for i, todo in enumerate(data[listname.upper()], start=1):
        click.echo(f"{i}.[{'x' if todo['done'] else ' '}]  {todo['item']}")
    click.echo()
    return

@todo.command()
@click.option('--list', 'listname', type=str)
@click.option('--index', type=int)
def complete(listname, index):
    data = open_db()
    try:
        data[listname.upper()][index-1]['done'] = True
    except:
        click.echo("invalid command")
    save_db(data)

@todo.command()
@click.option('--list', 'listname')
def clear(listname):
    data = open_db()
    for todo in data[listname.upper()]:
        if not todo['done']:
            continue
        data[listname.upper()].remove(todo)
    save_db(data)
    return

@todo.command()
@click.argument('listname')
def rmlist(listname):
    if listname.upper() == 'MISC' or listname.upper() == 'DAILY':
        click.echo("You are not supposed to delete this todo")
        return
    data = open_db()
    if listname.upper() not in data:
        click.echo("There is no such list")
        return
    data.pop(listname.upper())
    save_db(data)
    return

@todo.command()
@click.option('--list', 'listname', type=str)
@click.option('--index', type=int)
def rmtodo(listname, index):
    data = open_db()
    todolist = data[listname.upper()]
    try:
        todolist_item = todolist[index-1]
        todolist.remove(todolist_item)
    except:
        click.echo("invalid command")
    save_db(data)
    return

def main():
    todo()