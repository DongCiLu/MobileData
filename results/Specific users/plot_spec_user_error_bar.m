x = VarName1';
y = VarName2';
mid = (x + y) / 2;
e = (y - x) / 2;
perm = sin([1:size(mid, 2)]/10*pi);
errorbar(perm,mid,e,'.');
title('random high traveled towers user (sort by start time)');
xlabel('not used, just to separate user');
ylabel('time (s)');
set(gca, 'Ylim', [0 10800]);
yt=get(gca,'ytick');
ytl=strread(...
          sprintf('%5.0f\n',yt),'%s',...
         'delimiter','');
set(gca,'yticklabel',ytl);
set(gca,'CameraUpVector',[1,0,0],'YDir','reverse','XAxisLocation','top');
set(gca,'fontsize',24)

%plot(VarName1, VarName2, 'd');
% set(gca, 'Xlim', [0 10800]);
% set(gca, 'Ylim', [0 5]);
%title('random low duration user')
% 
% plot(VarName3, VarName4, 'd');
% set(gca, 'Xlim', [0 10800]);
% set(gca, 'Ylim', [0 5]);
% title('random high duration user')
% 
% plot(VarName5, VarName6, 'd');
% set(gca, 'Xlim', [0 10800]);
% set(gca, 'Ylim', [0 5]);
% title('random low record count user')
% 
% plot(VarName7, VarName8, 'd');
% set(gca, 'Xlim', [0 10800]);
% set(gca, 'Ylim', [0 5]);
% title('random high record count user')
% 
% plot(VarName9, VarName10, 'd');
% set(gca, 'Xlim', [0 10800]);
% set(gca, 'Ylim', [0 5]);
% title('random low traveled towers user')
% 
% plot(VarName11, VarName12, 'd');
% set(gca, 'Xlim', [0 10800]);
% set(gca, 'Ylim', [0 5]);
% title('random high traveled towers user')