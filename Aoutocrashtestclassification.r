#Automative Crash Testing
#poor -10
#excellent +10
rm(list=ls())
library(caret)
#reading the data
crashTest_1 <- read.csv("crashTest_1.csv",row.name=1,stringsAsFactors = T)
crashTest_1_TEST <- read.csv("crashTest_1_TEST.csv",row.name=1,stringsAsFactors = T)
#viewing the data
View(crashTest_1)
View(crashTest_1_TEST)
str(crashTest_1)
str(crashTest_1_TEST)
summary(crashTest_1)
summary(crashTest_1_TEST)
#model
logisfit <- glm(formula=crashTest_1$CarType~., family='binomial',data = crashTest_1)
logisfit
summary(logisfit)
#Finding the odds
logisTrain <- predict(logisfit, type = 'response')
plot(logisTrain)
#mean of probabilities
tapply(logisTrain,crashTest_1$CarType,mean)
#predicting on test set
logisPred <- predict(logisfit, newdata=crashTest_1_TEST,type='response')
plot(logisPred)
logisPred
crashTest_1_TEST[logisPred<=0.5,"LogisPred"] <- "Hatchback"
crashTest_1_TEST[logisPred>0.5,"LogisPred"] <- "SUV"
confusionMatrix(table(crashTest_1_TEST[,7],crashTest_1_TEST[,6]),positive = 'Hatchback')
