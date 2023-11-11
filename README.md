# Welcome to the AirBnB clone project!

![Hbnb Logo](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T151340Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=1244bc9e330c4e72996dcd5b3ef8cb1db615292808ab2f6175d7312039994652)

## Project Description

The AirBnB clone project is a full web application: It is a clone of the [AirBnB website](https://www.airbnb.com/). This project implements some of the features of the website.

The AirBnB clone project is composed by:
+   A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for  development and debugging)
+   A website (the front-end) that shows the final product to everybody: static and dynamic
+   A database or files that store data (data = objects)
+   An API that provides a communication interface between the front-end and your data (retrieve, + create, delete, update them)


## What’s a command interpreter - The Console?

![A picture showing the interaction of a console with a storage engine](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231111%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231111T151340Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6f8a49e799aedfe48caeffb9f93cd447784139cdf517d7637e7f02fe961a7efd)

The command interpreter is a shell-like program specifically tailored to manage AirBnB clone data. It interacts directly with the storage engine. It is called a **console**. It can be used to perform the following actions:

-   Create a new object (ex: a new User or a new Place)
-   Retrieve an object from a file, a database etc…
-   Do operations on objects (count, compute stats, etc…)
-   Update attributes of an object
-   Destroy an object

### How to start it?
To start the console, kindly follow the code instructions below:

```

$ ./console.py
(hbnb)
```

### How to use it?
To use the console, you have to start the console first. Then, type the help command to see list of available commands. `Crtl + D` for windows OS or `Command + D` for Mac OS will exit the console. Likewise, the `quit` command. See code instruction or examples below:

```

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit create show all update destroy

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

The console also works in the non-interactive mode as follows:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
