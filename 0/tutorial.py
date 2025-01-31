# pylint: disable=invalid-name # shut up ide
"""
python is a programming language

and so it is very much like a programming language

this file is going to show you how you will use a programming language
"""

# pylint: disable=pointless-string-statement
"""
python syntax is very uhh:
it uses indentation instead of brackets {}, and no ;

indentation:

```python
broski = "writing python in md in python"

if len(broski) > 0:
    print("inside a block")

```

normally you would see a lot of semicolons and brackets
```rust
let broski = "writing rust in here is crazy";

if broski.len() > 0 {
    println!("inside a block");
}
```

but in python you just need to press enter.

to get in a block you press four spaces more,
and out of block you press four spaces less
"""

"""
how to make a variable:
name your variable name, place a single equal sign,
then name your value
"""  # remember a multiline string is not a comment

my_var = 4

# 4 is certainly a value of a type

# pylint: disable=unidiomatic-typecheck
assert type(my_var) == int  # yes use isinstance i know
# oh yes two equal signs make a comparison between left and right
# and return a boolean (true or false)
"""
assert will fail and crash if what after it is false:
that means my var is an integer
"""

"you can change the content of the variable to whatever"
# idk if it is a shadow (making past my_var out of use)
# dont have to care tho
my_var = 3.14
# float has a dot in there. just put a dot in there


assert type(my_var) == float  # pylint already disabled :)
# still true; this file do not crash you can trust the assertions

"there is a lot of types: float, int, bool also, and string:"

my_var = "hello python"
# its str now

"""
kinda lax isnt it. you can bind my_var to everything at this point.

but not quite so lax: you can not just mention something you have not made
"""

try:  # this is a try block: errors/exceptions inside get captured...

    # this is obviously an error
    my_undeclared_var  # pyright: ignore reportUndefinedVariable # extension hell
except NameError:  # ...in an except block, over here
    print("my undeclared var is obviously undeclared")
    # this will run will print to console
# exceptions not captured will bubble

"""
certainly not so lax

that is some values, we also have containers, which contain values
"""

my_list = [5, "list", "items", ("with", "different"), type]
# type() is a function: you could put literally everything in a list it does not care

"""
values, including lists. yes, thats powering your 2d matrix.

we have tuples, and set, and also dict. these are the python data types:
"""

my_tuple = ("these can not be changed", 2, 3.0)
# tuple is just for grouping items to send somewhere together
# if you want to change/add things you should be using any other types of container

my_set = {
    "unique",
    "items",
}

my_dict = {
    "key": "value",
    # key must has __hash__ (for O(1) lookup)
    # this is the existing my_var: see below
    my_var: 12,
    3 + 5: 8,
}

"""
keys in dict and items in set have to be unique:
school = {
    "name": "mog school",
    "class": "a",
    "class": "b" # Not allowed
}

notice for dictionaries it goes like this:

    key : value ,

where key and value are both expressions.
"""
# but what are expressions?
# they are the thing that can stay on right side of an assignment
# variable = expression
# lets consider this expression: my_var + " beginners"
# it returns a value: "hello python beginners"
# if whatever you do: putting down an existing variable, adding two variables,
# calling a function, getting attributes...
# returns values, then it must be an expression.
# check wikipedia Python for more examples

"""how do you aceess these containers?

we have a sugar syntax: container[index]

where index can be a value, in case of list and tuple:
"""

assert my_list[2] == "items"  # third item staring from 1,
# so 2nd item starting from 0

"index can be negative: different from C"

assert my_tuple[-2] == 2

"""for sets: good luck

for dictionary you can use a value that is equal to
an existing key:
"""

assert my_dict["hello python"] == 12

"""
for lists and tuples you would see a thing called a slice notation:

start:end[:step]
"""

assert (my_list[2:5]) == ["items", ("with", "different"), type]

"""
start is inclusive, end is exclusive

step makes it only index every (step) items from (start) and stop right before reaching (end)

slice notation makes life easy
"""

assert (my_list[:5:2]) == [5, "items", type]

"""use blank for start to denote first item,
blank for end to denote past last item,
and nothing for step means step by 1

you may need this to select a range of items. its confusing but handy
"""


one_to_20 = list(range(1, 21))  # [1, ... , 20]
weird_selection = [19, 15, 11, 7]

assert one_to_20[-2:3:-4] == weird_selection
# imagine instead of -2 its len(list) - 2. its handy for someone coming from C

"""
uh huh slice also takes negative number, and out of bounds number:
one_to_20[30] would be index out of range, but
one_to_20[20:30] simply returns empty array.
"""

