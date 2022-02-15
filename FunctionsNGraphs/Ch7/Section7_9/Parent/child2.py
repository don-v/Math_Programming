from Parent.child1 import square_arg

def cube_arg(x):
    return x**3

if __name__ == '__main__':
    x = 3
    print('the square of',x, 'is',square_arg(3))
    print('the cube of',x, 'is',cube_arg(3))


'''
so it seems to work now: 

1. to run it as a file from the regular command line:

```python -m Parent.child2```

2. to import it as a module in interpreter:

>> from Parent.child2 import*

great SO response, explanation:
https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time
'''