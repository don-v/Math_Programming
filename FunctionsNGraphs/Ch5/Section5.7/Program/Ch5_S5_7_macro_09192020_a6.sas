/*replace period ('.') below with path to location where graphics files should be saved*/
%let path = %nrstr(.);


data myattrmap;
input ID $ value $ linecolor $ fillcolor $;
datalines;
myid  0  blue blue
myid  1 red red
myid  2 green green
;





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






options mprint mlogic symbolgen;

%macro trig_add(

q = 1,

g = %quote(cos(x)),
h = %quote(3*sin(x)),

tan =0,
b = %str(&h),
f =%str(&g + &h),

altb = %nrstr(),
altf = %nrstr(),



ymin = -3, 
ymax = 3,

xform=twopi  
)
;


/*
neg2pi 
neg6pi 
twopi 
sixpi
*/


%if &tan=1 %then %do;

%let b = &altb;
%let f = &altf;

%end;




%if &xform =neg2pi %then %do;

%let valf = %nrstr(values = (-6.28 -4.71 -3.14 -1.57 0 1.57 3.14 4.71 6.28) valuesformat=pi2u_neg2pi_2pi_f.);
%let xmin = -6.28;
%let xmax = 6.28;

%end; %else %do;

%if &xform =neg6pi %then %do;


%let valf = %nrstr(values = (-6.28 -4.71 -3.14 -1.57 0 1.57 3.14 4.71 6.28) valuesformat=pi2u_neg2pi_2pi_f.);
%let xmin = -6.28;
%let xmax = 6.28;

%end; %else %do;

%if &xform =twopi %then %do;


%let valf = %nrstr(values = (0 1.57 3.14 4.71 6.28) valuesformat=pi2uf.);
%let xmin = 0;
%let xmax = 6.28;


%end; %else %do;


