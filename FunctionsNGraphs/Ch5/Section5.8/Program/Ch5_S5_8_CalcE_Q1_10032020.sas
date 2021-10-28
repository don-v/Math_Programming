%macro isBlank(param);   
%sysevalf(%superq(param)=,boolean) 
%mend  isBlank; 


%macro isBlank2(param);   
%let x = %sysevalf(%superq(param)=,boolean); 
%put &x;
%mend  isBlank2; 

%let a = 20;

%isBlank2(&a)


%let longMinus3=%sysfunc(repeat(X,65534-1-3)); 

%macro test2;   

%if %isBlank(&longMinus3) and %isBlank(&longMinus3) %then %put both blank;   
%else %put at least either is not blank; 

%mend  test2; 

%test2



%macro check(parm);
   %local status;
   %if &parm= %then %do;
       %put ERROR:  You must supply a parameter to macro CHECK.;
       %goto exit;
   %end;
   more macro statements that test for error conditions 
   %if &status > 0 %then %do;
       %put ERROR:  File is empty.;
       %goto exit;
   %end;
   more macro statements that generate text 
   %put Check completed successfully.;
%exit: %mend check;

%macro info(type);
   %if %upcase(&type)=SHORT %then %goto quick; /* No % here */
      proc contents;
      run;
      proc freq;
         tables _numeric_;
      run;
   %quick: proc print data=_last_(obs=10);     /* Use % here */
      run;
%mend info;
%info(short)


/*parameters:*/

/*alpha*/
/*beta*/
/*gamma*/
/*a*/
/*b*/
/*c*/

/*4. side, hypotenouse  -- eg: (a, c); (b, c)*/
/*3. 2 non-hyp sides -- eg: (a, b); (b, a)*/
/*2. angle, same side -- eg: (alpha, b); (beta, a)*/
/*1. angle, opp side --  eg: (alpha, a); (beta, b)*/


alpha: only paired with a, or b, not both.

beta: only paired with a, or b, not both.

a: paired with exactly ONE of (b, c, alpha, or beta)
b: paired with exactly ONE of (a, c, alpha, or beta)

errors:

if alpha, beta is not numeric and greater than 90
a > c
b > c


%put %datatyp(2);
%put %datatyp(&a);





%macro veeral;

%let a =3;
%if 1-%isBlank(&a) %then %put a is not blank.;

%let b =20;
%let c =30;
%let alpha =95;
%let beta = 30;

%put a: &a;
%put b: &b;
%put c: &c;

%let x = %eval(&a > &c);
%put x: &x;



%if (90 < &alpha | 90 < &beta) %then %goto error_angle;
%if (%eval(&a > &c) | %eval(&b > &c)) %then %goto error_sides;
%if %sysfunc(sum(%isBlank(&b),%isBlank(&c)))>1 %then %goto error;


%error_sides: %put ERROR: %str(a must be less than c; b must be less than c);
%error_angle: %put ERROR: angles must be less than 90 degrees!; 
%error: %put ERROR: can only supply values for EXACTLY two of %str((a, b, c, alpha, beta););

%mend veeral;

options mlogic mprint symbolgen;

%veeral







/*sas trig function accept radians*/

%macro deg_to_rad(ang_deg);

data _null_;
pi = constant('pi');
ang_rad = &ang_deg*(2*pi)/360;
call symputx('ang_rad',ang_rad, 'G');
run;

%put &ang_rad;


%mend;

%deg_to_rad(90);


%macro rad_to_deg(ang_rad);

data _null_;
pi = constant('pi');
ang_deg = &ang_rad*360/(2*pi);
call symputx('ang_deg',ang_deg, 'G');
run;

%put &ang_deg;


%mend;

options mprint mlogic symbolgen;

%deg_to_rad(90)
%rad_to_deg(&ang_rad)


/* right triangle solver*/

/*4 cases*/


/*

terminology:
angle: non right angle
side: non-hypotenuse 

triangle ABC
angles: alpha, beta, gamma
sides: a, b, c

side a opposes alpha; 
side b opposes beta;
side c opposes gamma;

gamma = 90 degrees; 
c always hypotenuse (longest side)


*/

%macro right_tri_solver(
alpha=,
beta=,
gamma=90,
a=,
b=,
c=
)
;


%put 

alpha = &alpha
beta = &beta
gamma = &gamma

a = &a
b = &b
c = &c
;


%put 

length_alpha = %length(&alpha)
length_beta = %length(&beta)
length_gamma = %length(&gamma)

length_a = %length(&a)
length_b = %length(&b)
length_c = %length(&c)

;







/*goal and strategy for each case above:*/
/*find angles, sides based on given info:*/

/*1. angle, opp side --  eg: (alpha, a); (beta, b)*/
/*objective: find (missing angle, missing side, c);*/
/*strategy: */

/*missing angle = 90 - (given angle);*/
/*missing side = (given side) * (cosine (given angle in rads)) / (sine(given angle in rads))*/
/*c = (given side)/(sine(given angle rads))*/


