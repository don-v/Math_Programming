
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



%macro trig_add(
q = ,

g = ,
h = ,
f = ,

ymin = ,
ymax = ,

xform = twopi/*neg2pi, neg6pi, twopi, sixpi*/
);


%if &xform = neg2pi %then %do;

%let valf = %nrstr((-6.28 -4.71 -3.14 -1.57 0 1.57 3.14 4.71 6.28) valuesformat=pi2u_neg2pi_2pi_f.);
%let xmin = -6.28;
%let xmax = 6.28;

%end; %else %do;

%if &xform = neg6pi %then %do;


%let valf = %nrstr((-6.28 -4.71 -3.14 -1.57 0 1.57 3.14 4.71 6.28) valuesformat=pi2u_neg2pi_2pi_f.);
%let xmin = -6.28;
%let xmax = 6.28;

%end; %else %do;

%if &xform = twopi %then %do;


%let valf = %nrstr((0 1.57 3.14 4.71 6.28) valuesformat=pi2uf.);
%let xmin = 0;
%let xmax = 6.28;


%end; %else %do;


%let valf = %nrstr((
 0   
 1.57
 3.14
 4.71
 6.28
 7.85
 9.42
11.00
12.57
14.14
15.71
17.28
18.85
) 

valuesformat=sixpi2uf.);
%let xmin = 0;
%let xmax = 19;


%end; 

%end;

%end;

/*%end;*/




/*overlay data*/

data one two;
pi = constant('pi');
do i = -6 to 6 by (1/64);
x = i*pi;
g = &g;
h = &h;
f = &g + &h;
if (i GE 0 & i LE 2) & (mod(i,(1/4)) = 0) then output two; 
output one;
end;
run;


/*panel data*/

data three;
length
panel_c $ 25;
pi = constant('pi');
do i = -6 to 6 by (1/64);
/*do i = -6 to 6 by (1/2);*/
x = i*pi;
do panel = 0 to 2;

if panel = 0 then do;
panel_c = "A: f = &g";
f = &g;

end; else do;

if panel = 1 then do;

panel_c = "B: f = &h";
f = &h;

end; else do;

panel_c = "C: f = &g + &h";
f = &g + &h;


end;

end;

output;
end;
end;
run;




/*overlay plot*/

proc sgplot data=one noautolegend;
scatter x=x y=g/name='g' legendlabel="y = &g";
scatter x=x y=h/name='h' legendlabel="y = &h";
scatter x=x y=f/name='f' legendlabel="y = &g + &h";
keylegend 'g' 'f' 'h' /title='Function Key' across=1 down=3;
refline 0/axis=y;
refline 0/axis=x;
refline -1/axis = x lineattrs=(pattern=ShortDash color=black);
refline 1/axis=y lineattrs=(pattern=ShortDash color=red);
refline -1/axis=y lineattrs=(pattern=ShortDash color=blue);
yaxis max= &ymax min= &ymin;
xaxis max= &xmax min = &xmin &valf; 


title "Q&q.: f(x) = &g + &h";
run;



/*sort, print, describe data sets*/

proc contents data=three; run;

proc sort data=three out=three_sort; by panel_c; run;
/*proc print data=three_sort; run;*/

proc print data=one; run;
proc print data=two 
(drop=i pi)
; 
run;



/*panel plot*/

data myattrmap;
input ID $ value $ linecolor $ fillcolor $;
datalines;
myid  0  blue blue
myid  1 red red
myid  2 green green
;



proc sgpanel data=three_sort dattrmap=myattrmap noautolegend;
panelby panel_c / columns = 3 novarname spacing = 10;
styleattrs datacolors=(blue red);
scatter x=x y=f/group=panel attrid=myid;
refline 0/axis=y;
refline 0/axis=x;
/*refline -1/axis = x lineattrs=(pattern=ShortDash color=black);*/
refline 1/axis=y lineattrs=(pattern=ShortDash color=black);
refline -1/axis=y lineattrs=(pattern=ShortDash color=black);

rowaxis max= &ymax min= &ymin;
colaxis max= &xmax min = &xmin &valf; 


title "Q&q.: f(x) = &g + &h";
run;

%mend;





%trig_add(
q = 1,

g = x**2,
h = x-2,
f = (x**2) + (x-2),

ymin = -3,
ymax = 3,

xform = twopi/*neg2pi, neg6pi, twopi, sixpi*/
)
