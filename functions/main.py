# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

#defining greet function.
def greet(name):
    greet  = f'Hello, {name}!'
    return (greet)

print (greet('Bob'))

#2. Defining add function.
def add(q, w, e):
    addup = q + w + e
    return addup

groceries = add(5, 8, 12)
print (groceries)

#3. Defining positive function as boolean.
def positive(x):
    pos = x > 0
    return bool(pos)

print (positive(5))

#4. Defining negative function as boolean.
def negative(x):
    neg = x < 0
    return bool(neg)

print (negative(-5))
