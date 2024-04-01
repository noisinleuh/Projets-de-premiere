from turtle import*
from math import*

def interlettre(l):
    up()
    forward(0.25*l)
    down()
    
def space(l):
    up()
    forward(l*2/3)
    down()

def apos(l):
    up()
    forward(0.25*l)
    left(90)
    forward(l*1.5)
    down()
    forward(l*0.5)
    up()
    forward(-l*2)
    right(90)
    forward(0.25*l)
    down()
    
def largeur_apos(l):
    return l/3 

def à(l):
    up()
    left(90)
    forward(2*l)
    right(90)
    forward(0.25*l)
    left(90)
    forward(0.75*l)
    right(135)
    down()
    forward(0.75*l)
    up()
    forward(-0.75*l)
    left(135)
    forward(-2.75*l)
    right(90)
    forward(-0.25*l)
    down()
    left(75)
    forward(sqrt((l*2)**2+(l/2)**2))
    right(150)
    forward(sqrt((l*2)**2+(l/2)**2))
    forward(-(sqrt((l*2)**2+(l/2)**2)/2))
    right(105)
    forward(l/2)
    forward(-(l/2))
    left(105)
    forward((sqrt((l*2)**2+(l/2)**2)/2))
    left(75)
    
def largeur_à(l):
    return l

def a(l):
    left(75)
    forward(sqrt((l*2)**2+(l/2)**2))
    right(150)
    forward(sqrt((l*2)**2+(l/2)**2))
    forward(-(sqrt((l*2)**2+(l/2)**2)/2))
    right(105)
    forward(l/2)
    forward(-(l/2))
    left(105)
    forward((sqrt((l*2)**2+(l/2)**2)/2))
    left(75)
    
def largeur_a(l):
    return l
    
def b(l):
    left(90)
    forward(2*l)
    right(90)
    forward(2/5*l)
    circle(-2*l/5,180)
    forward(2/5*l)
    left(180)
    forward(2/5*l)
    circle(-3*l/5,180)
    forward(2/5*l)
    left(180)
    up()
    forward(l)
    down()
    
def largeur_b(l):
    return l

def c(l):
    up()
    forward(l)
    down()
    circle(l,-180)
    left(90)
    up()
    forward(2*l)
    down()
    left(90)
    
def largeur_c(l):
    return l
    

def d(l):
    
    left(90)
    forward(2*l)
    right(90)
    forward(0.25*l)
    circle(-l,180)
    forward(0.25*l)
    left (180)
    up()
    forward(l*1.25)
    down()
    
   
def largeur_d(l):
    return l*1.25

def é(l):
    left(90)
    forward(2*l)
    up()
    right(90)
    forward(0.25*l)
    left(90)
    forward(0.25*l)
    right(45)
    down()
    forward(0.75*l)
    up()
    forward(-0.75*l)
    left(45)
    forward(-0.25*l)
    right(90)
    forward(-0.25*l)
    left(90)
    down()
    right(90)
    forward(l)
    forward(-l)
    right(90)
    forward(l)
    left(90)
    forward(l/1.5)
    forward(-l/1.5)
    right(90)
    forward(l)
    left(90)
    forward(l)

def largeur_é(l):
    return l

def è(l):
    left(90)
    forward(2*l)
    up()
    right(90)
    forward(0.25*l)
    left(90)
    forward(0.75*l)
    right(135)
    down()
    forward(0.75*l)
    up()
    forward(-0.75*l)
    left(135)
    forward(-0.75*l)
    right(90)
    forward(-0.25*l)
    left(90)
    down()
    right(90)
    forward(l)
    forward(-l)
    right(90)
    forward(l)
    left(90)
    forward(l/1.5)
    forward(-l/1.5)
    right(90)
    forward(l)
    left(90)
    forward(l)

def largeur_è(l):
    return l

