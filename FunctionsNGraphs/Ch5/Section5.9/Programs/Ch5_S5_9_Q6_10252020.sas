%let path = %nrstr(.);
%let q=6;

ods listing gpath = "&path";



data one;
pi = constant('pi');
a = 6;
omega = (2/3)*pi;
amplitude = abs(a);
period = (2*pi)/omega;
frequency = omega/(2*pi);
do t = 0 to period by (1/256);
d = amplitude*sin(omega*t);
speed = d - lag1(d);
output;
/*keep d t speed;*/
end;
run;

proc print data=one; run;

proc means data=one max;
var speed;
run;


data two;
pi = constant('pi');
a = 6;
omega = (2/3)*pi;
amplitude = abs(a);
period = (2*pi)/omega;
frequency = omega/(2*pi);
do t = 0 to period by (1/16);
d = amplitude*sin(omega*t);
speed = d - lag1(d);
output;
/*keep d t speed;*/
end;
run;

proc print data=two;
run;



ods graphics / imagename = "Q&q._speed" imagefmt = png;

proc sgplot data=one;
scatter x=t y=speed;
title 'Q6: speed graph';
run;

ods graphics / imagename = "Q&q._position" imagefmt = png;

proc sgplot data=one;
scatter x=t y=d;
title 'Q6: position graph';
run;

ods graphics / imagename = "Q&q._pos_spd" imagefmt = png;

proc sgplot data=one;
scatter x=t y=d/name = 'd';
scatter x=t y=speed/y2axis name = 's';
keylegend "d" / title="position" position=bottomleft;
keylegend "s" / title="speed" position=bottomright;
title 'Q6 position and speed';
run;