%if %length(&alpha) ^= 0 %then %do;

	%if %length(&a) ^=0 %then %do;
	
	%deg_to_rad(&alpha)

	data solver;
	alpha_rad = &ang_rad;
	alpha = &alpha;
	beta = 90-alpha;
	gamma = &gamma;
	a = &a;	
	b = a * (cos(alpha_rad) / sin(alpha_rad));
	c_trig = a / sin(alpha_rad);
	c_pyth = ((a**2) + (b**2))**(1/2);
	drop alpha_rad;


	run;

	proc print data=solver; run;


	%end;

/*2. angle, same side -- eg: (alpha, b); (beta, a)*/
/*objective: find (missing angle, missing side, c);*/
/*strategy: */

/*missing angle = 90 - (given angle);*/
/*missing side = (given side) * (sine(given angle in rads)) / (cosine (given angle in rads))*/
/*c = (given side)/(cosine (given angle in rads))*/


	%if %length(&b) ^=0 %then %do;

	%deg_to_rad(&alpha)

	data solver;
	alpha_rad = &ang_rad;
	alpha = &alpha;
	beta = 90-alpha;
	gamma = &gamma;
	a = &b * (sin(alpha_rad) / cos(alpha_rad));
	b = &b;
	c_trig = &b / cos(alpha_rad);
	c_pyth = ((a**2) + (b**2))**(1/2);
	drop alpha_rad;


	run;

	proc print data=solver; run;

	%end;

%end;



/*3. 2 non-hyp sides -- eg: (a, b); (b, a)*/
/*ATAN(arg), ATAN2(arg1/arg2)*/
/*objective: (find angles, c)*/
/*strategy: */

/*alpha = %rad_to_deg(ATAN2(a, b));*/
/*beta = %rad_to_deg(ATAN2(b, a));*/

/*c = ((a**2) + (b**2))**(1/2)*/




%if %length(&a) ^=0 %then %do;

	%if %length(&b) ^=0 %then %do;

	%let alpha_rad = %sysfunc(ATAN2(&a., &b));
	%let beta_rad = %sysfunc(ATAN2(&b., &a));
	%rad_to_deg(&alpha_rad)
	%let alpha_deg = &ang_deg;

	%rad_to_deg(&beta_rad)
	%let beta_deg = &ang_deg;

	data solver;
	alpha = &alpha_deg;
	beta = &beta_deg;
	gamma = &gamma;
	a = &a;
	b = &b;
	c = ((a**2) + (b**2))**(1/2);
	run;

	proc print data=solver; run;
	
	

	%end;

/*4. side, hypotenouse  -- eg: (a, c); (b, c)*/
/*arsin(arg); arcos(arg);*/
/*given(a, c):*/
/*alpha = %rad_to_deg(arsin(a/c));*/
/*beta = %rad_to_deg(arcos(a/c));*/
/*b = ((c**2) - (a**2))**(1/2);*/

/*given(b, c):*/
/*alpha = %rad_to_deg(arcos(b/c));*/
/*beta = %rad_to_deg(arsin(b/c));*/
/*a = ((c**2) - (b**2))**(1/2);*/

%end;

%if %length(&c) ^=0 %then %do;

	%if %length(&a) ^=0 %then %do;


	%let alpha_rad = %sysfunc(ARSIN(&a./&c));
	%let beta_rad = %sysfunc(ARCOS(&a./&c));
	%rad_to_deg(&alpha_rad)
	%let alpha_deg = &ang_deg;

	%rad_to_deg(&beta_rad)
	%let beta_deg = &ang_deg;

	data solver;
	alpha = &alpha_deg;
	beta = &beta_deg;
	gamma = &gamma;
	a = &a;
	b = ((&c**2) - (a**2))**(1/2);
	c = &c;
	run;

	proc print data=solver; run;
	
	%end;


/*given(b, c):*/
/*alpha = %rad_to_deg(arcos(b/c));*/
/*beta = %rad_to_deg(arsin(b/c));*/
/*a = ((c**2) - (b**2))**(1/2);*/



	%if %length(&b) ^=0 %then %do;


	%let alpha_rad = %sysfunc(ARSIN(&b./&c));
	%let beta_rad = %sysfunc(ARCOS(&b./&c));
	%rad_to_deg(&alpha_rad)
	%let alpha_deg = &ang_deg;

	%rad_to_deg(&beta_rad)
	%let beta_deg = &ang_deg;

	data solver;
	alpha = &alpha_deg;
	beta = &beta_deg;
	gamma = &gamma;
	a = &a;
	b = ((&c**2) - (b**2))**(1/2);
	c = &c;
	run;

	proc print data=solver; run;
	
	%end;

%end;















%mend;

%right_tri_solver(
alpha=20,
beta=,
gamma=90,
a=3,
b=,
c=
)


%right_tri_solver(
alpha=30,
beta=,
gamma=90,
a=,
b=4,
c=
)


%right_tri_solver(
alpha=,
beta=,
gamma=90,
a=1,
b=1,
c=
)


%right_tri_solver(
alpha=,
beta=,
gamma=90,
a=3,
b=,
c=5
)



/*1: alpha = 41.27; a = 314.6*/


%right_tri_solver(
alpha=41.27,
beta=,
gamma=90,
a=314.6,
b=,
c=
)


/*2: beta = 24.96; beta = 209.3*/


%right_tri_solver(
alpha=,
beta=24.96,
gamma=90,
a=,
b=209.3,
c=
)