"""we are here for math. calculations. functions.

well:

to define a function you go def my_function(my_param):
then indent four spaces to get in the function block.
"""


def hello_world():
    "print 'hello world' to console"
    print("hello world")


# as math person, there would be a lot of times where there are symbols and shit
# naming it would be clear i would understand your code.
# take some time. name your variable mu or theta or dvdt

"""
see that. indent. dedent. (outdent?)

and you can define another function in in a function, unlike in c i would have to use closure [](){}

for parameters you put in the () at the def over there. (a, b, c)
and then in the fn body you would interact with them

your function can return some values:
"""


# hey
def quadratic_builder(a, b, c):
    """this function returns a function with 1 parameter

    calling the returned function with a number argument x would calculate

    a * x ** 2 + b * x + c
    """

    def quadratic(x):
        second_order = a * x**2
        first_order = b * x
        zeroth_order = c
        # oh this looks redundant.
        # but trust me when i say youll write code like this
        return second_order + first_order + zeroth_order

    return quadratic


"""
your function is already usable anywhere in the code

to call any function you would do my_function()

if the function needs params you supply it with arguments:
"""

x_minus_one_squared = quadratic_builder(1, -2, 1)

assert x_minus_one_squared(3) == (3 - 1) ** 2 == 4

"your function can have default params"


def hello_to(name=None):
    """if called with zero arguments, this function prints hello world

    if supplied a name argument it will hello the name instead
    """
    if name is None:
        print("hello world!")
    else:
        print(f"hello {name}!")


"""
in python you can pass in anything as a parameter.

which is particularly scary, because i dont want to call 
x_minus_one_squared("bad string") do i

welcome to problem number one of python.

Solution: type hints.
"""
# type hints are hints. which means you can still pass args with invalid types. coders be careful.


def bungee_jumper(t: float, mass: float, drag_coeff: float) -> float:
    """
    using this funny ass function found in the slides:

    v(t) = sqrt(g*m/cd) * tanh(sqrt(g*cd/m) * t)
    """
    # hey pylint this one im not sure
    from math import sqrt, tanh  # pylint: disable=import-outside-toplevel

    # manual check
    if t < 0 or drag_coeff < 0 or mass <= 0:
        raise ValueError("well uh its not possible is it")

    # scipy where
    g = 9.80665

    if drag_coeff == 0 or t == 0:
        return t * g  # please

    term_vel = sqrt(g * mass / drag_coeff)
    what_is_this = sqrt(g * drag_coeff / mass)

    return term_vel * tanh(what_is_this * t)


"""
holy function

with type hints over there you know what type of args you are supposed to put in and what would be returned, which is very handy.

you can even put in default values!
i love default values. there is some problems with certain types but i know to avoid it.

that example is crazy
"""

"""
truly math focused. Function first.

we have conditionals and loops, which is a lot easier in code than in math:

if, just like above.
"""


obvious = 1 + 1 == 2  # this operation returns true

if obvious:
    print("this will print")

obviously_wrong = x_minus_one_squared(5) == 25

if obviously_wrong:
    print("you will never appear")
else:
    print("this will also print")


"chaining if statements is easy with elif:"

my_five = 5

if 2 + 2 == my_five:
    print("2 + 2 = 5")
elif 2 + 3 == my_five:
    print("2 + 3 = 5")
elif 3 + 3 == my_five:
    print("3 + 3 = 5")
else:
    print("D. None of the above")


"""
for.

it is for element in collection. Remember: for element in collection.

C for is ass: for (;;) which is ass.

for of C is: 
    for ([this statement runs once before the loop];
        [this expressions is calculated if it returns 0 the loop stops];
        [this statement runs after each loop])

used a lot for running through an array:
for (int i = 0; i < arr_size; i++);

some wicked shit. notice that it is < and not <=. WHY do i have to care about that?
NO you dont. 

Python for is for element in iterable (which can be a collection, like an array)

it is much easier to work with and much much less prone to bugs.

yeah no segfaults for you here
"""
another_number = 1

for number in one_to_20:
    assert number == another_number
    another_number += 1
    # this would add 1 to itself

# quick notice: this number variable can not be accessed outside the for loop.

# actually it will be the last element actually i dont know
# coming from literally any other language:
# a variable made for the loop should only stay in the loop
# why is python like this? is this a bug?

"""
while.

while condition is True:
    # do something with the condition.        

while just runs until the condition (after while before colon) is falsy.
"""

while another_number:
    another_number -= 1

assert another_number == 0

"""
sometimes you want to break out early:

use break

sometimes you want to skip some of the loops:

use continue
"""

