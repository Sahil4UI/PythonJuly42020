Python 3.8.3 (v3.8.3:6f8c8320e9, May 13 2020, 16:29:34) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 1
>>> b = 2
>>> a+b
3
>>> a = 5.59
>>> b = 9.8
>>> a+b
15.39
>>> a-b
-4.210000000000001
>>> a*b
54.782000000000004
>>> a/b
0.5704081632653061
>>> 1.2**2
1.44
>>> 1.90990//12
0.0
>>> #Comples NUmber
>>> #Complex Number
>>> #a = real+ imaginary
>>> a = 5+3z
SyntaxError: invalid syntax
>>> a = 5+3j
>>> a.real
5.0
>>> a.imag
3.0
>>> b = 1+2j
>>> b
(1+2j)
>>> b.real
1.0
>>> b.imag
2.0
>>> a+b
(6+5j)
>>> b_b
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    b_b
NameError: name 'b_b' is not defined
>>> type(a+b)
<class 'complex'>
>>> a-b
(4+1j)
>>> a*b
(-1+13j)
>>> a
(5+3j)
>>> b
(1+2j)
>>> a/b
(2.2-1.4j)
>>> 11/5
2.2
>>> 7/5
1.4
>>> 3+2j/4+5j
(3+5.5j)
>>> (3+2j)/(4+5j)
(0.5365853658536587-0.17073170731707318j)
>>> import cmath
>>> help(cmath)
Help on module cmath:

NAME
    cmath

MODULE REFERENCE
    https://docs.python.org/3.8/library/cmath
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to mathematical functions for complex
    numbers.

FUNCTIONS
    acos(z, /)
        Return the arc cosine of z.
    
    acosh(z, /)
        Return the inverse hyperbolic cosine of z.
    
    asin(z, /)
        Return the arc sine of z.
    
    asinh(z, /)
        Return the inverse hyperbolic sine of z.
    
    atan(z, /)
        Return the arc tangent of z.
    
    atanh(z, /)
        Return the inverse hyperbolic tangent of z.
    
    cos(z, /)
        Return the cosine of z.
    
    cosh(z, /)
        Return the hyperbolic cosine of z.
    
    exp(z, /)
        Return the exponential value e**z.
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two complex numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them must be
        smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard. That is, NaN is
        not close to anything, even itself. inf and -inf are only close to themselves.
    
    isfinite(z, /)
        Return True if both the real and imaginary parts of z are finite, else False.
    
    isinf(z, /)
        Checks if the real or imaginary part of z is infinite.
    
    isnan(z, /)
        Checks if the real or imaginary part of z not a number (NaN).
    
    log(...)
        log(z[, base]) -> the logarithm of z to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of z.
    
    log10(z, /)
        Return the base-10 logarithm of z.
    
    phase(z, /)
        Return argument, also known as the phase angle, of a complex.
    
    polar(z, /)
        Convert a complex from rectangular coordinates to polar coordinates.
        
        r is the distance from 0 and phi the phase angle.
    
    rect(r, phi, /)
        Convert from polar coordinates to rectangular coordinates.
    
    sin(z, /)
        Return the sine of z.
    
    sinh(z, /)
        Return the hyperbolic sine of z.
    
    sqrt(z, /)
        Return the square root of z.
    
    tan(z, /)
        Return the tangent of z.
    
    tanh(z, /)
        Return the hyperbolic tangent of z.

DATA
    e = 2.718281828459045
    inf = inf
    infj = infj
    nan = nan
    nanj = nanj
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload/cmath.cpython-38-darwin.so


>>> cmath.sqrt(5+10j)
(2.8443224050289158+1.7578879212707146j)
>>> #STRING
>>> a ='123'
>>> type(a)
<class 'str'>
>>> a =123
>>> a="123"
>>> type(a)
<class 'str'>
>>> a="""123"""
>>> type(a)
<class 'str'>
>>> #INDEXING
>>> string = "PYTHON"
>>> string[0]
'P'
>>> string[4]
'O'
>>> string[-1]
'N'
>>> string[-3]
'H'
>>> #Slicing
>>> string
'PYTHON'
>>> string="Python Programming"
>>> string[0,5]
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    string[0,5]
TypeError: string indices must be integers
>>> string[0:5]
'Pytho'
>>> #end - n-1
>>> string[0:6]
'Python'
>>> string[:6]
'Python'
>>> string[:]
'Python Programming'
>>> string[::1]
'Python Programming'
>>> string[::2]
'Pto rgamn'
>>> string
'Python Programming'
>>> string[::-1]
'gnimmargorP nohtyP'
>>> 