n = 8;
c = 4;
r = ceil(n/c);
column = 5;
title_string = {'Instant message' ...
    'Reading' ...
    'Microblog' ...
    'Navigation' ...
    'Video' ...        
    'Music' ...
    'App market' ...
    'Browser & Download'};

figure(1); % speed appcat correlation
for i = 1:n
    subplot(r, c, i);
%     marketshare = bsxfun(@rdivide, speedappcatallcity(i,1:column), sum(speedappcatallcity(:,1:column), 1));
    marketshare = bsxfun(@rdivide, speedappcatallcity(i,1:column), speedvol(1, 1:column));
    marketsharexuzhou = bsxfun(@rdivide, speedappcatxuzhou(i,1:column), speedvol(2, 1:column));
    marketshareyancheng = bsxfun(@rdivide, speedappcatyancheng(i,1:column), speedvol(3, 1:column));
    marketsharetaizhou = bsxfun(@rdivide, speedappcattaizhou(i,1:column), speedvol(4, 1:column));
    plot(marketsharexuzhou, '-d'); hold on;
    plot(marketshareyancheng, '-d'); hold on;
    plot(marketsharetaizhou, '-d'); hold on;
    marketshare = marketshare * 100;
    plot(marketshare, '-d', 'LineWidth', 2);
    grid on;
    
    set(gca, 'XTick', [1:column]);
    set(gca, 'XTickLabel', {'0-20'; '20-40'; '40-60'; '60-80'; '80-100'});
    Ymean = mean(marketshare);
    set(gca, 'Ylim', [0.5*Ymean 1.5*Ymean]);
    
    set(gca, 'Fontname', 'Times New Roman', 'Fontsize', 16);
    ylabel_hand=ylabel('Impact (%)');
    set(ylabel_hand,'Fontname', 'Times New Roman', 'Fontsize', 14);
    xlabel_hand=xlabel('Speed range (km/h)');
    set(xlabel_hand,'Fontname', 'Times New Roman', 'Fontsize', 14);
    title(title_string(i))
    
end

figure(2) % speed volume correlation
plot(speedvol(1, 1:column), '-d'); hold on;
plot(speedvol(1, 1:column), '-d'); hold on;
plot(speedvol(1, 1:column), '-d'); hold on;
plot(speedvol(1, 1:column), '-d'); 

set(gca, 'XTick', [1:column]);
set(gca, 'XTickLabel', {'0-20'; '20-40'; '40-60'; '60-80'; '80-100'});

legend('all city', 'xuzhou', 'yancheng', 'taizhou');
set(gca, 'Fontname', 'Times New Roman', 'Fontsize', 16);
ylabel_hand=ylabel('Volume (Byte)');
set(ylabel_hand,'Fontname', 'Times New Roman', 'Fontsize', 14);
xlabel_hand=xlabel('Speed range (km/h)');
set(xlabel_hand,'Fontname', 'Times New Roman', 'Fontsize', 14);

