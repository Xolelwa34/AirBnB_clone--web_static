#!/usr/bin/python3
"""Defines HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): Command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """None."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when the input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_num,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit program."""
        print("")
        return True

    def do_create(self, arg):
        """Method used to create a new class instance and print its id."""
    
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Method to display the string representation of a class instance of a given id."""
        argl = parse(arg)
        objctdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objctdict:
            print("** no instance found **")
        else:
            print(objctdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy or delete a class instance of a given id."""
        argl = parse(arg)
        objctdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objctdict.keys():
            print("** no instance found **")
        else:
            del objctdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Method to Display string representations of all instances of a given class."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objctl = []
            for objct in storage.all().values():
                if len(argl) > 0 and argl[0] == objct.__class__.__name__:
                    objctl.append(objct.__str__())
                elif len(argl) == 0:
                    objctl.append(objct.__str__())
            print(objctl)

    def do_num(self, arg):
        """Method num to retrieve the number of instances of a given class."""
        argl = parse(arg)
        num = 0
        for objct in storage.all().values():
            if argl[0] == objct.__class__.__name__:
                num += 1
        print(num)

    def do_update(self, arg):
        """Usage method to update; class; id; attributes."""
        argl = parse(arg)
        objctdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objctdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            objct = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in objct.__class__.__dict__.keys():
                val = type(objct.__class__.__dict__[argl[2]])
                objct.__dict__[argl[2]] = val(argl[3])
            else:
                objct.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objctdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in objct.__class__.__dict__.keys() and
                        type(objct.__class__.__dict__[k]) in {str, int, float}):
                    val = type(objct.__class__.__dict__[k])
                    objct.__dict__[k] = val(v)
                else:
                    objct.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
