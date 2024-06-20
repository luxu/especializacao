defeito <- c(8, 15, 11)
semdefeito <- c(62, 67, 57)

dados <- matrix(c(8, 15, 11, 62, 67, 57), nrow = 2, byrow = TRUE)
rownames(dados) <- c("D", "SD")
colnames(dados) <- c("F1", "F2", "F3")
dados

# Realizar o teste qui-quadrado de independência
resultado <- chisq.test(dados)
resultado