def e(l):
    left(90)
    forward(2*l)
    right(90)
    forward(l)
    forward(-l)
    right(90)
    forward(l)
    left(90)
    forward(l/1.5)
    forward(-l/1.5)
    right(90)
    forward(l)
    left(90)
    forward(l)


    
def largeur_e(l):
    return l

def f(l):
    left(90)
    forward(2*l)
    right(90)
    forward(l)
    forward(-l)
    right(90)
    forward(l)
    left(90)
    forward(l)
    forward(-l)
    right(90)
    forward(l)
    left(90)
    up()
    forward(l)
    down()
    
def largeur_f(l):
    return l

def g(l):
    up()
    left(90)
    forward(l)
    right(90)
    forward(l)
    down()
    forward(l)
    right(90)
    circle(-l,300)
    up()
    circle(-l,-300)
    forward(l)
    left(90)
    down()
    
def largeur_g(l):
    return 2*l

def h(l):
    left(90)
    forward(2*l)
    forward(-l)
    right(90)
    forward(l)
    left(90)
    forward(l)
    forward(-l*2)
    right(90)

def largeur_h(l):
    return l
    
def i(l):
    forward(l/2)
    forward(-l/4)
    left(90)
    forward(2*l)
    left(90)
    forward(-l/4)
    forward(l/2)
    up()
    left(90)
    forward(2*l)
    left(90)
    forward(l/2)
    down()

def largeur_i(l):
    return l/2
    
def j(l):
    up()
    left(90)
    forward(l/2)
    right(180)
    down()
    circle(l/2,180)
    forward(1.5*l)
    right(90)
    forward(-l/2)
    forward(l)
    up()
    right(90)
    forward(2*l)
    left(90)
    down()   
    
def largeur_j(l):
    return l*1.5
    
def k(l):
    left(90)
    forward(l*2)
    forward(-l)
    right(45)
    forward((sqrt((l*2)**2+((l/2)**2)))/1.5)
    forward(-(sqrt((l*2)**2+((l/2)**2)))/1.5)
    right(90)
    forward((sqrt((l*2)**2+((l/2)**2)))/1.5)
    left(45)
    
def largeur_k(l):
    return l

def l(l):
    left(90)
    forward(l*2)
    forward(-l*2)
    right(90)
    forward(l)
    
def largeur_l(l):
    return l
    
def m(l):
    left(90)
    forward(l*2)
    right (150)
    forward((sqrt((l)**2+((l/2)**2))))
    left(120)
    forward((sqrt((l)**2+((l/2)**2))))
    right(150)
    forward(l*2)
    left(90)
    
def largeur_m(l):
    return l

def n(l):
    left(90)
    forward(l*2)
    right (150)
    forward((sqrt((l)**2+((l/2)**2)))*2)
    left(150)
    forward(l*2)
    forward(-l*2)
    right(90)
    
def largeur_n(l):
    return l

def o(l):
    up()
    forward(l)
    down()
    circle(l)
    up()
    forward(l)
    down()
    
def largeur_o(l):
    return l*2

def p(l):
    left(90)
    forward(l*2)
    right(90)
    circle(-l/1.5,180)
    left(90)
    forward(0.75*l)
    left(90)
    up()
    forward(0.75*l)
    down()
    
def largeur_p(l):
    return l*1.5
    
def q(l):
    up()
    forward(l)
    down()
    circle(l)
    up()
    left(90)
    forward(l/2)
    down()
    right(135)
    forward(sqrt(((l/2)**2+(l/2)**2)))
    left(45)
    up()
    forward(l*0.5)
    down()
    
def largeur_q(l):
    return l*2

def r(l):
    left(90)
    forward(l*2)
    right(90)
    circle(-l/1.5,180)
    right(180)
    circle(l/1.5,36)
    right(111)
    forward(8*l/10)
    left(75)
    
def largeur_r(l):
    return l*1.5

