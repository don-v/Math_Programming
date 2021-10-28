data one two;
pi = constant('pi');
do i = -6 to 6 by (1/64);
x = i*pi;
g = cos(x);
g2 = abs(g);
h = 1;
f = g2 + h;
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
        

proc sgplot data=one noautolegend;
scatter x=x y=g/name='cos' legendlabel='y = cos(x)';
scatter x=x y=g2/name='acos' legendlabel='y = abs(cos(x))';
scatter x=x y=h/name='one' legendlabel='y = 1';
scatter x=x y=f/name='g2h' legendlabel='y = abs(cos(x)) + 1';
keylegend 'cos' 'acos' 'one' 'g2h'/title='Function Key' across=1 down=4;
refline 0/axis=y;
refline 1/axis=y lineattrs=(pattern=ShortDash color=red);
refline -1/axis=y lineattrs=(pattern=ShortDash color=blue);
yaxis max=3 min=-1;
xaxis min=0 max = 6.3 values = (0 1.57 3.14 4.71 6.28) valuesformat=pi2uf.;
title 'q28: f(x) = abs(cos(x)) + 1';
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
