# install.packages("tm")
# install.packages('reshape2')
# install.packages("SnowballC")
# install.packages('wordcloud')
library(tm) 
library(reshape2)
library(ggplot2)
library(SnowballC)
library(wordcloud)

createCorpus <- function(filepath) {
  conn <- file(filepath, "r")
  fulltext <- readLines(conn)
  close(conn)
  vs <- VectorSource(fulltext)
  Corpus(vs, readerControl=list(readPlain, language="en", load=TRUE))
}

news_corpus <- createCorpus("Teste3.txt")
news_corpus

dtm <- DocumentTermMatrix(news_corpus)   
dtm.matrix <- as.matrix(dtm)
wordcount <- colSums(dtm.matrix)
topten <- head(sort(wordcount, decreasing=TRUE), 10)

dfplot <- as.data.frame(melt(topten))
dfplot$word <- dimnames(dfplot)[[1]]
dfplot$word <- factor(dfplot$word,
                       levels=dfplot$word[order(dfplot$value,
                                                decreasing=TRUE)])
fig <- ggplot(dfplot, aes(x=word, y=value)) + geom_bar(stat="identity")
fig <- fig + xlab("Palavras")
fig <- fig + ylab("Frequência")
print(fig)

set.seed(142) # O comando set.seed garante que os resultados obtidos possam ser reproduzidos em qualquer computador.
wordcloud(names(wordcount), wordcount, min.freq=25)
wordcloud(names(wordcount), wordcount, min.freq=25, colors=brewer.pal(6, "Dark2"))
wordcloud(names(wordcount), wordcount, max.words=100, rot.per=0.2, colors=brewer.pal(6, "Dark2"))