def s(l):
    up()
    forward(0.25*l)
    down()
    forward(0.25*l)
    circle(l/2,180)
    circle(-l/2,180)
    forward(0.25*l)
    up()
    right(90)
    forward(2*l)
    left(90)
    forward(0.25*l)
    down()
    
def largeur_s(l):
    return l*1.25
    
def t(l):
    up()
    forward(l/2)
    down()
    left(90)
    forward(2*l)
    left(90)
    forward(l/2)
    forward(-l)
    up()
    left(90)
    forward(2*l)
    left(90)
    down()
    
def largeur_t(l):
    return l

def u(l):
    up()
    left(90)
    forward(l*0.5)
    down()
    forward(l*1.5)
    forward(-l*1.5)
    left(180)
    circle(l/2,180)
    forward(l*1.5)
    forward(-l*1.5)
    up()
    forward(-l*0.5)
    right(90)
    
def largeur_u(l):
    return l
    
def v(l):
    up()
    left(90)
    forward(l*2)
    down()
    right(165)
    forward(sqrt((l*2)**2+(l/2)**2))
    left(150)
    forward(sqrt((l*2)**2+(l/2)**2))
    right(165)
    up()
    forward(2*l)
    down()
    left(90)
    
def largeur_v(l):
    return l

def w(l):
    up()
    left(90)
    forward(l*2)
    down()
    right(165)
    forward(sqrt((l*2)**2+(l/2)**2))
    left(150)
    forward(sqrt((l*2)**2+(l/2)**2))
    right(150)
    forward(sqrt((l*2)**2+(l/2)**2))
    left(150)
    forward(sqrt((l*2)**2+(l/2)**2))
    right(165)
    up()
    forward(2*l)
    down()
    left(90)
    
def largeur_w(l):
    return 2*l

def x(l):
    left(65)
    forward(sqrt((l*2)**2+(l**2)))
    forward(-(sqrt((l*2)**2+(l**2)))/2)
    left(55)
    forward((sqrt((l*2)**2+(l**2)))/2)
    forward(-(sqrt((l*2)**2+(l**2))))
    right(120)
    
def largeur_x(l):
    return l

def y(l):
    up()
    forward(l/2)
    down()
    right(90)
    forward(-l)
    right(150)
    forward(sqrt((l/2)**2+(l**2)))
    forward(-(sqrt((l/2)**2+(l**2))))    
    right(60)
    forward(sqrt((l/2)**2+(l**2)))
    forward(-(sqrt((l/2)**2+(l**2))))
    right(150)
    up()
    forward(l)
    left(90)
    forward(l/1.8)
    down()
    
def largeur_y(l):
    return l

def z(l):
    forward(l)
    forward(-l)
    left(60)
    forward(sqrt((l)**2+((l*2)**2)))
    right(240)
    forward(l)
    forward(-l)
    left(90)
    up()
    forward(l*2)
    left(90)
    down()
    
def largeur_z(l):
    return l

def un(l):
    up()
    forward(0.5*l)
    down()
    left(90)
    forward(2*l)
    left(155)
    forward(sqrt((0.5*l)**2+l**2))
    forward(-sqrt((0.5*l)**2+l**2))
    left(25)
    forward(2*l)
    left(90)
    forward(-0.25*l)
    forward(0.5*l)

def largeur_un(l):
    return 0.75*l

def deux(l):
    forward(l)
    forward(-l)
    left(57)
    forward(sqrt((1.5*l)**2+l**2))
    left(33)
    circle(0.5*l,180)
    up()
    forward(1.5*l)
    left(90)
    forward(l)
    down()

def largeur_deux(l):
    return l

def trois(l):
    up()
    forward(0.5*l)
    left(90)
    forward(l)
    down()
    right(-90)
    circle(0.5*l,-270)
    circle(0.5*l,270)
    circle(-0.5*l,-220)
    circle(-0.5*l,220)
    up()
    left(90)
    forward(l)
    left(90)
    forward(0.5*l)

