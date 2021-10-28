/*make sure the current directory is set to the directory that contains this file and the directory 'mps'!*/
filename dep '.\mps';
%inc dep(rt_param_check_mp_10162020, deg_to_radians_mp_10162020, rad_to_degrees_mp_10162020, _ang_oppside_10162020, _ang_sameside_10162020, _sides_ab_ba_10162020, _sides_ac_bc_10162020);

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


/*alpha: only paired with a, or b, not both.*/
/**/
/*beta: only paired with a, or b, not both.*/
/**/
/*a: paired with exactly ONE of (b, c, alpha, or beta)*/
/*b: paired with exactly ONE of (a, c, alpha, or beta)*/
/**/
/*errors:*/
/**/
/*if alpha, beta is not numeric and greater than 90*/
/*a > c*/
/*b > c*/


/*sas trig function accept radians*/


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




%RT_check(
alpha=&alpha,
beta=&beta,
a=&a,
b=&b,
c=&c
)


%if &_error %then %do;

%return;

%end;


/*goal and strategy for each case above:*/
/*find angles, sides based on given info:*/

/*1. angle, opp side --  eg: (alpha, a); (beta, b)*/
/*objective: find (missing angle, missing side, c);*/
/*strategy: */

/*missing angle = 90 - (given angle);*/
/*missing side = (given side) * (cosine (given angle in rads)) / (sine(given angle in rads))*/
/*c = (given side)/(sine(given angle rads))*/



%if 1-%isBlank(&alpha) & 1-%isBlank(&a) %then %do;
		
	%ang_oppSide(&alpha, &a)	

%end;

%if 1-%isBlank(&beta) & 1-%isBlank(&b) %then %do;
		
	%ang_oppSide(&beta, &b)	

%end;







/*2. angle, same side -- eg: (alpha, b); (beta, a)*/
/*objective: find (missing angle, missing side, c);*/
/*strategy: */

/*missing angle = 90 - (given angle);*/
/*missing side = (given side) * (sine(given angle in rads)) / (cosine (given angle in rads))*/
/*c = (given side)/(cosine (given angle in rads))*/




%if 1-%isBlank(&alpha) & 1-%isBlank(&b) %then %do;
		
	%ang_sameSide(&alpha, &b)	

%end;

%if 1-%isBlank(&beta) & 1-%isBlank(&a) %then %do;
		
	%ang_sameSide(&beta, &a)	

%end;









/*3. 2 non-hyp sides -- eg: (a, b); (b, a)*/
/*ATAN(arg), ATAN2(arg1/arg2)*/
/*objective: (find angles, c)*/
/*strategy: */

/*alpha = %rad_to_deg(ATAN2(a, b));*/
/*beta = %rad_to_deg(ATAN2(b, a));*/

/*c = ((a**2) + (b**2))**(1/2)*/


%if 1-%isBlank(&a) & 1-%isBlank(&b) %then %do;
		
	%sides_ab(&a,&b)

%end;



/*4. side, hypotenouse  -- eg: (a, c); (b, c)*/
/*arsin(arg); arcos(arg);*/
/*given(a, c):*/
/*alpha = %rad_to_deg(arsin(a/c));*/
/*beta = %rad_to_deg(arcos(a/c));*/
/*b = ((c**2) - (a**2))**(1/2);*/


%if 1-%isBlank(&a) & 1-%isBlank(&c) %then %do;
		
	%sides_ac(&a,&c)

%end;


/*given(b, c):*/
/*alpha = %rad_to_deg(arcos(b/c));*/
/*beta = %rad_to_deg(arsin(b/c));*/
/*a = ((c**2) - (b**2))**(1/2);*/



%if 1-%isBlank(&b) & 1-%isBlank(&c) %then %do;
		
	%sides_bc(&b,&c)

%end;







%mend right_tri_solver;

%right_tri_solver(
alpha=,
beta=45,
gamma=90,
a=0.4613,
b=,
c=
)
