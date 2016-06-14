def add(s):
	s = s.split()
	x = 0
	for i in s:
		x += float(i)
	if int(x) == x:
		return int(x)
	else:
		return x
def sub(s):
        s = s.split()
        x = float(s[0])
        for i in s[1:]:
                x -= float(i)
        if int(x) == x:
                return int(x)
        else:
                return x
def mul(s):
        s = s.split()
        x = 1
        for i in s:
                x *= float(i)
        if int(x) == x:
                return int(x)
        else:
                return x
def div(s):
        s = s.split()
        x = float(s[0])
        for i in s[1:]:
                x /= float(i)
        if int(x) == x:
                return int(x)
        else:
                return x
                
def test(expr, a, b):
	if expr:
		return a
	else:
		return b

