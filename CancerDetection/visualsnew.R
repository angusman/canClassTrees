# change to your data location
setwd('/Users/nick/Documents/MATLAB/canClassTrees/CancerDetection/data/results')
library(ggplot2)

r1 <- read.csv("casestudy1.csv")
r1a <- read.csv("casestudy1a.csv")
r1a <- subset(r1a, method != "DecisionTreeClassifier")
r2 <- read.csv("casestudy2.csv")
r3 <- read.csv("casestudy3.csv")
r4 <- read.csv("casestudy4.csv")
r5 <- read.csv("casestudy5.csv")
r6 <- read.csv("casestudy6.csv")

# case study 1

ggplot(data = r1, aes(x = ntrees, y = aveaccuracy, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Average Accuracy', title = '10 Fold CV') +
  facet_wrap(~ cancertype)
ggsave("casestudyvis/c1accuracy.pdf")

ggplot(data = r1, aes(x = ntrees, y = computationtime, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Computation Time', title = 'Random Forest and Adaboost Computation') +
  facet_wrap(~ cancertype)
ggsave("casestudyvis/c1cputime.pdf")


ggplot(data = r1, aes(x = ntrees, y = std, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Stand deviatation of fold accuracy', title = 'Random Forest and Adaboost STD') +
  facet_wrap(~ cancertype)
ggsave("casestudyvis/c1std.pdf")

# case study 1a

ggplot(data = r1a, aes(x = ntrees, y = aveaccuracy, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Average Accuracy', title = '10 Fold CV') +
  facet_wrap(~ cancertype)
ggsave("casestudyvis/c1Aaccuracy.pdf")

ggplot(data = r1a, aes(x = ntrees, y = computationtime, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Computation Time', title = 'Random Forest and Adaboost Computation') +
  facet_wrap(~ cancertype)
ggsave("casestudyvis/c1Acputime.pdf")


ggplot(data = r1a, aes(x = ntrees, y = std, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = full_df$ntrees) +
  labs(x = 'Number of trees', y = 'Stand deviatation of fold accuracy', title = 'Random Forest and Adaboost Computation STD') +
  facet_wrap(~ cancertype)
ggsave("casestudyvis/c1Astd.pdf")

# case study 2

r2RF <- subset(r2, method == "RandomForestClassifier")
r2Ada <- subset(r2, method == "AdaBoostClassifier")

ggplot(data = r2RF, aes(x = cancertype, y = aveaccuracy, fill=kstrat)) +
  geom_bar(stat = "identity", width=.7, position = "dodge") +
  labs(x = 'Cancer Type', y = 'Average Accuracy', title = 'Random Forest, Effects of Stratified Sampling')
ggsave("casestudyvis/c2rfStrat.pdf")

ggplot(data = r2Ada, aes(x = cancertype, y = aveaccuracy, fill=kstrat)) +
  geom_bar(stat = "identity", width=.7, position = "dodge") +
  labs(x = 'Cancer Type', y = 'Average Accuracy', title = 'Adaboost, Effects of Stratified Sampling')
ggsave("casestudyvis/c2adaStrat.pdf")

# case study 3

ggplot(data = r3, aes(x = cancertype, y = aveaccuracy, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Average Accuracy", title = "Size of Random Feature Selection Random Forrest")
ggsave("casestudyvis/c3featuresize.pdf")
# case study 4

ggplot(data = r4, aes(x = cancertype, y = aveaccuracy, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Average Accuracy", title = "Accuracy between ExtraForest and RandomForest" )
ggsave("casestudyvis/c4accExtraRandom.pdf")

ggplot(data = r4, aes(x = cancertype, y = computationtime, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Computation Time", title = "Computation Time between ExtraForest and RandomForest" )
ggsave("casestudyvis/c4cputime.pdf")

# case study 5

ggplot(data = r5, aes(x = cancertype, y = aveaccuracy, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Average Accuracy", title = "Accuracy with Bootstrapping or Not on Random Forest" )
ggsave("casestudyvis/c5BootAcc.pdf")

ggplot(data = r5, aes(x = cancertype, y = computationtime, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Computation Time", title = "RandomForest Bootstrapping Computation Time" )
ggsave("casestudyvis/c5BootCPU.pdf")

# case study 6

ggplot(data = r6, aes(x = cancertype, y = aveaccuracy, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Average Accuracy", title = "Accuracy of 4 Methods" )
ggsave("casestudyvis/c6acc3method.pdf")

ggplot(data = r6, aes(x = cancertype, y = computationtime, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Computation Time", title = "Computation Time of 4 Methods" )
ggsave("casestudyvis/c6CPU3method.pdf")
