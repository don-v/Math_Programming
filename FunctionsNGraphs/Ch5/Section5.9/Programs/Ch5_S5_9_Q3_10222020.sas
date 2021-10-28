%let path = %nrstr(.);
%let q=3;

ods listing gpath = "&path";



data one;
pi = constant('pi');
do t = 0 to (1/3) by (1/512);
d = 10*sin(6*pi*t);
speed = d - lag1(d);
output;
keep t d speed;
end;
run;

proc print data=one; run;

proc means data=one max;
var speed;
run;


ods graphics / imagename = "Q&q._speed" imagefmt = png;

proc sgplot data=one;
scatter x=t y=speed;
title 'Q3: speed graph';
run;

ods graphics / imagename = "Q&q._position" imagefmt = png;

proc sgplot data=one;
scatter x=t y=d;
title 'Q3: position graph';
run;

ods graphics / imagename = "Q&q._pos_spd" imagefmt = png;

proc sgplot data=one;
scatter x=t y=d/name = 'd';
scatter x=t y=speed/y2axis name = 's';
keylegend "d" / title="position" position=bottomleft;
keylegend "s" / title="speed" position=bottomright;
title 'Q3 position and speed';
run;
