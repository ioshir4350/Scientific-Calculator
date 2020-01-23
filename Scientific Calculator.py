def factorial(num):
  end = num
  while num>1:
    num = num-1
    end = end*num
  if num==0:
    end = 1
  return end
  
def absval(x):
  if(x<0):
    return x*(-1)
  else:
    return x
  
def pi():   #We said this was inaccurate, however we increasesd the number of terms from 10 to 999999, which makes at least 5 decimals correct
  k=999999
  b=0 
  for i in range(k):
    a = (((((-1)**i))*(1)/((2*i)+1))*4)
    b=b+a
  return b
  
def sin(x):
  x=x % (2*pi())
  k=80
  b=0
  for i in range(k):
    b += (-1)**i * (x**((2*i)+1))/factorial((2*i)+1)
  return b


def cos(x):
  x=x % (2*pi())
  k=80
  b=0 
  for i in range(k):
    a = (((((-1)**i))*(x**(2*i)))/(factorial(2*i)))
    b=b+a
  return b
  
def derivatpoint(f, x):
  ans = (f(x+0.000000001)-f(x))/(.000000001)
  return ans
  
def integral(x1, x2, f):
  k=10
  b=0 
  for i in range(k):
    a = ((x2-x1)/float(k))*(f(x1+(i*((x2-x1)/float(k)))))
    b=b+a
  return b
  
#print(integral(1, 2, lambda x: x+2))

def tan(x):       #kind of slow
  k=0.000001    
  if absval(x-(pi()/2))<k or absval(x-(3*pi()/2))<k or absval(x-(-pi()/2))<k or absval(x-(-3*pi()/2))<k:
    print("undefined")
  else:
    ans = sin(x)/cos(x)
    return ans


#print(tan(pi()/3))
 
def e(x):
  k=1000
  b=0 
  for i in range(k):
    a = ((x**i)/(factorial(i)))
    b=b+a
  return b


def ln(x):
  if (x<1):
    k=100
    b=0 
    for i in range(1,k):
      a = (((-1)**(i-1))*((x-1)**(i)))/(i)
      b=b+a
    return b
  if (x==1):
    ans = 0
    return ans 
  if (x>1):
    x=x-1
    c=10000
    d=0 
    for i in range(0,c):
      f = (((-1)**(i))*((x)**(i+1)))/(i+1)
      d=d+f
    return d

print(ln(0.6))

  
#print(ln(0.6))


def log(base, x):
  potentialans=0
  while potentialans<x:
    if (x!=int(round(base**potentialans))):
      potentialans=potentialans+0.001
    else:
      return potentialans
    
    

def arctan(x):
    k=1000
    partialsum=0
    upperbound=x
    lowerbound=0
    dx = (upperbound-lowerbound)/k
    for i in range(0,k):
      if upperbound<0:
        upperbound=-upperbound
      if lowerbound<upperbound:
        a=((1/(1+(lowerbound**2)))*dx)
        partialsum=a+partialsum
        lowerbound=lowerbound+dx
    finalsum=partialsum
    return finalsum

def arcsin(x):
  if x==1:
    return 1.57079633
  elif x==-1:
    return -1.57079633
  else:
    return arctan(x/((1-(x**2))**0.5))
  
  
#print(tancon(-0.75))
#print(arctan(-1.1338))    
#print(arcsin(-0.70))
  
def arccos(x):
  if x==0:
    return 1.57079633
  elif x<0 and x>-1:
    return (pi()/2)-arcsin(x)
  elif x==-1:
    return 3.14159265
  else:
    return arctan(((1-(x**2))**0.5)/x)

def arccot(x):
  return arctan(1/x)

#print(arccot(-0.5))

def arcsec(x):
  return arccos(1/x)
  
def arccsc(x):
  return arcsin(1/x)
  
#print(arccsc(-1))  
  
#print(arcsec(2))
#print(arccos(0.5))


def lrie(x1, x2, sub, f):
  k=sub
  a=0
  x=x1
  for i in range(0,k):
    a = a+f(x)
    x=x+((x2-x1)/sub)
  return a*((x2-x1)/sub)


#print(lrie(0,1,3,lambda x:x**2))

def rrie(x1, x2, sub, f):
  k=sub
  a=0
  x=x1+((x2-x1)/sub)
  for i in range(0,k):
    a = a+f(x)
    x=x+((x2-x1)/sub)
  return a*((x2-x1)/sub)

#print(rrie(0,1,3,lambda x:x**2))  

def traprie(x1, x2, sub, f):
  k=sub
  a=0
  b=0
  c=0
  x=x1
  for i in range(0,k):
    a=f(x)
    b=f(x+((x2-x1)/sub))
    c=c+a+b
    x=x+((x2-x1)/sub)
  return (c/2)*((x2-x1)/sub)
  
def midrie(x1, x2, sub, f):
  k=sub
  a=0
  b=0
  c=0
  x=x1
  for i in range(0,k):
    a=(x+(x+((x2-x1)/sub)))/2
    b=b+f(a)
    x=x+((x2-x1)/sub)
  return (b)*((x2-x1)/sub)
    
  
#print(midrie(0,1,3,lambda x:x**2)) 

#print(pi())
#print(arccot(-0.5))

