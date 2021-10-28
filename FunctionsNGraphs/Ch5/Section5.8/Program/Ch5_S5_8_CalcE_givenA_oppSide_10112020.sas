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


%macro gang_side_oppgang(gang, side_oppgang);


	%deg_to_rad(&gang)

	data solver;
	gang_rad = &ang_rad;
	gang = &gang;
	oang = 90-gang;
	gamma = &gamma;
	side_oppgang = &side_oppgang;	
	side_adjgang = side_oppgang * (cos(gang_rad) / sin(gang_rad));
	c_trig = side_oppgang / sin(gang_rad);
	c_pyth = ((side_oppgang**2) + (side_adjgnag**2))**(1/2);
	drop gang_rad;

	run;

	%if &gang=



%mend;



%gang_side_oppgang(gang, side_oppgang)
