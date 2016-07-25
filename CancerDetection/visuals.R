
# change to your data location
setwd('/Users/nick/Documents/MATLAB/canClassTrees/CancerDetection/data/results')
library(ggplot2)

temp = list.files(pattern="*.csv")

full_df = data.frame(X = numeric(0), aveaccuracy = numeric(0), cancertype = numeric(0),
                     fold0 = numeric(0), fold1 = numeric(0), fold2 = numeric(0),
                     fold3 = numeric(0), fold4 = numeric(0), ntrees = numeric(0), 
                     maxsinglefold = numeric(0), minsinglefold = numeric(0), std = numeric(0),
                     timestamp, computationtime = numeric(0))

for (i in temp){
  print(i)
  temp_df <- read.csv(file = i, head = TRUE)
  full_df <- rbind(full_df,temp_df)
}


ggplot(data = full_df, aes(x = ntrees, y = aveaccuracy, color = cancertype)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Average Accuracy', title = '5 Fold CV') +
  facet_wrap(~ cancertype)

ggplot(data = full_df, aes(x = ntrees, y = maxsinglefold, color = cancertype)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Max accuracy for a single fold', title = 'Max of Accuracy of the 5 Folds') +
  facet_wrap(~ cancertype)

ggplot(data = full_df, aes(x = ntrees, y = std, color = cancertype)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Standard deviation of fold results', title = '5 Fold CV STD') +
  facet_wrap(~ cancertype)
  
ggplot(data = full_df, aes(x = ntrees, y = aveaccuracy, color = cancertype)) +
  geom_point() +
  geom_line() + 
  labs(x = 'Number of trees', y = 'Fold accuracy', title = '5 Fold CV accuracy') +
  facet_wrap(~ cancertype) +
  scale_x_continuous(breaks = full_df$ntrees) +
  geom_line(linetype = 2, aes(y = maxsinglefold, colour = "max fold acc")) + 
  geom_line(linetype = 2, aes(y = minsinglefold, colour = "min fold acc"))
