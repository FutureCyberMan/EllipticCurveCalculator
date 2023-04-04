# EllipticCurveCalculator
## Introduction:
This tool is designed to sum points on an elliptic curve.
## Basic Tutorial:
You have a curve

$E: y^2 = x^3 + 3x + 2 \mod{7}$ 

that follows the form 

$E: y^2 = x^3 + ax + b \mod{p}$.

We also have a point element $\alpha = (0, 3)$. 


Note, this calculator does **NOT** tell you which points are on a curve. You must determine yourself which points are on the curve.

To init the objects, type in the following:
```
curv = curve(3, 2)
p1 = point(0, 3, 7, curv)
```

Now that the objects have been created, we can perform addition and multiplication between a point!

```
>>> print(p1+p1)
(2, 3)
```

This package also supports multiplication:
```
>>> print(p1*2)
(2, 3)
>>> print(p1*4) 
(4, 6)
```

More functionality (such as determining points on a curve) will be present in the future.