%let valf = %nrstr(values = (
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


















/*%put &xmin;*/
/*%put &xmax;*/
/*%put &valf;*/



/*data one;*/
/*x = 0;*/
/*y = &g;*/
/*z = &h;*/
/*run;*/
/**/
/*proc print data=one; run;*/




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
panel_c $ 40;
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

panel_c = "B: f = &b";
f = &h;

end; else do;

panel_c = "C: f = &f";
f = &g + &h;


end;

end;

output;
end;
end;
run;



ods listing gpath = "&path";
ods graphics / imagename = "Q&q._overlay" imagefmt = png;



/*overlay plot*/

proc sgplot data=one noautolegend;
scatter x=x y=g/name='g' legendlabel="y = &g";
scatter x=x y=h/name='h' legendlabel="y = &b";
scatter x=x y=f/name='f' legendlabel="y = &f";
keylegend 'g' 'h' 'f' /title='Function Key' across=1 down=3;
refline 0/axis=y;
refline 0/axis=x;
refline -1/axis = x lineattrs=(pattern=ShortDash color=black);
refline 1/axis=y lineattrs=(pattern=ShortDash color=red);
refline -1/axis=y lineattrs=(pattern=ShortDash color=blue);
yaxis max= &ymax min= &ymin;
xaxis max= &xmax min = &xmin &valf; 


title "Q&q.: f(x) = &f";
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


ods graphics / imagename = "Q&q._panel" imagefmt = png;


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


title "Q&q.: f(x) = &f";
run;


%mend;

%trig_add()

/*Q1*/

%trig_add(

q = 1,

g = %quote(cos(x)),
h = %quote(3*sin(x)),

ymin = -3, 
ymax = 3,

xform=twopi  
)


/*Q2*/


%trig_add(

q = 2,

g = %quote(sin(x)),
h = %quote(3*cos(x)),

ymin = -3, 
ymax = 3,

xform=twopi  
)


/*Q3*/


%trig_add(

q = 3,

g = %quote(2*cos(x)),
h = %quote(3*sin(x)),

ymin = -4, 
ymax = 4,

xform=twopi  
)


/*Q4*/


%trig_add(

q = 4,

g = %quote(2*sin(x)),
h = %quote(3*cos(x)),

ymin = -4, 
ymax = 4,

xform=twopi  
)


/*Q5*/


%trig_add(

q = 5,

g = %quote(sin(x)),
h = %quote(cos(2*x)),

ymin = -2, 
ymax = 2,

xform=twopi  
)






/*Q6*/


%trig_add(

q = 6,

g = %quote(2*cos(x)),
h = %quote(sin(2*x)),

ymin = -3, 
ymax = 3,

xform=twopi  
)


/*Q7*/


%trig_add(

q = 7,

g = %quote(cos(x)),
h = %quote((-1)*sin(x)),

ymin = -2, 
ymax = 2,

xform=twopi  
)


/*Q8*/

%trig_add(

q = 8,

g = %quote(2*sin(x)),
h = %quote((-1)*cos(x)),

ymin = -3, 
ymax = 3,

xform=twopi  
)


/*Q9*/

%trig_add(

q = 9,

g = %quote(2*cos(x)),
h = %quote((1/2)*sin(2*x)),

ymin = -3, 
ymax = 3,

xform=twopi  
)


/*Q10*/

%trig_add(

q = 10,

g = %quote(2*cos(x)),
h = %quote(cos((1/2)*x)),

ymin = -3, 
ymax = 3,

xform=twopi  
)

/*Q11*/

%trig_add(

q = 11,

g = %quote(1),
h = %quote(sin(x)),

ymin = -3, 
ymax = 3,

xform=twopi  
)

/*Q12*/

%trig_add(

q = 12,

g = %quote(2),
h = %quote((sin(x))/(cos(x))),

ymin = -6, 
ymax = 6,

xform=twopi  
)



/*12a*/


%trig_add(

q =12a,

g = %quote(2),
h = %quote((sin(x))/(cos(x))),

tan =0,
f =%str(&g + &h),
alt = %nrstr(),


ymin = -6, 
ymax = 6,

xform=twopi  
)



/*12b*/



%trig_add(

q =12b,

g = %quote(2),
h = %quote((sin(x))/(cos(x))),

tan =1,
f =%str(&g + &h),
alt = %nrstr(2 + tan(x)),


ymin = -6, 
ymax = 6,

xform=twopi  
)



%trig_add(

q = 12c,

g = %quote(2),
h = %quote((sin(x))/(cos(x))),

tan =0,
b = %str(&h),
f =%str(&g + &h),

altb = %nrstr(),
altf = %nrstr(),



ymin = -6, 
ymax = 6,

xform=twopi  
)


/*12d*/

%trig_add(

q = 12d,

g = %quote(2),
h = %quote((sin(x))/(cos(x))),

tan =1,
b = %str(&h),
f =%str(&g + &h),

altb = %nrstr(tan(x)),
altf = %nrstr(2 + tan(x)),



ymin = -6, 
ymax = 6,

xform=twopi  
)


/*Q13*/


%trig_add(

q = 13,

g = %quote((1/2)*x),
h = %quote(sin(x)),

tan =0,
b = %str(&h),
f =%str(&g + &h),

altb = %nrstr(tan(x)),
altf = %nrstr(2 + tan(x)),



ymin = -6, 
ymax = 6,

xform=sixpi  
)



/*Q14*/


%trig_add(

q = 14,

g = %quote(1),
h = %quote(cos(x)),

tan =0,
b = %str(&h),
f =%str(&g + &h),

altb = %nrstr(tan(x)),
altf = %nrstr(2 + tan(x)),



ymin = -3, 
ymax = 3,

xform=sixpi  
)



/*Q15*/


%trig_add(

q = 15,

g = %quote(2**x),
h = %quote(sin(x)),

tan =0,
b = %str(&h),
f =%str(&g + &h),

altb = %nrstr(tan(x)),
altf = %nrstr(2 + tan(x)),



ymin = -10, 
ymax = 10,

xform=neg6pi
)




/*Q16*/


%trig_add(

q = 16,

g = %quote(-1),
h = %quote(1/(sin(x))),

tan =1,
b = %str(&h),
f =%str(&g + &h),

altb = %nrstr(csc(x)),
altf = %nrstr(-1 + csc(x)),



ymin = -10, 
ymax = 10,

xform=neg6pi
)


/*Q17*/


%trig_add(

q = 17,

g = %quote(2),
h = %quote(1/(cos(x))),

tan =1,
b = %str(&h),
f =%str(&g + &h),

altb = %nrstr(sec(x)),
altf = %nrstr(2 + sec(x)),



ymin = -10, 
ymax = 10,

xform=neg6pi
)



/*Q18*/


%trig_add(

q = 18,

g = %quote(x),
h = %quote((-1)*sin(x)),

tan =0,
b = %str(&h),
f =%str(&g + &h),

altb = %nrstr(sec(x)),
altf = %nrstr(2 + sec(x)),



ymin = -10, 
ymax = 10,

xform=neg6pi
)


/*Q19*/


%trig_add(

q = 19,

g = %quote(-1),
h = %quote(cos(x)),

tan =0,
b = %str(&h),
f =%str(&g + &h),

altb = %nrstr(sec(x)),
altf = %nrstr(2 + sec(x)),



ymin = -10, 
ymax = 10,

xform=neg6pi
)










