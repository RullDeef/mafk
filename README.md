# Mafk

---

## Destination

Mafk - is a tool for fast and the easiest way to build/test your C projects.

However the cost of simplisity is a straight rules that you must follow:

1. All your *.c (and/or *.h) files must be in any of these directories: src, inc, include
2. You dont need to create makefiles over and over again
3. `more coming soon...`

---

## Usage

Basic steps in order to start brand new simple and small project:

1. `mafk new my_project_name` // creates directory *my_project_name* along with basic files in it. 
2. `cd ./my_project_name/src && vim main.c` // write some code!
3. `mafk build` // build from standard template!
4. `cd ../build && ./my_project_name` // actually run it

Syntax for .mfk files:

```
# comment
// another comment
/* yet, another comment */

USE gcc // or CC gcc, clang

STD c99
TARGET my_app_name
```
