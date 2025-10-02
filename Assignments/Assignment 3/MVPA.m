[STUDY, ALLEEG] = pop_loadstudy('filename', 'D:\Reza\Principles of Cognitive Science\Assignment\Assignment 3\Datasets\face-doll.study');

doll_triggers = STUDY.design.variable.value{2};

data_all = {};
triggers_all = [];

for i = 1:length(STUDY.datasetinfo)
    % Load subject EEG data
    EEG = pop_loadset('filename', STUDY.datasetinfo(i).filename, 'filepath', STUDY.datasetinfo(i).filepath);
    
    % Get trigger events per trial
    if iscell(EEG.epoch(i).eventlatency)
        trial_triggers = cell(1, length(EEG.epoch));
        for j = 1:length(EEG.epoch)
            zero_latency_indices = find([EEG.epoch(j).eventlatency{:}] == 0);
            trial_triggers{j} = EEG.epoch(j).eventtype{zero_latency_indices(1)};
        end
    else
        trial_triggers = {EEG.epoch.eventtype};
    end
    
    % Extract EEG data: channels × time × trials → convert to trials × channels × time
    trials = EEG.data;
    trials = permute(trials, [3,1,2]);

    % Append
    data_all{end+1} = trials;
    triggers_all = [triggers_all; trial_triggers(:)];
end

% Final data
t = EEG.times;
data = cat(1, data_all{:});   % trials × channels × time
labels = ismember(triggers_all, doll_triggers) + 1;
channels = {EEG.chanlocs.labels};

save('dataset.mat', 't', 'data', 'triggers_all', 'channels');

%% Temporal MVPA
cfg = [];
cfg.classifier = 'lda';
cfg.metric = {'accuracy', 'auc', 'f1'};
cfg.cv = 'kfold';
cfg.k = 5;

% Run MVPA
[~, result] = mv_classify_across_time(cfg, data, labels);

% plot result
h = mv_plot_result(result);

for i = 1:numel(h.plot)
    ax = h.plot(i).ax;
    ax_children = ax.Children;
    
    for k = 1:numel(ax_children)
        obj = ax_children(k);
        if isa(obj, 'matlab.graphics.primitive.Patch')
            obj.XData = [t, fliplr(t)];
        else
            obj.XData = linspace(t(1), t(end), numel(obj.YData));
        end
    end
    
    ax.XLimMode = 'auto';
end

%% Spatial MVPA
t_idx = find(t >= 100 & t <= 300);
data_avg = mean(data(:,:,t_idx), 3);  % trials × channels

[perf, result] = mv_classify(cfg, data_avg, labels);

figure;
weights = result.classifier.w;
topoplot(weights, EEG.chanlocs);

%% Cross-Temporal Generalization
[perf, result] = mv_classify_timextime(cfg, data, labels);

h = mv_plot_result(result);
for i = 1:numel(h.ax)
    ax = h.ax(i).ax;
    im = ax.Children;
    im.XData = t;
    im.YData = t;
    axis(ax, 'image');
    line(ax, [t(1), t(end)], [t(1), t(end)], 'LineStyle', '--');
end