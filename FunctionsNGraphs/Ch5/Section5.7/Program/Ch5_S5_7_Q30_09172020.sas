data one two;
pi = constant('pi');
do i = -6 to 6 by (1/64);
x = i*pi;
absx = abs(x);
x1=x+1;
absx1 = abs(x+1);
g = cos(x);
h = cos(x + 1);
f = cos(absx1);
if (i GE -2 & i LE 2) & (mod(i,(1/4)) = 0) then output two; 
output one;
end;
run;


data three;
length
panel_c $ 25;
pi = constant('pi');
do i = -6 to 6 by (1/64);
/*do i = -6 to 6 by (1/2);*/
x = i*pi;
absx = abs(x);
absx1 = abs(x+1);
do panel = 0 to 2;
/*if panel = 0 then f = sin(x); else*/
/*f = sin(absx);*/

if panel = 0 then do;
panel_c = 'A: f = cos(x)';
f = cos(x);

end; else do;

if panel = 1 then do;

panel_c = 'B: f = cos(x + 1)';
f = cos(x + 1);

end; else do;

panel_c = 'C: f = cos(abs(x + 1))';
f = cos(absx1);


end;

end;

output;
end;
end;
run;

/*proc print data=three; run;*/

proc contents data=three; run;

proc sort data=three out=three_sort; by panel_c; run;
/*proc print data=three_sort; run;*/

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




run;
        

proc sgplot data=one noautolegend;
scatter x=x y=g/name='cosx' legendlabel='y = cos(x)';
scatter x=x y=h/name='cosx1' legendlabel='y = cos(x + 1)';
scatter x=x y=f/name='cosax' legendlabel='y = cos(abs(x + 1))';
keylegend 'cosx' 'cosx1' 'cosax' /title='Function Key' across=1 down=3;
refline 0/axis=y;
refline 0/axis=x;
refline -1/axis = x lineattrs=(pattern=ShortDash color=black);
refline 1/axis=y lineattrs=(pattern=ShortDash color=red);
refline -1/axis=y lineattrs=(pattern=ShortDash color=blue);
yaxis max=1 min=-1;
xaxis min=-6.3 max = 6.3 values = (-6.28 -4.71 -3.14 -1.57 0 1.57 3.14 4.71 6.28) valuesformat=pi2u_neg2pi_2pi_f.;
title 'q30: f(x) = cos(abs(x + 1))';
run;


data myattrmap;
input ID $ value $ linecolor $ fillcolor $;
datalines;
myid  0  blue blue

myid  1 red red

myid  2 green green

;

/*proc sgpanel data=test dattrmap=myattrmap;*/
/*panelby mean;*/
/*hbar x / group=mean attrid=myid;*/
/*run;*/


proc sgpanel data=three_sort dattrmap=myattrmap noautolegend;
panelby panel_c / columns = 3 novarname spacing = 10;
styleattrs datacolors=(blue red);
scatter x=x y=f/group=panel attrid=myid;
refline 0/axis=y;
refline 0/axis=x;
/*refline -1/axis = x lineattrs=(pattern=ShortDash color=black);*/
refline 1/axis=y lineattrs=(pattern=ShortDash color=black);
refline -1/axis=y lineattrs=(pattern=ShortDash color=black);
rowaxis max=1 min=-1;
colaxis min=-6.3 max = 6.3 values = (-6.28 -4.71 -3.14 -1.57 0 1.57 3.14 4.71 6.28) valuesformat=pi2u_neg2pi_2pi_f.;

/*yaxis max=1 min=-1;*/
/*xaxis min=-6.3 max = 6.3 values = (-6.28 -4.71 -3.14 -1.57 0 1.57 3.14 4.71 6.28) valuesformat=pi2u_neg2pi_2pi_f.;*/
title 'q30: f(x) = cos(abs(x + 1)) paneled';
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





data test;
do mean= 5, 10;
     do i = 1 to 100;
          x = rand("Poisson", mean);
          output;
          end;
     end;
run;

data myattrmap;
input ID $ value $ linecolor $ fillcolor $;
datalines;
myid  5  blue blue

myid  10 orange orange

;

proc sgpanel data=test dattrmap=myattrmap;
panelby mean;
hbar x / group=mean attrid=myid;
run;



data four;
length
panel_c $ 25;
pi = constant('pi');
/*do i = -6 to 6 by (1/64);*/
/*do i = -6 to 6 by (1/2);*/
do i = -2 to 2 by (1/4);
x = i*pi;
absx = abs(x);
do panel = 0 to 1;
/*if panel = 0 then f = sin(x); else*/
/*f = sin(absx);*/

if panel = 0 then do;
panel_c = 'A: f = sin(x)';
f = sin(x);

end; else do;
panel_c = 'B: f = sin(abs(x))';
f = sin(absx);

end;

output;
end;
end;
run;


proc contents data=four;
run;