def largeur_trois(l):
    return l

def quatre(l):
    up()
    forward(0.75*l)
    down()
    left(90)
    forward(2*l)
    left(150)
    forward(sqrt(l**2+l**2))
    left(120)
    forward(l)
    up()
    right(90)
    forward(0.78*l)
    left(90)
    down()

def largeur_quatre(l):
    return l

def cinq(l):
    forward(0.25*l)
    circle(l*0.75,180)
    forward(0.25*l)
    right(90)
    forward(0.5*l)
    right(90)
    forward(l)
    up()
    right(90)
    forward(2*l)
    left(90)
    down()

def largeur_cinq(l):
    return l

def six(l):
    up()
    forward(0.5*l)
    down()
    circle(l*0.5)
    circle(l*0.5,-90)
    forward(-l)
    right(180)
    circle(-0.5*l,180)
    up()
    forward(1.5*l)
    left(90)
    down()

def largeur_six(l):
    return l

def sept(l):
    left(63)
    forward(sqrt((2*l)**2+l**2)/2)
    left(-63)
    forward(-0.25*l)
    forward(0.5*l)
    forward(-0.25*l)
    left(63)
    forward(sqrt((2*l)**2+l**2)/2)
    left(117)
    forward(l)
    up()
    left(90)
    forward(2*l)
    left(90)
    forward(l)
    down()

def largeur_sept(l):
    return l    

def huit(l):
    up()
    forward(0.5*l)
    down()
    circle(l*0.5)
    circle(l*0.5,180)
    circle(-0.5*l)
    up()
    left(90)
    forward(l)
    left(90)
    forward(l*0.5)
    down()

def largeur_huit(l):
    return l

def neuf(l):
    up()
    forward(0.5*l)
    left(90)
    forward(l)
    down()
    right(90)
    circle(l*0.5)
    circle(l*0.5,90)
    forward(-l)
    circle(0.5*l,-180)
    up()
    forward(0.5*l)
    left(90)
    forward(l)
    down()

def largeur_neuf(l):
    return l

def zéro(l):
    up()
    forward(0.5*l)
    down()
    circle(0.5*l,90)
    forward(l)
    circle(0.5*l,180)
    forward(l)
    circle(0.5*l,90)
    up()
    forward(0.5*l)
    down()

def largeur_zéro(l):
    return l

def smile(l):
    up()
    forward(0.75*l)
    down()
    circle(l)
    up()
    left(90)
    forward(0.25*l)
    down()
    right(90)
    circle(0.5*l,90)
    left(90)
    forward(l)
    left(90)
    circle(0.5*l,90)
    left(90)
    up()
    forward(l)
    left(90)
    forward(0.25*l)
    down()
    dot(3)
    up()
    forward(-0.5*l)
    down()
    dot(3)
    up()
    left(90)
    forward(1.25*l)
    left(90)
    forward(0.75*l)

def largeur_smile(l):
    return 2*l

def exc(l):
    dot(3)
    up()
    left(90)
    forward(0.5*l)
    down()
    forward(l*1.5)
    up()
    forward(-2*l)
    right(90)
    down()
    
def intero(l):
    dot(3)
    up()
    left(90)
    forward(0.5*l)
    down()
    forward(l*0.5)
    right(90)
    circle(0.5*l,270)
    circle(0.5*l,-270)    
    up()
    left(90)
    forward(-l)
    right(90)
    down()

def point(l):
    dot(3)  

def coeur(l):
    up()
    forward(l)
    down()
    left(45)
    forward(sqrt(l**2+l**2))
    left(45)
    forward(0.5*l)
    circle(0.5*l,180)
    circle(-0.5*l,-180)
    left(180)
    forward(0.5*l)
    left(45)
    forward(sqrt(l**2+l**2))
    up()
    left(45)
    forward(l)
    down()

def largeur_coeur(l):
    return 2*l