from scipy.optimize import minimize as fmin
from scipy.optimize import curve_fit
from numpy import *
from matplotlib.pyplot import *
ion()

# Measured height of dish along right edge, from top of horizontal L-bracket
# At uprights
x=500-array([0.0,100.3,200.6,300.8,401.1])
y=array([199.7,126.8,71.7,33.3,12.3])

# Midway between uprights
xx=500-array([46.9,150.5,248.7,343.5])
yy=array([163.1,96.8,50.8,22.1])

def ymod(x,*p):
    """Params are:
    p[0], p[1], p[2] = fit y = p[0] + p[1]*(x-p[2])**2
    """
    y = p[0] + p[1]*(x-p[2])**2
    return y

pguess=[1,.001,1]
pfit=curve_fit(ymod,x,y,p0=pguess,method='lm')[0]
xfine=linspace(80,520)
yfitfine=ymod(xfine,*pfit)
yfit=ymod(x,*pfit)
yfit2=ymod(xx,*pfit)

clf()
subplot(2,1,1)   
plot(x,y,'.')
plot(xfine,yfitfine,'k')
xlabel('x (cm)')
ylabel('y (cm)')
legend(['data','best fit parab (at uprights)'],loc='upper left')
xlim(50,550)
ylim(0,225)

subplot(2,1,2)
plot(x,y-yfit,'.',label='at uprights');
plot(xx,yy-yfit2,'.',label='between uprights');
xlim(50,550)
xlabel('x (cm)')
ylabel('residuals (cm)')
legend()
grid('on')
ylim(-.5,.5)
