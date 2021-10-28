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



%macro sides_ac(side_a,side_c);

%let alpha_rad = %sysfunc(ARSIN(&side_a./&side_c));
%let beta_rad = %sysfunc(ARCOS(&side_a./&side_c));

%rad_to_deg(&alpha_rad) %*output is quote(ang_deg) macro var;
%let alpha_deg = &ang_deg;

%rad_to_deg(&beta_rad) %*output is quote(ang_deg) macro var;
%let beta_deg = &ang_deg;



data solver;
ang_alpha = &alpha_deg;
ang_beta = &beta_deg;

side_a=&side_a;
side_b=((&side_c**2) - (&side_a**2))**(1/2);
side_c=&side_c;
run;


data _null_;
set solver;
if _n_;
call symputx('angle_alpha',ang_alpha, 'G');
call symputx('angle_beta',ang_beta, 'G');
call symputx('side_b',side_b, 'G');
run;

%put angle alpha is: &angle_alpha;
%put angle beta is: &angle_beta;
%put "side b" is: &side_b;

%mend sides_ac;

/*10. a=88.12, c=94.06*/
/*%sides_ac(88.12,94.06)*/
/*%sides_ac(3,5)*/


%macro sides_bc(side_b,side_c);

%let alpha_rad = %sysfunc(ARCOS(&side_b./&side_c));
%let beta_rad = %sysfunc(ARSIN(&side_b./&side_c));

%rad_to_deg(&alpha_rad) %*output is quote(ang_deg) macro var;
%let alpha_deg = &ang_deg;

%rad_to_deg(&beta_rad) %*output is quote(ang_deg) macro var;
%let beta_deg = &ang_deg;



data solver;
ang_alpha = &alpha_deg;
ang_beta = &beta_deg;

side_a=((&side_c**2) - (&side_b**2))**(1/2);
side_b=&side_b;
side_c=&side_c;
run;


data _null_;
set solver;
if _n_;
call symputx('angle_alpha',ang_alpha, 'G');
call symputx('angle_beta',ang_beta, 'G');
call symputx('side_a',side_a, 'G');
run;

%put angle alpha is: &angle_alpha;
%put angle beta is: &angle_beta;
%put "side a" is: &side_a;

%mend sides_bc;

/*%sides_bc(2462,5074);*/
/*%sides_bc(4,5)*/


