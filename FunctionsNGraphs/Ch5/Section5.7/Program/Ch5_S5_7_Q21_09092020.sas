data one two;
pi = constant('pi');
do i = -5 to 5 by (1/64);
x = i*pi;
g = 2**(-x);
g2 = -g;
h = cos(x);
f = g*h;
if (i GE 0 & i LE 2) & (mod(i,(1/4)) = 0) then output two; 
output one;
end;
run;

proc print data=one; run;
proc print data=two 
/*(drop=i pi)*/
; 
run;

proc sgplot data=one;
where (x >= 0 & x <= 6.3);
scatter x=x y=g;
scatter x=x y=g2;
scatter x=x y=h;
scatter x=x y=f;
refline 0/axis=y;
title 'q21: f = (2**(-x))*cos(x)';
run;


