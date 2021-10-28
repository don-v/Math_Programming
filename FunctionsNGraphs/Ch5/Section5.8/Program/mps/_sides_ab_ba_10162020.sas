/*3. 2 non-hyp sides -- eg: (a, b); (b, a)*/
/*ATAN(arg), ATAN2(arg1/arg2)*/
/*objective: (find angles, c)*/
/*strategy: */

/*alpha = %rad_to_deg(ATAN2(a, b));*/
/*beta = %rad_to_deg(ATAN2(b, a));*/

/*c = ((a**2) + (b**2))**(1/2)*/

%macro sides_ab(side_a, side_b);

%let alpha_rad = %sysfunc(ATAN2(&side_a., &side_b));
%let beta_rad = %sysfunc(ATAN2(&side_b., &side_a));
%rad_to_deg(&alpha_rad) %*output is quote(ang_deg) macro var;
%let alpha_deg = &ang_deg;

%rad_to_deg(&beta_rad) %*output is quote(ang_deg) macro var;
%let beta_deg = &ang_deg;



data solver;
ang_alpha = &alpha_deg;
ang_beta = &beta_deg;

side_a=&side_a;
side_b=&side_b;
side_c=((side_a**2) + (side_b**2))**(1/2); 
run;


data _null_;
set solver;
if _n_;
call symputx('angle_alpha',ang_alpha, 'G');
call symputx('angle_beta',ang_beta, 'G');
call symputx('side_c',side_c, 'G');
run;

%put angle alpha is: &angle_alpha;
%put angle beta is: &angle_beta;
%put "side c" is: &side_c;

%mend sides_ab;


/*7. a=46.87, b=13.12*/
/*%sides_ab(46.87, 13.12)*/
/*8. a=6.948, b=8.371*/
/*%sides_ab(6.948, 8.371)*/



