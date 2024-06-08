library(ggplot2)

row_1 = read.table(text = clipr::read_clip())
row_2 = read.table(text = clipr::read_clip())
row_3 = read.table(text = clipr::read_clip())

dados_df = data.frame(
  Variavel1 = row_1,
  Variavel2 = row_2
)

ggplot(dados_df, aes(x = row_1, y = row_2)) +
  geom_point() +
  geom_smooth(method = "lm", se = FALSE) +
  labs(x = "Variável 1", y = "Variável 2", title = "Diagrama de Dispersão")

