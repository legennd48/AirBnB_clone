#!/usr/bin/python3
'''
Module: 6. Console 0.0.1
contains the entry point of the command interpreter:
'''
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    '''This is the entry point of the command line interpreter '''
    prompt = '(hbnb) '
    __classList = {"BaseModel", "User", "State", "City", "Amenity", "Place", "Review"}

    def do_EOF(self, line):
        '''Exits the program (interpreter)'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        ''' Does nothing when empty line is passed '''
        pass

    def do_create(self, className):
        '''Creates a new instance of BaseModel and prints its id'''

        if not className:
            print("** class name missing **")
        elif className in HBNBCommand.__classList:
            instance = globals()[className]()
            instance.save()
            print("{}".format(instance.id))
            storage.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        '''Prints string representation of an instance based class name nd id'''

        argsList = args.split()
        allObjects = storage.all()

        if len(argsList) == 0:
            print("** class name missing **")
        elif argsList[0] not in HBNBCommand.__classList:
            print("** class doesn't exist **")
        elif len(argsList) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argsList[0], argsList[1]) not in allObjects.keys():
            print("** no instance found **")
        else:
            print(allObjects["{}.{}".format(argsList[0], argsList[1])])

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id'''

        argsList = args.split()
        allObjects = storage.all()

        if len(argsList) == 0:
            print("** class name missing **")
        elif argsList[0] not in HBNBCommand.__classList:
            print("** class doesn't exist **")
        elif len(argsList) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argsList[0], argsList[1]) not in allObjects.keys():
            print("** no instance found **")
        else:
            del allObjects["{}.{}".format(argsList[0], argsList[1])]
            storage.save()

    def do_all(self, args):
        '''Prints all string representation of all
        instances based or not on the class name.
        '''
        argsList = args.split()
        if len(argsList) > 0 and argsList[0] not in HBNBCommand.__classList:
            print("** class doesn't exist **")
        else:
            allObjects = []
            for obj in storage.all().values():
                if len(argsList) > 0 and argsList[0] == obj.__class__.__name__:
                    allObjects.append(obj.__str__())
                elif len(argsList) == 0:
                    allObjects.append(obj.__str__())
            print(allObjects)

    def do_update(self, args):
        '''Updates an instance based on the class name and
        id by adding or updating attribute
        '''
        argList = args.split()
        allObjects = storage.all()

        if len(argList) == 0:
            print("** class name missing **")
            return False
        if argList[0] not in HBNBCommand.__classList:
            print("** class doesn't exist **")
            return False
        if len(argList) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argList[0], argList[1]) not in allObjects.keys():
            print("** no instance found **")
            return False
        if len(argList) == 2:
            print("** attribute name missing **")
            return False
        if len(argList) == 3:
            try:
                type(eval(argList[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argList) == 4:
            obj_instance = allObjects["{}.{}".format(argList[0], argList[1])]
            if argList[2] in obj_instance.__class__.__dict__.keys():
                val_type = type(obj_instance.__class__.__dict__[argList[2]])
                obj_instance.__dict__[argList[2]] = val_type(argList[3])
            else:
                obj_instance.__dict__[argList[2]] = argList[3]
        elif type(eval(argList[2])) == dict:
            obj_instance = allObjects["{}.{}".format(argList[0], argList[1])]
            for k, v in eval(argList[2]).items():
                if (k in obj_instance.__class__.__dict__.keys() and
                    type(obj_instance.__class__.__dict__[k])
                    in {str, int, float}):
                    val_type = type(obj_instance.__class__.__dict__[k])
                    obj_instance.__dict__[k] = val_type(v)
                else:
                    obj_instance.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
