
C = zeros(1000,11);

A = zeros(500,11);
B = zeros(500,11);

A(:,1) = 1;
B(:,1) = 0;

A(:,2) = random('Normal',0,1,500,1);
B(:,2) = random('Normal',.5,1,500,1);


A(:,3) = random('Normal',10,3,500,1);
B(:,3) = random('Normal',8,4,500,1);

A(:,4) = random('Normal',-5,3,500,1);
B(:,4) = random('Normal',-4,3,500,1);

A(:,5) = random('Poisson',6,500,1);
B(:,5) = random('Poisson',7,500,1);

A(:,6) = random('Poisson',12,500,1);
B(:,6) = random('Poisson',10,500,1);

A(:,7) = random('Poisson',30,500,1);
B(:,7) = random('Poisson',35,500,1);

A(:,7) = random('exp',13,500,1);
B(:,7) = random('exp',11,500,1);

A(:,8) = random('Poisson',30,500,1);
B(:,8) = random('Poisson',35,500,1);

A(:,9) = random('beta',1,8,500,1);
B(:,9) = random('beta',3,.5,500,1);

A(:,10) = random('Poisson',17,500,1);
B(:,10) = random('Poisson',18,500,1);

A(:,11) = random('bino',17,.5,500,1);
B(:,11) = random('bino',18,.4,500,1);

C = [ A; B];

csvwrite('thousandtoytest.csv', C)
