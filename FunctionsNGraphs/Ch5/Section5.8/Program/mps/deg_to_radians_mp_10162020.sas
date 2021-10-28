/*degree to radian macro*/


%macro deg_to_rad(ang_deg);

data _null_;
pi = constant('pi');
ang_rad = &ang_deg*(2*pi)/360;
call symputx('ang_rad',ang_rad, 'G');
run;

/*%put &ang_rad;*/


%mend deg_to_rad;
