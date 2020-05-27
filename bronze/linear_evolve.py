
def linear_evolve(B, v):
    u = []
    for i in range(len(B)):
        u_i = sum(B[i][j] * v[j] for j in range(len(v)))
        u.append(u_i)
    return u
