data one;
x = (-1)**(1/2);
run;

proc print data=one;
run;


data two;
pi = constant('pi');
do i = 0 to 2 by (1/4);
x=i*pi;
f=((sin(x)**2)+(cos(x)**2))**(1/2);
g=sin(x)+cos(x);
output;
end;
run;


proc print data=two;
run;

