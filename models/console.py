#!/usr/bin/python3
'''
Module: 6. Console 0.0.1
contains the entry point of the command interpreter:
'''
import cmd

class HBNBCommand(cmd.Cmd):
    '''This is the entry point of the command line interpreter '''
    prompt = '(hbnb)'

    def do_EOF(self, line):
        '''Exits the program (interpreter)'''
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        ''' Does nothing when empty line is passed '''
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
