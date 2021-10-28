data one two;
pi = constant('pi');
do i = -6 to 6 by (1/64);
x = i*pi;
g = (1/2)*(x**2);
g2 = -g;
h = sin(x);
f = g*h;
if (i GE 0 & i LE 2) & (mod(i,(1/4)) = 0) then output two; 
output one;
end;
run;

proc print data=one; run;
proc print data=two 
(drop=i pi)
; 
run;

proc sgplot data=one;
/*where (g >= -10 & g <= 10);*/
scatter x=x y=g;
scatter x=x y=g2;
scatter x=x y=h;
scatter x=x y=f;
refline 0/axis=y;
title 'q25: f = ((1/2)*(x**2))*sin(x)';
run;


proc sgplot data=two;
/*where (g >= -10 & g <= 10);*/
/*scatter x=x y=g;*/
/*scatter x=x y=g2;*/
/*scatter x=x y=h;*/
/*scatter x=x y=f;*/
refline 0/axis=y;
pbspline x=x y=g;
pbspline x=x y=g2;
pbspline x=x y=h;
pbspline x=x y=f/nknots=10;
title 'q25: f = ((1/2)*(x**2))*sin(x)';
run;

proc sgplot data=one;
where (x >= 0 & x <= 6.3);
pbspline x=x y=g;
pbspline x=x y=g2;
pbspline x=x y=h;
pbspline x=x y=f;
refline 0/axis=y;
title 'q25: f = ((1/2)*(x**2))*sin(x)';
run;
