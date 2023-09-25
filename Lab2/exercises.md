# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*Edit your responses here*
In many standard libraries, such as the c++ standard template library or Python's built-in list method, pop operations can not only remove elements, but also return them. This has become a common practice. So, in this case, using pop is not necessarily a "bad" example. Still, for those unfamiliar with this convention, their expectations can be mismatched.


2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*Edit your response here*
They are both collection data types, but they serve different purposes and are based on different underlying data structures. While dictionaries and lists both store collections of data, dictionaries are centered around unique keys that map to values, while lists are about maintaining an ordered collection of items. 

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Edit your response here*
The list allows random access, which means that you can access any element directly through its index within constant time O(1). In the context of a list implemented as a dynamic array，you can use its index to access any element without having to traverse the others.

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*Edit your response here*
While generic container data structures offer significant benefits in terms of flexibility, reusability, and type safety, they also present challenges related to complexity, potential performance overhead, and availability. The decision to use them often depends on the specific needs of the project and the development team's familiarity with generic programming.
## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*Edit your responses here*
Use CRUD: **get(url, params=None, kwargs): to issue a get request. The name "get" accurately refers to the HTTP get method.



**post(url, data=None, json=None, kwargs): Used for post requests. The name "post" matches the HTTP post method.



**put(url, data=None, kwargs): Matches the put method of HTTP.



**delete(url, kwargs): The delete method matches HTTP.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*Edit your responses here*
Functions with many arguments can get messy and can be error-prone, especially if many of these arguments are of similar types or their order is difficult to remember.

Regarding request libraries, the main functions provided by the API typically accept a small number of commonly used parameters directly and then rely on **kwargs to capture any additional parameters. Using **kwargs provides flexibility without overloading function signatures with a large number of arguments.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*Edit your responses here*
**kwargs is a syntax in Python that allows a variable number of keyword arguments to be passed to functions. While **kwargs offer flexibility, they should be used with caution. As with many programming constructs, balance is key. In situations where the benefits outweigh the potential clarity or security tradeoffs, kwargs is a great tool. Otherwise, it is better to be more explicit in the function signature.
4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


*Edit your responses here*
<<<<<<< HEAD
The default value is None: indicates an optional feature. Prevents problems with variable defaults. - Can the default value not be None? Yes, any valid Python value can be the default value. - Advantage of default: simplified call in common cases. Ensure backward compatibility. Provide hints about expectations. Reduce caller complexity. Provide more secure default behavior.
=======
The default value is None: indicates an optional feature. Prevents problems with variable defaults. - Can the default value not be None? Yes, any valid Python value can be the default value. - Advantage of default: simplified call in common cases. Ensure backward compatibility. Provide hints about expectations. Reduce caller complexity. Provide more secure default behavior.
>>>>>>> c18438daf4a04b5b385bba5e8b3117d1947341a8
