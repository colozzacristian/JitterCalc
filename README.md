# The math behind

## Precise jitter
$$
\sqrt\frac{(num_0-Avg)^2+...+(num_n-Avg)^2}{N-1}
$$
## Less precise jitter
$$
\sqrt\frac{(num_0-Avg)^2+...+(num_n-Avg)^2}{N}
$$

# Usage
To call the program you must be in the same directory as the file.
To use it:
```
python3 jittercalc.py <num1> <num2> ... <numN>
```
There is no limit on how many values you can input.
