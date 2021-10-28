data q20_5_7 
(drop=i pi)
;
pi = constant('pi');
do i = 0 to 2.75 by (1/64);
x = i*pi;
g = abs(x+1);
h = cos(2*x);
f = g + h;
output;
end;
run;

data q20_5_7_ 
/*(drop=i pi)*/
;
pi = constant('pi');
do i = -3 to 2.75 by (1/4);
x = i*pi;
g = abs(x+1);
h = cos(2*x);
f = g + h;output;
end;
run;

data q20_5_7_2
(drop=i pi)
;
pi = constant('pi');
do i = 0 to 2 by (1/4);
x = i*pi;
g = abs(x+1);
h = cos(2*x);
f = g + h;output;
end;
run;

proc print; run;

proc sgplot data=q20_5_7;
scatter x=x y=g;
scatter x=x y=h;
scatter x=x y=f;
title 'q20: f = abs(x+1) + cos(2*x)';
run;




