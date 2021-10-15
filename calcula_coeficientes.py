""" Fun��es auxiliares para a resolu��o do exerc�cio """

""" Rotina que calcula os coeficientes do polin�mio de Chebyshev de maneira n�o-recursiva 

Par�metros: w - vetor de frequ�ncias (sugest�o: usar um vetor com amostras de 0 a 20 rad/s)
            wc - freq. de corte do filtro (em rad/s)
            n - ordem do filtro de Chebyshev
Sa�da:      Tn - vetor com os coeficientes calculados do polin�mio de Chebyshev (possui o mesmo tamanho que w)

"""

def calcula_coeficientes(w,wc,n):
    
    Tn = np.zeros((w.size,))
    #determina os valores dos coeficientes segundo as express�es padronizadas
    Tn[abs(w) < wc] = np.cos(n*np.arccos(w[abs(w) < wc] / wc))
    Tn[abs(w) >= wc] = np.cosh(n*np.arccosh(w[abs(w) >= wc] / wc))
    return Tn

