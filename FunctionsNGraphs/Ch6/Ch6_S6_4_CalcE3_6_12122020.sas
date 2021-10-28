data q3;
x = 3.624;
two_x = 2*x;
sin_2x = sin(two_x);
sin_2x_expand = 2*sin(x)*cos(x);
equal = (sin_2x = sin_2x_expand);
run;

proc print data=q3;
run;

data q4;
pi = constant('PI');
e = constant('E');
exp1 = exp(1);
x = ((2*pi)**(1/2)) + (e**(7**(1/2)));
x1 = ((2*pi)**(1/2)) + (exp(7**(1/2)));
two_x = 2*x;
cos_2x = cos(two_x);
cos_2x_expand = ((cos(x))**2) - ((sin(x))**2);
equal = (cos_2x = cos_2x_expand);
run;

proc print data=q4; run;

data q5;
x = log(13.5)**5;
two_x = 2*x;
tan_2x = tan(two_x);
tan_2x_expand = (2*tan(x))/(1-((tan(x))**2));
equal = (tan_2x = tan_2x_expand);
run;

proc print data=q5; run;

data q6;
x = tan(0.1634);
xover2 = x/2;
absinxover2 = abs(sin(xover2));
abs_sinxover2_expand = ((1-cos(x))/2)**(1/2);
run;

proc print data=q6;
run;
