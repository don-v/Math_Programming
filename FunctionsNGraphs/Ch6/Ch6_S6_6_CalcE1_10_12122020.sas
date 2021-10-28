
/*1-6 Approximate the solutions of the equations*/
/*in exercises  55-60 to four decimal places*/

/*1*/

data d55;
a=-9;
b=57**(1/2);
c=4;
d1 = (a+b)/c;
d2 = (a-b)/c;

t1 = atan(d1);
t2 = atan(d2);
run;
proc print data=d55(keep = t1 t2);
run;

/*2*/

proc format;
value undef
. = 'undefined';
run;

data d56;
length
x a b c d1 d2 truth 8
t1 t2 $ 20;
x = .;
a=7;
b=13**(1/2);
c=6;
d1 = (a+b)/c;
d2 = (a-b)/c;
truth = (d1 LE 1 & d1 GE -1);
if d1 LE 1 & d1 GE -1 then t1 = put(arsin(d1),6.4); else t1 = put(x, undef.);
if d2 LE 1 & d2 GE -1 then t2 = put(arsin(d2),6.4); else t2 = 'undefined';
run;
proc print data=d56
/*(*/
/*keep = t1 t2*/
/*)*/
;
run;

/*3*/

data d57;
length
x 
/*a*/
/*b*/
/*c */
d1 d2 truth 8
t1a t1b t2a t2b $ 20;
x = .;
/*a=7;*/
/*b=13**(1/2);*/
/*c=6;*/
d1 = ((3)**(1/2))/3;
d2 = ((15)**(1/2))/5;
truth = (d1 LE 1 & d1 GE -1);
if d1 LE 1 & d1 GE -1 then t1a = put(arcos(d1),6.4); else t1a = put(x, undef.);
if -d1 LE 1 & -d1 GE -1 then t1b = put(arcos(-d1),6.4); else t1b = put(x, undef.);

if d2 LE 1 & d2 GE -1 then t2a = put(arcos(d2),6.4); else t2a = 'undefined';
if -d2 LE 1 & -d2 GE -1 then t2b = put(arcos(-d2),6.4); else t2b = 'undefined';
run;
proc print data=d57
/*(*/
/*keep = t1 t2*/
/*)*/
;
run;


/*4*/

data d58;
a=19;
b=337**(1/2);
c=6;
d1 = ((a+b)/c)**1/2;
d2 = ((a-b)/c)**1/2;

t1a = put(atan(d1),8.4);
t1b = put(atan(-d1),8.4);
t2a = put(atan(d2),8.4);
t2b = put(atan(-d2),8.4);
run;
proc print data=d58;
run;


/*5*/


data d59;
length
x a b c d1 d2 truth 8
t1 t2 $ 20;
x = .;
a=0;
b=30**(1/2);
c=6;
d1 = (a+b)/c;
d2 = -d1;
truth = (d1 LE 1 & d1 GE -1);
if d1 LE 1 & d1 GE -1 then t1 = put(arsin(d1),8.4); else t1 = put(x, undef.);
if d2 LE 1 & d2 GE -1 then t2 = put(arsin(d2),8.4); else t2 = 'undefined';
run;
proc print data=d59
/*(*/
/*keep = t1 t2*/
/*)*/
;
run;


/*6*/


data d60;
length
x a b c d1 d2 truth 8
t1 t2 $ 20;
x = .;
a=2;
b=3;
c=4;
d1 = b/c;
d2 = a/b;
truth = (d1 LE 1 & d1 GE -1);
if d1 LE 1 & d1 GE -1 then t1 = put(arcos(d1),8.4); else t1 = put(x, undef.);
if d2 LE 1 & d2 GE -1 then t2 = put(arsin(d2),8.4); else t2 = 'undefined';
run;
proc print data=d60
/*(*/
/*keep = t1 t2*/
/*)*/
;
run;



/*7. Show by calculations, that sin(arcsin x) = x for*/
/*the following values of x:*/
/**/
/*a. 0.4631*/
/*b. log(3.64)*/
/*c. 1/((22/7)**(1/2))*/



data d7;
x1 = 0.4631 ;
x2 = log10(3.64) ;
x3 = 1/((22/7)**(1/2));
array x {3} x1-x3;
do i = 1 to dim(x);
	arcsin = arsin(x(i));
	sin = sin(arcsin);
	yes = (sin=x(i)); output;
end;

proc print data=d7;
run;



/*8. Show that arctan(tan (x)) = x for the following*/
/*values of x:*/
/**/
/*a. 74.85*/
/*b. log(((22/7)**2)+ 94.7)*/
/*c. 10**(6.39)*/



data d8;
x1 = 74.85;
x2 = log(((22/7)**2)+ 94.7) ;
x3 = 10**(6.39);
array x {3} x1-x3;
do i = 1 to dim(x);
	arctan = atan(x(i));
	tan = tan(arctan);
	yes = (tan=x(i)); output;
end;

proc print data=d8;
run;



/*9. Exercises 9 and 10 employ the notation introduced*/
/*in the Calculator Exercises of Section 5.5. Use a */
/*calculator to suppor the given statements by */
/*substituting the following values for t:*/
/*0.1, 0.01, 0.001, 0.0001.*/
/**/
/*9. (arcsin(2x))/(arcsin(x)) --> 2 as x --> 0+*/
/**/


data d9;
do x = 0.1, 0.01, 0.001, 0.0001;
asin2x = arsin(2*x);
asinx = arsin(x);
ratio = asin2x/asinx;
output;
end;
run;

proc print data=d9;
run;

/*10. (csc(x))/(arctan(x)) --> 1 as x --> 0+*/


data d10;
do x = 0.1, 0.01, 0.001, 0.0001;
cscx = 1/(sin(x));
arctanx = atan(x);
product = cscx*arctanx;
output;
end;
run;

proc print data=d10;
run;
