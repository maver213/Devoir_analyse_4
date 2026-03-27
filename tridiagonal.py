def tridiagonal(N, D, I, S, b):
    D = D.copy()
    I = I.copy()
    S = S.copy()
    b = b.copy()

    for i in range(1, N):
        w = I[i-1] / D[i-1]
        D[i] = D[i] - w * S[i-1]
        b[i] = b[i] - w * b[i-1]

    x = [0] * N
    x[N-1] = b[N-1] / D[N-1]

    for i in range(N-2, -1, -1):
        x[i] = (b[i] - S[i] * x[i+1]) / D[i]

    return x