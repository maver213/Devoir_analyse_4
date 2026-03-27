from tridiagonal import tridiagonal

def problimite(N, Q, R, a, b, alpha, beta):
    h = (b - a) / (N + 1)

    D = [0] * N
    I = [-1 / h**2] * (N - 1)
    S = [-1 / h**2] * (N - 1)
    B = [0] * N

    for i in range(N):
        D[i] = 2 / h**2 + Q[i]
        B[i] = R[i]

    B[0] += alpha / h**2
    B[N-1] += beta / h**2

    y_interne = tridiagonal(N, D, I, S, B)

    y = [0] * (N + 2)
    y[0] = alpha
    y[N + 1] = beta

    for i in range(N):
        y[i + 1] = y_interne[i]

    return y