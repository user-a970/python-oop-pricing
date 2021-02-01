# Getting Started
## What You'll Need
Since this is a _Python_ Design Pattern project, 
you'll need Python, 
Python 3 specifically. 
Open the command prompt _Search > cmd_ and enter

```bash
py -0p
```

to list all currently installed versions of Python. 
If you don't already have Python, 
you can download it from [here](https://www.python.org/).

Microsoft's [Visual Studio Code Editor](https://code.visualstudio.com/) is recommended with the [Python Extension](https://code.visualstudio.com/docs/languages/python) installed. 
The command prompt can be directly accessed in VSCode, 
either through the menu item _Terminal > New Terminal_, 
or by [keyboard shortcut](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf). 
Make sure the terminal is set to `cmd` and not Powershell.

![cmd](../Images/00%20Getting%20Started/cmd.png)

From the command line install [Pylint](https://pylint.org/) either globally with 

```bash
pip install pylint
```

or in a [virtual environment](https://docs.python.org/3/tutorial/venv.html) with

```bash
pipenv install pylint
```

Once pylint is installed, 
set the workspace linter to pylint by opening VSCode's pallette with
`Ctrl + Shift + p` and searching for _Python: Select Linter_. 
This is a feature enabled with the [Python Extension](https://code.visualstudio.com/docs/languages/python). 
Choose pylint from the list of available linters.

![Select Pylint](../Images/00%20Getting%20Started/select_pylint.png)

Next, 
open the workspace settings configuration, 
again through VSCode's pallette, 
and search for _Preferences: Open Settings (JSON)_. 
Make sure `python.linting.pylintEnabled` and `python.linting.enabled` are set to `true`.

```json
{
    "python.linting.pylintEnabled": true,
    "python.linting.enabled": true
}
```

## Using Pylint
Pylint is a Python static code analysis tool which looks for programming errors, 
helps enforce a coding standard, 
sniffs out code smells, 
and offers simple refactoring suggestions.
We will use Pylint to enforce _contracts_ between code users. 

We'll use the popular [2D Point class example](./2d_point_class_example.py) to check that pylint is working as it should be. 

The 2D Point class is defined as

```python
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
```

It says - supply 2 points, `x`, and `y`, 
and "draw" those points in space. 

We can check if Pylint is working by creating a programming error. 
Open the file in VSCode and change line 23 from

```python
point = Point(1, 2)
```

to 

```python
point = Point(1)
```

and save the file. 
If Pylint is correctly installed, 
and enabled in the configuration file, 
a red line should appear under the `Point` class call. 

![Pylint doing its job](../Images/00%20Getting%20Started/point_error.png)

Hovering the mouse over the red line will generate an information box attempting to debug the programming error detected by Pylint in the creation of the class instance. 
Indeed, 
creating a 2-dimensional Point class object requires 2 inputs, 
yet we have only provided the class with one.