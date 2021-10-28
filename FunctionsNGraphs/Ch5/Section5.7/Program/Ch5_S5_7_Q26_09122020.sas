/*figure out how to get modulo for tan x to evaluate!*/

/*data test;*/
/*pi = constant('pi');*/
/*do i = 0 to 2 by (1/4);*/
/*x = i*pi;*/
/**/
/**/
/*cel = ceil(x);*/
/*flo = floor(x);*/
/*rnd = round(x);*/
/**/
/**/
/*output;*/
/**/
/*end;*/
/*run;*/
/**/
/*proc print data=test;*/
/*run;*/


data one two;
pi = constant('pi');
do i = -6 to 6 by (1/64);
x = i*pi;

sin = sin(x);
cos = cos(x);


/*g = 1/(tan(x));*/
h = sin/cos;
g = cos/sin;
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

proc format;
value pi2f
0 = '0'
1.57 = 'pi/2'
3.14 = 'pi'
4.71 = '3pi/2'
6.28 = '2pi'
;

value pi2uf
0 = '0'
1.57 = '(*ESC*){unicode "03c0"x}/2'
3.14 = '(*ESC*){unicode "03c0"x}'
4.71 = '3(*ESC*){unicode "03c0"x}/2'
6.28 = '2(*ESC*){unicode "03c0"x}'
;



run;


        

proc sgplot data=one;
/*where (g >= -10 & g <= 10);*/
scatter x=x y=g;
/*scatter x=x y=g2;*/
scatter x=x y=h;
scatter x=x y=f;
refline 0/axis=y;
refline 1.57 4.71/axis=x lineattrs=(pattern=ShortDash color=red);
refline 0 3.14 6.28/axis=x lineattrs=(pattern=ShortDash color=blue);
yaxis max=5 min=-5;
xaxis min=0 max = 6.3 values = (0 1.57 3.14 4.71 6.28) valuesformat=pi2uf.;
title 'q26: f(x) = cot(x)*tan(x)';
run;


proc sgplot data=two;
/*where (g >= -10 & g <= 10);*/
/*scatter x=x y=g;*/
/*scatter x=x y=g2;*/
/*scatter x=x y=h;*/
/*scatter x=x y=f;*/
refline 0/axis=y;
pbspline x=x y=g;
/*pbspline x=x y=g2;*/
pbspline x=x y=h;
pbspline x=x y=f/nknots=10;
title 'q26: f = cot(x)*tan(x)';
run;

proc sgplot data=one;
where (x >= 0 & x <= 6.3);
pbspline x=x y=g;
/*pbspline x=x y=g2;*/
pbspline x=x y=h;
pbspline x=x y=f;
refline 0/axis=y;
title 'q26: f = cot(x)*tan(x)';
run;