while True:
    # if there is no break in this loop it would be BAD
    another_number += 1
    if another_number == 10:
        # maybe the check is more sophisticated you cant put it in the while condition
        # idfk your code your decision
        break

    if another_number in [4, 7]:
        continue

    print(another_number, "is not a bad number")  # this will skip 4 and 7

# wtf

"""
match case

like switch case but it is match case and it doesnt have fallthroughs
"""


"""
errors. you get those when you use a thing and it doesnt run how you want, so it crashes and print:

Traceback (most recent call last):
  File "nmu/python/0/tutorial.py", line 442, in <module>
    int("string")
ValueError: invalid literal for int() with base 10: 'string'

thats bad. someone raised an error on us.

you can catch it with the try except block, and you can also raise your own error!

previous examples have those. there are some common errors like TypeError or ValueError or IndexError etc. 
how use? python docs got u. visit python docs
"""

"""
custom model

currently you are having a problem. you have a model of stuff, with this and that. 
you have some things you want to get from the model.

How would this work?
"""

from collections import namedtuple
from numbers import Number
from typing import Self

# a habit that you should take is that you should never blanket import.
# non of these import * in python, use ::* in rust, using namespace in c++, etc.
# only import what you need. the IDE will help you.


class BungeeJumper:
    """
    this is also the slide but i use the numerical

    v(t+dt) = v(t) + (g + cd/m * v(t)**2) * dt
    """

    BungeeTuple = namedtuple("BungeeTuple", ["t", "dt", "vt"], rename=True)

    def __init__(self, mass, drag_coeff):
        if not isinstance(mass, Number) or not isinstance(drag_coeff, Number):
            raise ValueError("did not supply numbers")
        if mass <= 0 or drag_coeff <= 0:
            raise ValueError("values smaller than 0")

        # doing this basically forbids all outside access to __(something).
        # two underscores. i repeat: two underscores.
        self.__mass = float(mass)
        self.__drag_coeff = float(drag_coeff)
        self.__time = 0.0
        self.__delta_time = 1.0
        self.__vt = 0.0
        self.__table: list[BungeeJumper.BungeeTuple] = [self.current_bungee_tuple()]

    @property
    def mass(self):
        "mass of the bungee person"
        return self.__mass

    @property
    def cd(self):
        "air drag of bungee person"
        return self.__drag_coeff

    # getter overrides property fn for getting values.
    # you wont be using @my_attr.getter ever

    @property
    def t(self):
        """current time

        we will not set time, change it through delta + special reset fn,"""
        return self.__time

    @property
    def dt(self):
        "current delta, settable"
        return self.__delta_time

    @dt.setter
    def dt(self, new_delta):
        "setting delta time"
        if new_delta <= 0:
            raise ValueError("delta <= 0 which isnt what we like")
        self.__delta_time = new_delta

    @property
    def vt(self):
        "current vt for viewing only"
        return self.__vt

    # we do not like boilerplate code
    def current_dvdt(self, current_vt):
        """
        get deriv supplied current vt
        """
        g = 9.80665
        cd_m = self.cd / self.mass
        return g - cd_m * current_vt**2

    def vt_step(self, delta_t):
        "what would be next given current systems state"
        current_vt = self.vt
        current_t = self.t
        current_dvdt = self.current_dvdt(current_vt)
        new_t = current_t + delta_t
        new_vt = current_vt + current_dvdt * delta_t
        return new_t, new_vt

    @staticmethod
    def bungee_tuple(t, dt, vt):
        "static method for the format of BungeeJumper.BungeeTuple"
        return BungeeJumper.BungeeTuple(t=t, dt=dt, vt=vt)

    def current_bungee_tuple(self):
        "class method for current BungeeJumper.BungeeTuple"
        return BungeeJumper.bungee_tuple(self.t, self.dt, self.vt)

    def vt_next(self):
        "step"
        self.__time, self.__vt = self.vt_step(self.dt)
        c = self.current_bungee_tuple()
        self.__table.append(c)
        return c

    def reset(self):
        old = self.__table
        self.__time = 0.0
        self.__delta_time = 1.0
        self.__vt = 0.0
        self.__table = [self.current_bungee_tuple()]
        return old

    def bungee_info(self):
        return {
            "t": self.t,
            "dt": self.dt,
            "vt": self.vt,
            "m": self.mass,
            "cd": self.cd,
            "table": [i._asdict() for i in self.__table],
        }

    # pylint flagged this for design choice, and i agree.
    def bungee_import(self, t=None, dt=None, vt=None, m=None, cd=None, table=None):
        """overrides, also format from bungee_info only"""
        if t is not None:
            self.__time = t
        if dt is not None:
            self.__delta_time = dt
        if vt is not None:
            self.__vt = vt
        if m is not None:
            self.__mass = m
        if cd is not None:
            self.__drag_coeff = cd
        if table is not None:
            self.__table = [self.bungee_tuple(**i) for i in table]

    @staticmethod
    def from_bungee_table(table: list[BungeeTuple], mass, drag_coeff) -> Self:
        last = table[-1]
        t, dt, vt = last
        new = BungeeJumper(mass, drag_coeff)
        new.bungee_import(t=t, dt=dt, vt=vt, m=mass, cd=drag_coeff, table=table)
        return new


