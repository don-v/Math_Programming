data q18_5_7 (drop=i pi);
pi = constant('pi');
do i = 0 to 2 by (1/64);
x = i*pi;
g = x;
h = -sin(x);
f = g + h;
output;
end;
run;

data q18_5_7_ (drop=i pi);
pi = constant('pi');
do i = 0 to 2 by (1/4);
x = i*pi;
g = x;
h = -sin(x);
f = g + h;
output;
end;
run;

proc print; run;

proc sgplot data=q18_5_7;
scatter x=x y=g;
scatter x=x y=h;
scatter x=x y=f;
title 'q18: f = x - sin(x)';
run;




