#!/usr/bin/python3
"""contains entry point of the command interpreter
"""
import cmd
import datetime
from models.base_model import BaseModel
from models import storage
class HBNBCommand(cmd.Cmd):
    """command line interprete

    Args:
        cmd (_cmd_): _python module for CLI interpretion_
    """
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel}

    def do_quit(self, args):
        """quit command exits out of the command interpreter

        Args:
            args (_str_): _any argument in cli_
        """
        quit()

    def do_EOF(self, args):
        """_EOF command exits out of the command interpreter_

        Args:
            args (_str_): _any argument in cli_
        """
        quit()

    def do_help(self, args):
        """_list all help details for each command_

        Args:
            args (_str_): _any argument in cli_
        """
        cmd.Cmd.do_help(self, args)

    def emptyline(self):
        """returns back to prompt when line is empty and enter is pressed
        """
        return

    def do_create(self, args):
        """creates a new instance of any class

        Args:
            args (_str_): _name of a class in AirBnB_
        """
        if not args:
            print("** class name missing **")
        args = args.split(' ')
        if len(args) == 1 and args[0] in self.classes:
            new_instance = eval(f"{args[0]}()")
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")
    
    def do_show(self, args):
        """prints string representation of instance

        Args:
            args (_string_): 2 strings name and id separated with space
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args[0] in self.classes:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            instance_id = "{}.{}".format(args[0], args[1])
            try:
                print(instances[instance_id])
            except:
                print("** no instance found **")

    def do_destroy(self, args):
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args[0] in self.classes:
            print("** instance id missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            instances = storage.all()
            instance_id = "{}.{}".format(args[0], args[1])
            try:
                del(instances[instance_id])
                storage.save()
            except:
                print("** no instance found **")
        
    def do_all(self, args):
        """prints a string representation of all instances

        Args:
            args (_str_): _optional. name of class_
        """
        objects = storage.all()
        instances = []
        if not args:
            for name in objects:
                instances.append(objects[name])
            print(instances)
            return
        tokens = args.split(" ")
        if tokens[0] in self.classes:
            for name in objects:
                if name[0:len(tokens[0])] == tokens[0]:
                    instances.append(objects[name])
            print(instances)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """update instances

        Args:
            args (_str_): _4 strings class, id, attr, value_
        """
        tokens = args.split(" ")
        objects = storage.all()
        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return
        elif len(tokens) == 2:
            print("** attribute name missing **")
            return
        elif len(tokens) == 3:
            print("** value missing **")
            return
        else:
            name = tokens[0] + "." + tokens[1]
            if name not in objects:
                print("** no instance found **")
            else:
                obj = objects[name]
                not_to_change = ["id", "created_at", "updated_at"]
                if tokens[2] not in not_to_change:
                    obj[tokens[2]] = tokens[3]
                    obj['updated_at'] = datetime.datetime.today().isoformat()
                    storage.save()
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()
   