bungee = BungeeJumper(68.1, 0.25)
bungee.dt = 2
print(bungee.vt_next())


# wow it so works
# trailing off

"""so much over here. a lot of it is boilerplate,
only a few: namely vt_step and current_dvdt is doing all the math.

yes. thats code for you. a lot of structure for idk 5 lines of actual calculation or something idfk
"""

"""
Class. The heart of python. literally everything is a class. 

you are either working with a function, which is a class,
a data type, which is a class,
or like an external module / package, which is (oh no) also a class.


class in python is more lenient than java:

first up: everything need not be a class:
in java you have to declare the main class and the main function.
in python they see statement they execute statement. no need for class.

while java you can only inherit from only one base class, in python
you can have multiple base classes, classes that double as interfaces, etc.

you can also have directly editable attributes.
No getter / setter functions. if you want you could make them, like i do, but rn you dont

you also have no private attributes. i can only hope you wont touch my 
bungee._BungeeJumper__time and mess it up.

Class is yk classic OOP: you have class, you have instances of class.
class BungeeJumper is a class, bungee is an instance.
int is a class, and 1 is an instance.


everywhere else they call a function function, but in a class they call them Methods.

methods have this kinda thing they call dot notation.
basically instance.method is just another function. but somethings going on:

instance instead of doing nothing will be passed into methods as first argument.
yes, not javas `this`. `this` is a set name.
python `self` i could change it to whatever. instance will be passed to it.

That is a method.
a staticmethod has no such rules.
"""

# do you know you can declare a class without even touching the word class at all? its the power of type().
# however dont do this oh please


def lda_set_example_arg(inst, arg):
    inst.lda_example_instance_arg = arg


" __init__ is a magic function that will run when you make a class instance"

LdaExampleClass = type(
    "LdaExampleClass",
    (object,),
    {
        "__init__": lda_set_example_arg,
        "lda_example_class_arg": 1,
        "quadratic_builder": quadratic_builder,
        "hello_world": hello_world,
        "hello_to": hello_to,
    },
)

LdaExampleClass.hello_to("lda")  # prints hello lda!


def lda_print_example_arg(inst):
    print("instance:", inst.lda_example_instance_arg)
    print("class:", inst.lda_example_class_arg)

# @classmethod # class methods passes class as opposed of instance for first arg # i just knew this!
# def cls_print_example_arg(cls):
#     print("class:", cls.lda_example_class_arg)
#     print("instance:", cls.lda_example_instance_arg) # uh oh

# objects can freely add properties
LdaExampleClass.lda_print_example_arg = lda_print_example_arg
# LdaExampleClass.cls_print_example_arg = cls_print_example_arg # see note below

lda1 = LdaExampleClass(3)  # this must fit the args of self.__init__()
lda1.lda_print_example_arg()  # pylint: disable=no-member # ide freak out
# this will print instance which we just passed as 3,
# and class which is from the above which is 1.
# Nothing was changed: i dont assign anything to anything in the functions
# except for lda_set_example_arg
# lda1.cls_print_example_arg() # crashes as cls LdaExampleClass dont have lda_example_instance_arg instance variable

# dont do this, however, as ide will freak out.


"""so uh that was a bad example huh.

turning back to list. Now you know list is a kinda a class.
and class has methods. List also has some methods.
"""

copied_1_20 = one_to_20.copy()  # this shallow copies

copied_1_20.append(21)

assert copied_1_20 != one_to_20
assert copied_1_20[-2:] == [20, 21]

# if you have intellicode you can do ctrl + space to get that hints going.

"""
ah yes intellicode. 
You can view methods easily with intellisense if using vscode, 
and you can also docs.python.org for more
"""

# here is where you should be downloading jupyter to get the Tutorial2 Going.
# check its website. make sure you have the python, it is in PATH, and the pip exists. Or you can use poetry or miniconda. Or pipx. idfk do research.
