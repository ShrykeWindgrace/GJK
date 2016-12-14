from math import sqrt

def add(p1, p2):
    return (p1[0] + p2[0], p1[1] + p2[1])

def neg(p1):
    return (-p1[0], -p1[1])

def sub(p1, p2):
    return add(p1, neg(p2))

def dot(p1, p2):
    return p1[0] * p2[0] + p1[1] * p2[1]

def doubleCross(a, e):
    # returns e\times e\times a 
    # this vector is orthogonal to e and its scalar product with a is negative

    return (e[0]*e[1]*a[0]-e[1]*e[1]*a[1],
            e[0]*e[1]*a[1]-e[0]*e[0]*a[0])

def furthest(shape, d):
    #print("shape with ", len(shape), " vertices")
    dis = dot(shape[0], d)
    j = 0

    for i in range(1, len(shape)):
       dis_temp = dot(shape[i], d)
       if dis_temp > dis:
            j = i
            dis = dis_temp

    return (dis, shape[j])

def cross (a, b):
    return a[0]*b[1] - a[1]*b[0]

def inTrig(a, b, c):
    ab = sub (b, a)
    bc = sub (c, b)
    ca = sub (a, c)

    sa = cross(bc, a)
    sb = cross(ca, b)
    sc = cross(ab, c)

    return (sa >=0 and sb>=0 and sc >= 0) or (sa <=0 and sb<=0 and sc <= 0)

def distTwo(a, b): #  returns a direction to the closest point on the interval
    # the distance itself
    # and the type 0 for point, 1 for interval
    # will return interval in degenerate cases

    e = sub(b, a)
    te = dot(a, e) 
    
    if te > 0:
        return (a, dot(a,a), 0)

    if te < - dot(e, e):
        return (b, dot(b,b), 0)
    
    te = doubleCross(a, e)
    print(te)
    return (te, - dot(te, te), 1)

simplices = []

poly1 = [(2,0), (3,0), (3,1),(2,1)]
poly2 = [(1,0), (-1,0), (0,1),(0,-1)]
testShape = []
for p in poly1:
    for q in poly2:
        testShape.append(sub(p,q))

d = (0,1)#
#d = (1,0)
r, s = furthest(testShape,d)
r2, s2 = furthest(testShape, neg(d))
simplices.append((r, s, 0))
simplices.append((-r2, s2, 0)) #  0 for "point"


if r*r2 < 0:
    print("the direction ", d, " shows that 0 is not in the testShape")
else:
    print("the direction ", d, "is inconclusive")

WTFFlag = False
inThere = False
while(True):
    if (len(simplices)<2):
        WTFFlag = True
        break
    if (len(simplices) == 2):
        pass

    if (len(simplices) == 3):
        if inTrig(simplices[0][0], simplices[1][0], simplices[2][0]):
            inThere = True
            break
        else:
            pass


    break
if WTFFlag:
    print("WTF happenned")

print("Our search yielded ", inThere)
#print(distTwo((1,1), (2,0)))

#print(testShape)

#print(inTrig((1,1), (-0.5, 1),(-0.6, -1)))
#print(inTrig((1,1), (0.5, 1),(0.6, -1)))

#print(doubleCross((1,0),(0,1)))
#print(poly)
#print(furthest(shape=poly, d=(2,1)))
