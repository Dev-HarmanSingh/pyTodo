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
    



def main():
    todo()