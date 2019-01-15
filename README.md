# UBC Subbots Object Detection Training Repository
Main Tensorflow Training Repository for Subbots

## Table of Contents
- [Setup](#setup)
  - [Install](#install)
- [Coding Conventions](#code-conventions)
- [Testing](#testing)


## Setup 

### Install

Clone repository with 'git clone --recursive https://github.com/ubc-subbots/Object-Detection-Training'

To install the dependencies of the repository, run the ./setup_environment.sh script. Anytime you want to use the tensorflow api, run 'source subbots_python/bin/activate'.

## Code Conventions

Source files should adhere to the following documentation standards. There is a sample file in scripts/sample_package/sample_py.py for reference.

````


#Created By: Someone
#Created On: December 1st, 2000

"""
This example module shows various types of documentation available for use
with pydoc.  To generate HTML documentation for this module issue the
command:

    pydoc -w foo

"""

class Foo(object):
    """
    Foo encapsulates a name and an age.
    """
    def __init__(self, name, age):
        """
        Construct a new 'Foo' object.

        :param name: The name of foo
        :param age: The ageof foo
        :return: returns nothing
        """
        self.name = name
        self.age = age

def bar(baz):
    """
    Prints baz to the display.
    """
    print(baz)

if __name__ == '__main__':
    f = Foo('John Doe', 42)
    bar("hello world")
    
````

## Testing

All files should have unit tests written using the pytest convention (https://docs.pytest.org/en/latest/#). A proper test function begins with test_* and is placed in a file in the test folder.

````
import pytest

class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')
 
 ````




