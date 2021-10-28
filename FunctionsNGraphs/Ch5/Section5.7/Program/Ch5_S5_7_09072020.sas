data one (drop=pi i);
pi = constant('pi');
do i = 0 to 2 by (1/64);
x = i*pi;
g = 2**x;
h = sin(x);
h2 = 10*sin(x);
f = g + h;
f2 = g + h2;

output;
end;
run;

proc print data=one; run;

proc sgplot data=one;
scatter x=x y=g;
scatter x=x y=h;
scatter x=x y=f;
scatter x=x y=h2;
scatter x=x y=f2;
title 'Section 5.7 Q15: f = 2**x + sin(x)';
run;

