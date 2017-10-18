n = 19;
c = 4;
r = floor(n/c)+1;
title_string = {'Instant message' ...
    'Reading' ...
    'Microblog' ...
    'Navigation' ...
    'Video' ...        
    'Music' ...
    'App market' ...
    'Game' ...
    'Online payment' ...
    'Comic' ...
    'Email' ...
    'P2P' ...
    'VOIP' ...
    'Multimedia message' ...
    'Browser & Download' ...
    'Finance' ...
    'Security' ...
    'Other1' ...
    'Other2'};

figure(1);
for i = 1:n
    subplot(r, c, i);
    scatter(corrawspeed(i,:), corrawvol(i,:), 1);
    set(gca, 'Xlim', [1 110]);
    set(gca, 'YScale', 'log');
    title(title_string(i))
end

figure(2); 
for i = 1:n
    column = 5;
    subplot(r, c, i);
    plot(bsxfun(@rdivide, cordist(i,1:column), mean(cordist(i,1:column), 2))); 
    set(gca, 'Xlim', [1 column]);
    set(gca, 'XTickLabel', [20 40 60 80 100]);
	set(gca, 'Ylim', [0 2]);
    title(title_string(i))
end

figure(3); 
for i = 1:n
    column = 5;
    subplot(r, c, i);
    plot(bsxfun(@rdivide, cordist(i,1:column), sum(cordist(:,1:column), 1)));
    set(gca, 'Xlim', [1 column]);
    set(gca, 'XTickLabel', [20 40 60 80 100]);
    title(title_string(i))
end

figure(4); 
for i = 1:n
    column = 5;
    subplot(r, c, i);
    plot(bsxfun(@rdivide, cordistxuzhou(i,1:column), mean(cordistxuzhou(i,1:column), 2))); hold on;
    plot(bsxfun(@rdivide, cordistyancheng(i,1:column), mean(cordistyancheng(i,1:column), 2))); hold on;
    plot(bsxfun(@rdivide, cordisttaizhou(i,1:column), mean(cordisttaizhou(i,1:column), 2)));
    set(gca, 'Xlim', [1 column]);
    set(gca, 'XTickLabel', [20 40 60 80 100]);
	set(gca, 'Ylim', [0 2]);
    title(title_string(i))
end

% figure(5);
% subplot(2,1,1);
% scatter(duration, speed, 1);
% set(gca, 'Xlim', [1 2000]);
% set(gca, 'YScale', 'log');
% title('estimated speed')
% subplot(2,1,2);
% scatter(optduration, optspeed, 1);
% set(gca, 'Xlim', [1 2000]);
% set(gca, 'YScale', 'log');
% title('estimated speed lower bound')