figure(1);
title('abc')

subplot(6, 1, 1);
plot(VarName1, VarName2, 'd');
set(gca, 'Xlim', [0 10800]);
set(gca, 'Ylim', [0 5]);
title('random low duration user')

subplot(6, 1, 2);
plot(VarName3, VarName4, 'd');
set(gca, 'Xlim', [0 10800]);
set(gca, 'Ylim', [0 5]);
title('random high duration user')

subplot(6, 1, 3);
plot(VarName5, VarName6, 'd');
set(gca, 'Xlim', [0 10800]);
set(gca, 'Ylim', [0 5]);
title('random low record count user')

subplot(6, 1, 4);
plot(VarName7, VarName8, 'd');
set(gca, 'Xlim', [0 10800]);
set(gca, 'Ylim', [0 5]);
title('random high record count user')

subplot(6, 1, 5);
plot(VarName9, VarName10, 'd');
set(gca, 'Xlim', [0 10800]);
set(gca, 'Ylim', [0 5]);
title('random low traveled towers user')

subplot(6, 1, 6);
plot(VarName11, VarName12, 'd');
set(gca, 'Xlim', [0 10800]);
set(gca, 'Ylim', [0 5]);
title('random high traveled towers user')