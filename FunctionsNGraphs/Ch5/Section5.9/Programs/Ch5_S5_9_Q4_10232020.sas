%let path = %nrstr(.);
%let q=4;

ods listing gpath = "&path";



data one;
pi = constant('pi');
do t = 0 to (8) by (1/256);
d = (1/3)*cos((pi/4)*t);
speed = d - lag1(d);
output;
keep d t speed;
end;
run;

proc print data=one; run;

proc means data=one max;
var speed;
run;


data two;
pi = constant('pi');
do t = 0 to (8) by (1/2);
d = (1/3)*cos((pi/4)*t);
speed = d - lag1(d);
output;
keep d t speed;
end;
run;

proc print data=two;
run;



ods graphics / imagename = "Q&q._speed" imagefmt = png;

proc sgplot data=one;
scatter x=t y=speed;
title 'Q4: speed graph';
run;

ods graphics / imagename = "Q&q._position" imagefmt = png;

proc sgplot data=one;
scatter x=t y=d;
title 'Q4: position graph';
run;

ods graphics / imagename = "Q&q._pos_spd" imagefmt = png;

proc sgplot data=one;
scatter x=t y=d/name = 'd';
scatter x=t y=speed/y2axis name = 's';
keylegend "d" / title="position" position=bottomleft;
keylegend "s" / title="speed" position=bottomright;
title 'Q4 position and speed';
run;
