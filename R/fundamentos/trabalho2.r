library(ggplot2)
dados=read.csv("graduacao.csv", header = T, sep = ";")
categorias=c('especialistas','mestres', 'doutores')
#especialista = 294 / 3012 = 0.09760956 * 100 = 9.7 %
#mestres = 1099 / 3012 = 0.3648738 * 100 =     36.48 %
#doutores = 1619 / 3012 = 0.5375166 * 100 =    53.75 %
#9.7 + 36.48 + 53.75 = 99.93 %
porcentagem=c(9.7,36.48,53.75)

resultado = matrix(c(categorias,porcentagem), nrow = 2, ncol = 3, byrow = T )

df = data.frame(
  Categorias = categorias,
  Porcentagem = porcentagem
)

ggplot(df, aes(x = Categorias, y = Porcentagem, fill = Categorias)) + geom_bar(stat = 'identity') +
  theme_minimal()
