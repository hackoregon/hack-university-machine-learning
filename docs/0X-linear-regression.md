04-Regression

Regression is one of the most basic forms of Machine Leaning
It's often taught in High School and when I was in school we learned the "slope" and "intercept" equation for converting from Fahrenheit to Celsius and Kelvin.

- middle school: pick a point, pick any point
  - rise / run for any pair of points
  - bias/offset for a single point
- high school: use averages to reduce error
  - average rise / average run
    - `slope = mean(diff(y) / diff(x))`
  - average bias/offset
    - `mean(y - a * x)`
- college: [use linear algebra](http://faculty.cas.usf.edu/mbrannick/regression/regma.htm)
  - `y = x * a + b`
  - `a = mean(y - b) / x = inv(x.T * x) * x.T * y`
  - `b = mean(x * a - y)`
- nerd: use optimization
  - `minimize(y - (a * x + b), a0=0, b0=0)`

[Notebooks](../huml/day4)