#1 and #2
plot(CafeRuckus2016$Sales, type = "l")
plot(CafeRuckus2016$Sales)
fivenum(CafeRuckus2016$Sales)
897.230-703.845
193.385*1.5
897.230+290.0775 #anything over 1187.307 is an outlier
703.845-290.0775 #anything below 413.7675 is an outlier
boxplot(CafeRuckus2016$Sales)
hist(CafeRuckus2016$Sales, breaks = c(500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700))
median(CafeRuckus2016$Sales)
#3
boxplot(CafeRuckus2016$Sales ~ CafeRuckus2016$`Day of week`)
#4
#a
#creating side by side boxplots
boxplot(CafeRuckus2016$`Iced Latte`~CafeRuckus2016$`Weather event`)
title(main="Avg. Iced Lattes Sold During Diff. Weather", + xlab="Weather Type", ylab="avg. # of lattes sold")
#b
#creating a linear regression model
model <- lm(CafeRuckus2016$`Iced Latte` ~ CafeRuckus2016$`High temp (F)`)
model
plot(CafeRuckus2016$`High temp (F)`, CafeRuckus2016$`Iced Latte`, main="Avg. Iced Lattes Sold by Temperature Highs", xlab="Temperature Highs in Farenheit", ylab="avg. # of lattes sold")#scatterplot of high temp vs latte sales
#plotting the correlation line over the scatterplot
abline(model)
#5
table(CafeRuckus2016$`Most Popular`,CafeRuckus2016$`Weather event`)
mosaicplot(table(CafeRuckus2016$`Most Popular`,CafeRuckus2016$`Weather event`), xlab = "Most Popular Item", ylab = "WeatherEvent", main = "Most Popular Items in Different Weather Events", color=TRUE)
prop.table(table(CafeRuckus2016$`Most Popular`,CafeRuckus2016$`Weather event`))
barplot(prop.table(table(CafeRuckus2016$`Most Popular`,CafeRuckus2016$`Weather event`),2), xlab = "Weather Event", ylab = "% of Days Most Popular", main = "% of Days Item was Most Popular in Weather Event", legend = TRUE)
#6
# Finding mean/median and distribution of sales of each item
hist(CafeRuckus2016$`Drip Coffee`)
median(CafeRuckus2016$`Drip Coffee`)
mean(CafeRuckus2016$`Drip Coffee`)
hist(CafeRuckus2016$Pastries)
mean(CafeRuckus2016$Pastries)
median(CafeRuckus2016$Pastries)
hist(CafeRuckus2016$Water)
median(CafeRuckus2016$Water)
mean(CafeRuckus2016$Water)
hist(CafeRuckus2016$`Iced Latte`)
median(CafeRuckus2016$`Iced Latte`)
mean(CafeRuckus2016$`Iced Latte`)
hist(CafeRuckus2016$Milkshakes)
median(CafeRuckus2016$Milkshakes)
mean(CafeRuckus2016$Milkshakes)
hist(CafeRuckus2016$`Afternoon Tea Service`)
median(CafeRuckus2016$`Afternoon Tea Service`)
mean(CafeRuckus2016$`Afternoon Tea Service`)
# Create bar graph of medians for each item
itemsales <- c(median(CafeRuckus2016$Water), median(CafeRuckus2016$`Drip Coffee`), median(CafeRuckus2016$`Iced Latte`), median(CafeRuckus2016$Pastries), median(CafeRuckus2016$Milkshakes), median(CafeRuckus2016$`Afternoon Tea Service`))
barplot(itemsales, names.arg = c("Water", "Drip Coffee", "Iced Latte", "Pastries", "Milkshake", "Tea"), col = "steelblue", main = "Median Sales by Item", xlab = "Item", ylab = "Median Sales for 2016")

