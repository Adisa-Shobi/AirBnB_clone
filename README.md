# AIRBNB Clone Project (HBNB)
![Airbnb logo image](./resources/logo.png)
## About
This project is a clone of Airbnb, a platform used to connect people who want to rent homes. It was built as part of a learning effort at Holberton School.
## Console
The console can be used to manipulate and manage app data as demonstrated below:
#### Interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
#### Non-Interactive mode:
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
### Console commands
| Command | Description                                                                    |
| ------- | ------------------------------------------------------------------------------ |
| quit    | Exits console when entered before `EOF` character                              |
| help    | Shows description of all working console commands                              |
| create  | Creates a new instance of the class whose name it precedes                     |
| show    | Prints a string representation of an instance based on the class name and `id` |
| destroy | Deletes an instance based on the class name and `id`                           |
| all     | Prints all string representation of all instances based or not on the classname|
| update  | Updates an instance based on the class name and id by adding/updating attribute|
## Project Structure
![Data diagram](./resources/structure.png)
