/*2. angle, same side -- eg: (alpha, b); (beta, a)*/
/*objective: find (missing angle, missing side, c);*/
/*strategy: */

/*missing angle = 90 - (given angle);*/
/*missing side = (given side) * (sine(given angle in rads)) / (cosine (given angle in rads))*/
/*c = (given side)/(cosine (given angle in rads))*/



%macro ang_sameSide(given_angle, same_side);

%let other_angle = %sysevalf(90-&given_angle);
%deg_to_rad(&given_angle) %*output is quote(ang_rad) macro var;

data solver;
given_angle_rad =&ang_rad;
given_angle =&given_angle;
other_angle =&other_angle;
same_side =&same_side;
other_side =&same_side * (sin(given_angle_rad) / cos(given_angle_rad));
side_c = &same_side  / cos(given_angle_rad);
drop given_angle_rad;
run;


data _null_;
set solver;
if _n_;
call symputx('side_missing',other_side, 'G');
call symputx('angle_missing',other_angle, 'G');
call symputx('side_c',side_c, 'G');
run;

%put missing side is: &side_missing;
%put missing angle is: &angle_missing;
%put "side c" is: &side_c;

%mend ang_sameSide;

/*options nomlogic nomprint nosymbolgen;*/

/*3. beta=37.06, side a=0.4614*/
/*%ang_sameSide(37.06,0.4613)*/
/*4. alpha=17.69, side b = 1.307*/
/*%ang_sameSide(17.69,1.307)*/
