data one (drop=pi i);
pi = constant('pi');
do i = 0 to 6 by (1/16);
x = i*pi;
f1 = sin(x);
f1a = 4*sin(x);
f1b = sin(4*x);
f1c = (1/4)*sin(x);
f1d = sin((1/4)*x);
f1e = 2*sin((1/4)*x);
f1f = (1/2)*sin(4*x);
f1g = (-1)*4*sin(x);
f1h = sin((-1)*4*x);

f2 = cos(x);
f2a = 4*cos(x);
f2b = cos(4*x);
f2c = (1/4)*cos(x);
f2d = cos((1/4)*x);
f2e = 2*cos((1/4)*x);
f2f = (1/2)*cos(4*x);
f2g = (-1)*4*cos(x);
f2h = cos((-1)*4*x);


output;
end;
run;

proc print data=one; run;

proc sgplot data=one;
scatter x=x y=f1;
scatter x=x y=f1a;
scatter x=x y=f1b;
scatter x=x y=f1c;
scatter x=x y=f1d;
scatter x=x y=f1e;
scatter x=x y=f1f;
scatter x=x y=f1g;
scatter x=x y=f1h;
refline 0/axis=y;
title 'Section 5.6 Q1: sin variations';
run;


proc sgplot data=one;
scatter x=x y=f2;
scatter x=x y=f2a;
scatter x=x y=f2b;
scatter x=x y=f2c;
scatter x=x y=f2d;
scatter x=x y=f2e;
scatter x=x y=f2f;
scatter x=x y=f2g;
scatter x=x y=f2h;
refline 0/axis=y;
title 'Section 5.6 Q2: cos variations';
run;








data two (drop=pi i);
pi = constant('pi');
do i = 0 to 6 by (1/16);
x = i*pi;


f3 = cos(x);
f3a = 3*cos(x);
f3b = cos(3*x);
f3c = (1/3)*cos(x);
f3d = cos((1/3)*x);
f3e = 2*cos((1/3)*x);
f3f = (1/3)*cos(2*x);
f3g = (-1)*3*cos(x);
f3h = cos((-1)*3*x);


f4 = sin(x);
f4a = 3*sin(x);
f4b = sin(3*x);
f4c = (1/3)*sin(x);
f4d = sin((1/3)*x);
f4e = 2*sin((1/3)*x);
f4f = (1/3)*sin(2*x);
f4g = (-1)*3*sin(x);
f4h = sin((-1)*3*x);



output;
end;
run;

proc print data=two; run;


proc sgplot data=two;
scatter x=x y=f3;
scatter x=x y=f3a;
scatter x=x y=f3b;
scatter x=x y=f3c;
scatter x=x y=f3d;
scatter x=x y=f3e;
scatter x=x y=f3f;
scatter x=x y=f3g;
scatter x=x y=f3h;
refline 0/axis=y;
title 'Section 5.6 Q3: cos variations';
run;


proc sgplot data=two;
scatter x=x y=f4;
scatter x=x y=f4a;
scatter x=x y=f4b;
scatter x=x y=f4c;
scatter x=x y=f4d;
scatter x=x y=f4e;
scatter x=x y=f4f;
scatter x=x y=f4g;
scatter x=x y=f4h;
refline 0/axis=y;
title 'Section 5.6 Q4: sin variations';
run;







data three (drop=pi i);
pi = constant('pi');
do i = -2 to 4 by (1/16);
x = i*pi;

f5 = sin(x);
f5a = sin(x-(pi/2));

f6 = cos(x);
f6a = cos(x+(pi/4));

output;
end;
run;

proc print data=three; run;




proc sgplot data=three;
scatter x=x y=f5;
scatter x=x y=f5a;
refline 0/axis=y;
refline 0/axis=x lineattrs=(pattern=dashed);
title 'Section 5.6 Q5: sin variations';
run;


proc sgplot data=three;
scatter x=x y=f6;
scatter x=x y=f6a;
refline 0/axis=y;
refline 0/axis=x lineattrs=(pattern=dashed);
title 'Section 5.6 Q6 cos variations';
run;










