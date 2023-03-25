**Auto-generated** using [documatic](https://github.com/aspizu/documatic)


# test1


 - [MyClass](#MyClass)

     - [MyClass.MyInnerClass](#MyClassMyInnerClass)
    


## `my_function`


```py

def my_function(arg1, arg2):
    ...
```

This is the docstring for my_function. It describes what this function does.


Example usage:
```py
  >>> my_function('hello', 3.14)
  ... 'hello 3.14'
```


### Arguments:

 - `arg1`: A string that is used in the calculation.

 - `arg2`: A number that is used in the calculation.



### Returns:

  A string that combines arg1 and arg2.

# `MyClass`


```py

class MyClass:
    ...
```

This is the short summary for MyClass.


This is the long summary for MyClass. It should describe what this class does in detail.

Example usage:
```py
  >>> my_object = MyClass()
  >>> my_object.my_method()
```


### Attributes:

 - `my_attribute`: A counter that keeps track of how many times my_method() has been called.



# `MyClass.MyInnerClass`


```py

class MyInnerClass:
    ...
```

This is the long summary for MyInnerClass.


It should describe what this class does in detail.

Example usage:
```py
  >>> my_object = MyClass()
  >>> my_inner_object = my_object.MyInnerClass()
```


### Attributes:

 - `inner_attribute`: A string that is used in my_method().



## `__init__`


```py

def __init__(self):
    ...
```

This is the constructor for MyInnerClass. It initializes a few attributes.


Example usage:
```py
  >>> my_object = MyClass()
  >>> my_inner_object = my_object.MyInnerClass()
  >>> my_inner_object.inner_attribute
  ... 'hello'
```


## `my_method`


```py

def my_method(self, arg1):
    ...
```

This is the docstring for MyInnerClass.my_method.


It describes what this method does.

Example usage:
```py
  >>> my_object = MyClass()
  >>> my_inner_object = my_object.MyInnerClass()
  >>> my_inner_object.my_method(3)
  ... 9
```


### Arguments:

 - `arg1`: A number that is used in the calculation.



### Returns:

  The result of the calculation.

### Raises:

 - `ZeroDivisionError`: Never.



## `__init__`


```py

def __init__(self):
    ...
```

This is the constructor for MyClass. It initializes a few attributes.


Example usage:
```py
  >>> my_object = MyClass()
  >>> my_object.my_attribute
  ... 0
```


## `my_method`


```py

def my_method(self):
    ...
```

This is the docstring for my_method.


It describes what this method does.

Example usage:
```py
  >>> my_object = MyClass()
  >>> my_object.my_method()
  ... 1
```


### Returns:

  The current value of my_attribute.

