library(caret)
iris_1 <- read.csv("iris (1).csv",row.names = 1,stringsAsFactors = T)
iris_1
summary(iris_1)
View(iris_1)
boxplot(iris_1)
is.na(iris_1)
sapply