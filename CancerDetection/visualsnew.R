# change to your data location
setwd('/Users/nick/Documents/MATLAB/canClassTrees/CancerDetection/data/results')
library(ggplot2)
library(reshape2)

r1 <- read.csv("casestudy1.csv")
r1a <- read.csv("casestudiesNEWdata/casestudy1a.csv")
r1aNoDtree <- subset(r1a, method != "DecisionTreeClassifier")
r1aDtree <-subset(r1a, method == "DecisionTreeClassifier")
r1NoDtree <- subset(r1, method != "DecisionTreeClassifier")
r2 <- read.csv("casestudy2.csv")
r3 <- read.csv("casestudy3.csv")
r4 <- read.csv("casestudy4.csv")
r5 <- read.csv("casestudy5.csv")
r6 <- read.csv("casestudy6.csv")
r6a <- read.csv("casestudiesNEWdata/casestudy6a.csv")
r6amelt <- read.csv("casestudiesNEWdata/casestudy6aMelt.csv")




# case study 1

ggplot(data = r1a, aes(x = ntrees, y = aveaccuracy,  linetype = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = r1NoDtree$ntrees) +
  labs(x = 'Number of trees', y = 'Average Accuracy', title = '10 Fold CV Average Accuracy') +
  facet_wrap(~ cancertype) +
  theme_bw()
ggsave("casestudyvis/c1AveaccuracyAGBW.pdf")

ggplot(data = r1NoDtree, aes(x = ntrees, y = computationtime, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = r1NoDtree$ntrees) +
  labs(x = 'Number of trees', y = 'Computation Time', title = 'Random Forest and Adaboost Computation') +
  facet_wrap(~ cancertype)
ggsave("casestudyvis/c1cputime.pdf")


ggplot(data = r1aNoDtree, aes(x = ntrees, y = std, color = method)) +
  geom_point() +
  geom_line() + 
  geom_line(data = r1aDtree, linetype = 2,  aes(x = ntrees, y = std)) +
  scale_x_continuous(breaks = r1NoDtree$ntrees) +
  labs(x = 'Number of trees', y = 'Stand deviatation of fold accuracy', title = 'Random Forest and Adaboost STD') +
  facet_wrap(~ cancertype)
ggsave("casestudyvis/c1stdAG.pdf")

ggplot(data = r1NoDtree, aes(x = ntrees, y = median, color = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = r1NoDtree$ntrees) +
  labs(x = 'Number of trees', y = 'Median', title = '10 Fold CV Median Accuracy') +
  facet_wrap(~ cancertype)
ggsave("casestudyvis/c1MedAccuracy.pdf")


ggplot(data = r1a, aes(x = ntrees, y = std, linetype = method)) +
  geom_point() +
  geom_line() + 
  scale_x_continuous(breaks = r1NoDtree$ntrees) +
  labs(x = 'Number of trees', y = 'Stand deviatation of fold accuracy', title = 'Random Forest and Adaboost STD') +
  facet_wrap(~ cancertype) +
  theme_bw()
ggsave("casestudyvis/c1stdBW.pdf")

r1atree100 <- subset(r1a, ntrees == 100)
ggplot(data = r1atree100, aes(x = cancertype, y = aveaccuracy, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Average Accuracy", title = "Average Accuracy of Decision Tree v. Random Forest and Adaboost with 100 trees" )
ggsave("casestudyvis/c1aAccBar.pdf")

r1atree10 <- subset(r1a, ntrees == 10)
ggplot(data = r1tree10, aes(x = cancertype, y = aveaccuracy, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Average Accuracy", title = "Average Accuracy of Decision Tree v. Random Forest and Adaboost with 10 trees" )
ggsave("casestudyvis/c1aAccBar10.pdf")

# case study 2

r2RF <- subset(r2, method == "RandomForestClassifier")
r2Ada <- subset(r2, method == "AdaBoostClassifier")

ggplot(data = r2RF, aes(x = cancertype, y = aveaccuracy, fill=kstrat)) +
  geom_bar(stat = "identity", width=.7, position = "dodge") +
  theme_bw()+
  scale_fill_grey()+
  labs(x = 'Cancer Type', y = 'Average Accuracy', title = 'Random Forest, Effects of Stratified Sampling')
ggsave("casestudyvis/c2rfStratBW.pdf")

ggplot(data = r2Ada, aes(x = cancertype, y = aveaccuracy, fill=kstrat)) +
  theme_bw()+
  scale_fill_grey()+
  geom_bar(stat = "identity", width=.7, position = "dodge") +
  labs(x = 'Cancer Type', y = 'Average Accuracy', title = 'AdaBoost, Effects of Stratified Sampling')
ggsave("casestudyvis/c2AdaStratBW.pdf")

ggplot(data = r2RF, aes(x = cancertype, y = median, fill=kstrat)) +
  geom_bar(stat = "identity", width=.7, position = "dodge") +
  labs(x = 'Cancer Type', y = 'Median Accuracy', title = 'Random Forest, Effects of Stratified Sampling')
ggsave("casestudyvis/c2MedrfStrat.pdf")

ggplot(data = r2Ada, aes(x = cancertype, y = median, fill=kstrat)) +
  geom_bar(stat = "identity", width=.7, position = "dodge") +
  labs(x = 'Cancer Type', y = 'Median Accuracy', title = 'Adaboost, Effects of Stratified Sampling')
ggsave("casestudyvis/c2MedadaStrat.pdf")

# case study 3

ggplot(data = r3, aes(x = cancertype, y = aveaccuracy, fill = method)) +
  theme_bw()+
  scale_fill_grey()+
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Average Accuracy", title = "Average Accuracy with Random Feature Selection")
ggsave("casestudyvis/c3featuresizeBW.pdf")

ggplot(data = r3, aes(x = cancertype, y = median, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Median Accuracy", title = "Median Accuracy Size of Random Feature Selection Random Forrest")
ggsave("casestudyvis/c3Medfeaturesize.pdf")
# case study 4

ggplot(data = r4, aes(x = cancertype, y = aveaccuracy, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Average Accuracy", title = "Average Accuracy between ExtraForest and RandomForest" )
ggsave("casestudyvis/c4accExtraRandom.pdf")

ggplot(data = r4, aes(x = cancertype, y = median, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Median Accuracy", title = "Median Accuracy between ExtraForest and RandomForest" )
ggsave("casestudyvis/c4MedaccExtraRandom.pdf")

ggplot(data = r4, aes(x = cancertype, y = computationtime, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Computation Time", title = "Computation Time between ExtraForest and RandomForest" )
ggsave("casestudyvis/c4cputime.pdf")

# case study 5

ggplot(data = r5, aes(x = factor(cancertype), y = aveaccuracy, fill=factor(method))) +
  scale_fill_grey() +
  theme_bw() +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Average Accuracy", title = " Average Accuracy of Rforest vs. bootstrap True/False" )
ggsave("casestudyvis/c5BootAveAccBW.pdf")

ggplot(data = r5, aes(x = cancertype, y = median, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Median Accuracy", title = "Median Accuracy with Bootstrapping or Not on Random Forest" )
ggsave("casestudyvis/c5BootMedAcc.pdf")

ggplot(data = r5, aes(x = cancertype, y = computationtime, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Computation Time", title = "RandomForest Bootstrapping Computation Time" )
ggsave("casestudyvis/c5BootCPU.pdf")

# case study 6

ggplot(data = r6, aes(x = cancertype, y = aveaccuracy, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Average Accuracy", title = "Average Accuracy of 4 Methods" )
ggsave("casestudyvis/c6acc4method.pdf")

ggplot(data = r6, aes(x = cancertype, y = median, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Median Accuracy", title = "Median Accuracy of 4 Methods" )
ggsave("casestudyvis/c6Medacc4method.pdf")

ggplot(data = r6, aes(x = cancertype, y = computationtime, fill = method)) +
  geom_bar(stat = "identity", width = .7, position = "dodge") +
  labs(x = "Cancer Type", y = "Computation Time", title = "Computation Time of 4 Methods" )
ggsave("casestudyvis/c6CPU4method.pdf")

ggplot(data = r6amelt, aes(x = method, y = Accuracy, fill = method)) +
  theme_bw()+
  scale_fill_grey()+
  geom_boxplot() +
  labs(x = "Method", y = "Accuracy", title = "Accuracy distributions" )+
  scale_x_discrete(breaks=NULL) +
  geom_jitter(width = 0.1, alpha = .4)+
  facet_wrap(~cancertype)
ggsave("casestudyvis/c6aBoxPlotsAGBW.pdf")

  
  



