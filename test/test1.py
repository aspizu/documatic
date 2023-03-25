"""This is the module summary.

It should briefly describe what this module does.

Example usage:
  >>> import my_module
  >>> my_object = my_module.MyClass()
"""


class MyClass:
    """This is the short summary for MyClass.

    This is the long summary for MyClass. It should describe what this class does in detail.

    Attributes:
      my_attribute: A counter that keeps track of how many times my_method() has been called.

    Example usage:
      >>> my_object = MyClass()
      >>> my_object.my_method()
    """

    def __init__(self):
        """This is the constructor for MyClass. It initializes a few attributes.

        Example usage:
          >>> my_object = MyClass()
          >>> my_object.my_attribute
          ... 0
        """
        self.my_attribute = 0

    def my_method(self):
        """This is the docstring for my_method.

        It describes what this method does.

        Returns:
          The current value of my_attribute.

        Example usage:
          >>> my_object = MyClass()
          >>> my_object.my_method()
          ... 1
        """
        self.my_attribute += 1
        return self.my_attribute

    class MyInnerClass:
        """This is the long summary for MyInnerClass.

        It should describe what this class does in detail.

        Example usage:
          >>> my_object = MyClass()
          >>> my_inner_object = my_object.MyInnerClass()
        """

        def __init__(self):
            """This is the constructor for MyInnerClass. It initializes a few attributes.

            Example usage:
              >>> my_object = MyClass()
              >>> my_inner_object = my_object.MyInnerClass()
              >>> my_inner_object.inner_attribute
              ... 'hello'
            """
            self.inner_attribute = "hello"
            """A string that is used in my_method()."""

        def my_method(self, arg1):
            """This is the docstring for MyInnerClass.my_method.

            It describes what this method does.

            Args:
              arg1: A number that is used in the calculation.

            Returns:
              The result of the calculation.

            Raises:
              ZeroDivisionError: Never.

            Example usage:
              >>> my_object = MyClass()
              >>> my_inner_object = my_object.MyInnerClass()
              >>> my_inner_object.my_method(3)
              ... 9
            """
            return arg1 * arg1


def my_function(arg1, arg2):
    """This is the docstring for my_function. It describes what this function does.

    Args:
      arg1: A string that is used in the calculation.
      arg2: A number that is used in the calculation.

    Returns:
      A string that combines arg1 and arg2.

    Example usage:
      >>> my_function('hello', 3.14)
      ... 'hello 3.14'
    """
    return arg1 + " " + str(arg2)
