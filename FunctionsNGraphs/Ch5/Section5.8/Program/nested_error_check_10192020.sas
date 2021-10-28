/*checking error in one macro to stop another!*/

%macro isBlank(param);   
%sysevalf(%superq(param)=,boolean) 
%mend  isBlank; 


%macro child_error(a=);

%global _error;

/*%let _error=0;*/

%if %isBlank(&a) %then %do;
	%let _error=1;
	%goto missing_param;
%end;

%goto code;

%missing_param: %put ERROR: please provide an argument for parameter 'a'; %return;

%code: %put OK you are all set -- please proceed!;

%mend child_error;





%macro parent_error(j);

%child_error(a=&j);

%if &_error %then %do;
	%put ERROR: execution will stop because parameter 'a' is missing;
	%return;
%end; 

%else %do;
	%put executing parent code!;
%end; 

%mend parent_error;


%parent_error()
%parent_error(2)
