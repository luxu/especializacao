fornecedor_A <- c(1.0, 1.2, 1.5, 1.8, 2.5)
fornecedor_B <- c(1.6, 2.5, 1.2, 2.3, 1.5)
fornecedor_A
fornecedor_B

maior_menor_nro_A <- range(fornecedor_A)
maior_menor_nro_A

amplitude_A <- diff(maior_menor_nro_A)
amplitude_A # 1.5

maior_menor_nro_B <- range(fornecedor_B)
maior_menor_nro_B

amplitude_B <- diff(maior_menor_nro_B)
amplitude_B # 1.3
