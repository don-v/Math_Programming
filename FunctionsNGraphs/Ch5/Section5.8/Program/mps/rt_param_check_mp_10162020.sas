/*right triangle solver parameter checker macro*/

%macro isBlank(param);   
%sysevalf(%superq(param)=,boolean) 
%mend  isBlank; 


/*constraints to model:*/
/**/
/*1. if an angle is supplied:*/
/*	- then the other angle cannot be supplied*/
/*	- can be paired with 1 of (a, b)*/
/**/
/*2. if an angle is not supplied:*/
/*	- a will be paired with 1 of (b, c)*/
/*	- b will be paried with 1 of (a, c)*/

/*if alpha and beta IS blank:*/
/**/
/*then exactly 2 of ( a, b, c ) must NOT be blank.*/



%macro RT_check(
alpha=,
beta=,
a=,
b=,
c=
);

%global _error;


%if %isBlank(&alpha) & %isBlank(&beta) %then %do;
	%let x=%sysfunc(sum(1-%isBlank(&a),1-%isBlank(&b),1-%isBlank(&c))); 
	%if &x ^=2 %then %goto error9;	
%end;


%if 1-%isBlank(&alpha) | 1-%isBlank(&beta) %then %do;


	%if (90 <= &alpha | 90 <= &beta) %then %goto error;

	%let x=%sysfunc(sum(1-%isBlank(&alpha),1-%isBlank(&beta))); 
	%if &x ^=1 %then %goto error2;

	%let y=%sysfunc(sum(1-%isBlank(&a),1-%isBlank(&b))); 
	%if &y ^=1 %then %goto error3;



%end; %else %do;

	%if 1-%isBlank(&a) | 1-%isBlank(&b) %then %do;

		%if 1-%isBlank(&a) %then %do;

			%let x=%sysfunc(sum(1-%isBlank(&b),1-%isBlank(&c),1-%isBlank(&alpha),1-%isBlank(&beta))); 
			%if &x ^=1 %then %goto error4;	

			%if 1-%isBlank(&c) %then %do;
				%let x=%sysevalf(&a < &c, boolean);
				%if &x ^=1 %then %goto error5;
			%end;	

		%end;

		%else %do;

			%let x=%sysfunc(sum(1-%isBlank(&a),1-%isBlank(&c),1-%isBlank(&alpha),1-%isBlank(&beta))); 
			%if &x ^=1 %then %goto error5;			

			%if 1-%isBlank(&c) %then %do;
				%let x=%sysevalf(&b < &c, boolean);
				%if &x ^=1 %then %goto error7;
			%end;	

		%end;		
		

	%end;

	%if 1-%isBlank(&c) %then %do;
		%let y=%sysfunc(sum(1-%isBlank(&a),1-%isBlank(&b))); 
		%if &y ^=1 %then %goto error8;
	%end;


%end;


%goto code;

%error: %put ERROR: angle supplied must be less than 90 degrees!; %let _error=1; %return;

%error2: %put ERROR: only alpha, or beta can be supplied, but not both!; %let _error=1; %return;

%error3: %put ERROR: since an angle is supplied, you must provide one and only one of (side a, side b)!; %let _error=1; %return;

%error4: %put ERROR: since "side a" is supplied, you must provide one and only one of  (side b, side c, angle a, or angle b)!; %let _error=1; %return;

%error5: %put ERROR: "side a" must be less than "side c"; %let _error=1; %return;

%error6: %put ERROR: since "side b" is supplied, you must provide one and only one of  (side a, side c, angle a, or angle b)!; %let _error=1; %return;

%error7: %put ERROR: "side b" must be less than "side c"; %let _error=1; %return;

%error8: %put ERROR: since "side c" is supplied, you must provide one and only one of (side a, side b)!; %let _error=1; %return;

%error9: %put ERROR: if "angle a" or "angle b" is NOT supplied, please select and input EXACTlY 2 of ("side a", "side b", or "side c") 
without replacement; %let _error=1; %return;

%code: %put THANK YOU: you have assigned arguments to macro parameters correclty -- well done!; %let _error=0;


%mend RT_check;
