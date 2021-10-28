%let path = %nrstr(.);
%let q=10;

ods listing gpath = "&path";



data one;
pi = constant('pi');

omega=120*pi;
phi=pi/3;
big_e=110;
amp_e=abs(big_e);
period=(2*pi)/omega;
frequency=omega/(2*pi);
lag_lead=phi/omega;

do t = 0 to period by (1/(720*10));
x=omega*t;
x_less_phi=x-phi;
sin_x=sin(x);
sin_x_less_phi=sin(x_less_phi);
e=big_e*sin(omega*t);
i=15*sin((omega*t)-phi);
i_nophi=15*sin(omega*t);
i_lag=15*sin((omega*t)-lag_lead);
i_lead=15*sin((omega*t)+lag_lead);
output;
end;

run;

proc print data=one; run;


ods graphics / imagename = "Q&q._emf_current" imagefmt = png;

proc sgplot data=one;
scatter x=t y=e/name = 'e' legendlabel='emf';
scatter x=t y=i/name = 'i' legendlabel='i';
scatter x=t y=i_lag/name = 'i-phi' legendlabel='i-phi';
scatter x=t y=i_lead/name = 'i+phi' legendlabel='i+phi';
keylegend 'e' 'i' 'i-phi' 'i+phi'/ down=4;
title 'Q10 EMF and current';
run;

ods graphics / imagename = "Q&q._current_only" imagefmt = png;

proc sgplot data=one;
scatter x=t y=i_nophi/name = 'e' legendlabel='i-nophi';
scatter x=t y=i/name = 'i' legendlabel='i';
scatter x=t y=i_lag/name = 'i-phi' legendlabel='i-phi';
scatter x=t y=i_lead/name = 'i+phi' legendlabel='i+phi';
keylegend 'e' 'i' 'i-phi' 'i+phi'/ down=4;
title 'Q10 just current';
run;


ods graphics / imagename = "Q&q._current_only_zoom" imagefmt = png;

proc sgplot data=one;
scatter x=t y=i_nophi/name = 'e' legendlabel='i-nophi';
scatter x=t y=i/name = 'i' legendlabel='i';
scatter x=t y=i_lag/name = 'i-phi' legendlabel='i-phi';
scatter x=t y=i_lead/name = 'i+phi' legendlabel='i+phi';
keylegend 'i' 'e' 'i-phi' 'i+phi'/ down=4;
title 'Q10 just current';
xaxis values=(.0014 to .0018 by .00001);
yaxis values=(0 to 20 by 1);
run;











