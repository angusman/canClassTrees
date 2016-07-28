
# change to your data location
setwd('/Users/nick/Documents/MATLAB/canClassTrees/CancerDetection/data/results')
library(ggplot2)

temp = list.files(pattern="*.csv")
homebrew <- read.csv(temp[1])
sklearn <- read.csv(temp[2])
sklearn <- subset(sklearn, kfolds ==5 & method == 'randomforest')


keeps <- c('aveaccuracy', 'computationtime', 'cancertype', 'maxsinglefold', 'method', 'minsinglefold' , 'std', 'ntrees')
sklearn <- sklearn[keeps]
homebrew <- homebrew[keeps]

full_df <- rbind(sklearn,homebrew)

ggplot(data = full_df, aes(x = ntrees, y = aveaccuracy, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Average Accuracy', title = '5 Fold CV') +
  facet_wrap(~ cancertype)
ggsave('AverageaccHBvSK.pdf')


ggplot(data = full_df, aes(x = ntrees, y = maxsinglefold, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Max accuracy for a single fold', title = 'Max of Accuracy of the 5 Folds') +
  facet_wrap(~ cancertype)
ggsave('MaxAccHBvSK.pdf')

ggplot(data = full_df, aes(x = ntrees, y = minsinglefold, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Min accuracy for a single fold', title = 'Min of Accuracy of the 5 Folds') +
  facet_wrap(~ cancertype)
ggsave('MinAccHBvSK.pdf')

ggplot(data = full_df, aes(x = ntrees, y = std, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Standard deviation of fold results', title = '5 Fold CV STD') +
  facet_wrap(~ cancertype)
ggsave('StdHBvSK.pdf')
  
ggplot(data = full_df, aes(x = ntrees, y = aveaccuracy, color = method)) +
  geom_point() +
  geom_line() + 
  labs(x = 'Number of trees', y = 'Fold accuracy', title = '5 Fold CV accuracy') +
  facet_wrap(~ cancertype) +
  scale_x_continuous(breaks = full_df$ntrees) +
  geom_line(linetype = 2, aes(y = maxsinglefold)) + 
  geom_line(linetype = 2, aes(y = minsinglefold))
ggsave('AccBoundsHBvSK.pdf')
