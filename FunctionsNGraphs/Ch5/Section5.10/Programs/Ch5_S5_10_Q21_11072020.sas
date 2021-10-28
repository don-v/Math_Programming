/*make sure your current directory is set to where you want your graphics to be stored!*/
%let path = %nrstr(.);



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

value pi2u_neg2pi_2pi_f
-1.57 = '-(*ESC*){unicode "03c0"x}/2'
-3.14 = '-(*ESC*){unicode "03c0"x}'
-4.71 = '-3(*ESC*){unicode "03c0"x}/2'
-6.28 = '-2(*ESC*){unicode "03c0"x}'
0 = '0'
1.57 = '(*ESC*){unicode "03c0"x}/2'
3.14 = '(*ESC*){unicode "03c0"x}'
4.71 = '3(*ESC*){unicode "03c0"x}/2'
6.28 = '2(*ESC*){unicode "03c0"x}'
;


value pi2uf
0 	 = '0'
1.57 = '(*ESC*){unicode "03c0"x}/2'
3.14 = '(*ESC*){unicode "03c0"x}'
4.71 = '3(*ESC*){unicode "03c0"x}/2'
6.28 = '2(*ESC*){unicode "03c0"x}'
;



value sixpi2uf


 0    = '0' 	
 1.57= '(*ESC*){unicode "03c0"x}/2'		
 3.14= '(*ESC*){unicode "03c0"x}'
 4.71= '3(*ESC*){unicode "03c0"x}/2'
 6.28= '2(*ESC*){unicode "03c0"x}'
 7.85= '5(*ESC*){unicode "03c0"x}/2'
 9.42= '3(*ESC*){unicode "03c0"x}'
11.00= '7(*ESC*){unicode "03c0"x}/2'
12.57= '4(*ESC*){unicode "03c0"x}'
14.14= '9(*ESC*){unicode "03c0"x}/2'
15.71= '5(*ESC*){unicode "03c0"x}'
17.28= '11(*ESC*){unicode "03c0"x}/2'
18.85= '6(*ESC*){unicode "03c0"x}'

;



run;


%let valf = %nrstr(values = (-6.28 -4.71 -3.14 -1.57 0 1.57 3.14 4.71 6.28) valuesformat=pi2u_neg2pi_2pi_f.);
%let xmin = -6.28;
%let xmax = 6.28;





data one two;
pi = constant('pi');
do i = -5 to 5 by (1/64);
x = i*pi;
g = 2**(-x);
g2 = -g;
h = sin(2*x);
f = g*h;
if (x GE -6.3 & x LE 6.3) & (mod(i,(1/4)) = 0) then output two; 
output one;
end;
run;

proc print data=one; run;
proc print data=two 
/*(drop=i pi)*/
; 
run;

%let q=25;

ods listing gpath = "&path";
ods graphics / imagename = "Q&q._overlay" imagefmt = png;


proc sgplot data=one;
where (x >= -6.3 & x <= 6.3);
scatter x=x y=g;
scatter x=x y=g2;
scatter x=x y=h;
scatter x=x y=f;
refline 0/axis=y;
xaxis max= &xmax min = &xmin &valf; 
title 'q25: f = (2**(-x))*sin(2*x)';
run;


