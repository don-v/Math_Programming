data one;
u=1.46;
v=8.27;
sin_add=sin(u+v);
sin_expand=(sin(u)*cos(v))+(cos(u)*sin(v));

cos_add=cos(u+v);
cos_expand=(cos(u)*cos(v))-(sin(u)*sin(v));

tan_add=tan(u+v);
tan_expand=(tan(u)+tan(v))/(1-(tan(u)*tan(v)));
run;

proc print data=one; run;


data two;
pi=constant('pi');
cosu = -0.4163;
sinv = 0.7216;

u = arcos(cosu);
v = arsin(sinv);

u_deg=(u*180)/pi;
v_deg=(v*180)/pi;


sin_expand=(sin(u)*cos(v))+(cos(u)*sin(v));
cos_expand=(cos(u)*cos(v))-(sin(u)*sin(v));

run;

proc print data=two;run;
