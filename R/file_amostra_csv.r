amostra <- read.csv("amostra.csv", header = TRUE, sep = ";")
pie(table(amostra$EstCivil))

rotulos <- paste(round((prop.table(table(amostra$EstCivil)) * 100), 2), "%")
pie(prop.table(table(amostra$EstCivil))*100, main="Estado Civil", labels=rotulos, col=c("pink",
"blue", "purple"))

legend("topright", pch=15, col=c("pink","purple","blue"), legend=c("casado","divorciado","separado"))

hist(amostra$Renda, br = c(0, 15, 30, 45, 60, max(amostra$Renda)))
hist(amostra$Renda, density = 30, freq = FALSE)

plot(amostra$Renda, amostra$Idade)

boxplot(amostra$Idade)
boxplot(amostra$Idade~amostra$EstCivil)
