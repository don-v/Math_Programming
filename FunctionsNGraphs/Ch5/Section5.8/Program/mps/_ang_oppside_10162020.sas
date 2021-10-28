/*1. angle, opp side --  eg: (alpha, a); (beta, b)*/
/*objective: find (missing angle, missing side, c);*/
/*strategy: */

/*missing angle = 90 - (given angle);*/
/*missing side = (given side) * (cosine (given angle in rads)) / (sine(given angle in rads))*/
/*c = (given side)/(sine(given angle rads))*/




%macro ang_oppSide(given_angle, opposite_side);

%let other_angle = %sysevalf(90-&given_angle);
%deg_to_rad(&given_angle) %*output is quote(ang_rad) macro var;

data solver;
given_angle_rad =&ang_rad;
given_angle =&given_angle;
other_angle =&other_angle;
opposite_side =&opposite_side;
other_side =&opposite_side * (cos(given_angle_rad) / sin(given_angle_rad));
side_c = &opposite_side  / sin(given_angle_rad);
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

%mend ang_oppSide;

/*options nomlogic nomprint nosymbolgen;*/

/*1. alpha=41.27, side a=314.6*/
/*%ang_oppSide(41.27,314.6)*/
/*2. beta=24.96, side b=209.3*/
/*%ang_oppSide(24.96,209.3)*/
/*5. beta=2.71, side b=7149*/
/*%ang_oppSide(2.71,7149)*/
/*6. alpha=84.07, side a=0.1024*/
/*%ang_oppSide(84.07, 0.1024)*/



