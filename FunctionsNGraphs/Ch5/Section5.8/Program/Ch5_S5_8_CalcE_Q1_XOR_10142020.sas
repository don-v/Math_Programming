%macro isBlank(param);   
%sysevalf(%superq(param)=,boolean) 
%mend  isBlank; 


/*making a macro to test exclusive or*/

%macro xor(a,b);


%let x=%sysfunc(sum(1-%isBlank(&a),1-%isBlank(&b)));

%if &x ^=1 %then %do; 

%goto error;

%end;

%else %do;

%put &x;

%end;

%error: %put ERROR: only alpha or beta can be supplied, but not both;

%mend xor;


%xor(2,3)
%xor(2,)
%xor(,3)


%macro xor2(alpha=,beta=);


%let x=%sysfunc(sum(1-%isBlank(&alpha),1-%isBlank(&beta)));

%if &x ^=1 %then %do; 

%goto error;

%end;

%else %do;

%put &x;

%end;

%error: %put ERROR: only alpha or beta can be supplied, but not both;

%mend xor2;

%xor2(alpha=90,beta=30)
%xor2(alpha=,beta=)


constraints to model:

1. if an angle is supplied:
	- then the other angle cannot be supplied
	- can be paired with 1 of (a, b)

2. if an angle is not supplied:
	- a will be paired with 1 of (b, c)
	- b will be paried with 1 of (a, c)


%macro RT_check(
alpha=,
beta=,
a=,
b=,
c=
);


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

		%end;

		%else %do;

			%let x=%sysfunc(sum(1-%isBlank(&a),1-%isBlank(&c),1-%isBlank(&alpha),1-%isBlank(&beta))); 
			%if &x ^=1 %then %goto error5;			

		%end;
		

	%end;


%end;


%goto code;

%error: %put ERROR: angle supplied must be less than 90 degrees!; %return;

%error2: %put ERROR: only alpha, or beta can be supplied, but not both!; %return;

%error3: %put ERROR: since an angle is supplied, you may only provide one of (side a, side b)!; %return;

%error4: %put ERROR: since side is supplied, you may only provide one of (side b, side c, angle a, or angle b)!; %return;

%error5: %put ERROR: since side is supplied, you may only provide one of (side a, side c, angle a, or angle b)!; %return;

%code: %put you have assigned arguments to parameters correclty -- well done!;


%mend RT_check;


%RT_check(
alpha=45,
beta=50,
a=,
b=,
c=
)

%RT_check(
alpha=45,
beta=55,
a=,
b=,
c=
)
