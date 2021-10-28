/*radian to degree macro*/


%macro rad_to_deg(ang_rad);

data _null_;
pi = constant('pi');
ang_deg = &ang_rad*360/(2*pi);
call symputx('ang_deg',ang_deg, 'G');
run;

/*%put &ang_deg;*/


%mend rad_to_deg;

