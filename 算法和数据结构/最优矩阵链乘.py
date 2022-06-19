N = 5  # 定义矩阵的数量+1
p = [5, 5, 10, 4, 2]
m = [[0 for _ in range(0, N)] for _ in range(0, N)]
s = [[0 for _ in range(0, N)] for _ in range(0, N)]


def MatrixChina(n):
    for r in range(2, n + 1):
        for i in range(1, n - r + 2):
            j = i + r - 1
            m[i][j] = m[i + 1][j] + p[i - 1] * p[i] * p[j]
            s[i][j] = i
            for k in range(i + 1, j):
                t = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k


def cout(i, j):
    if i == j:
        print('A[', i, ']', end=' ')
        return
    print('(', end=' ')
    cout(i, s[i][j])
    cout(s[i][j] + 1, j)  # 递归1到s[1][j]
    print(')', end=' ')


if __name__ == '__main__':
    MatrixChina(N - 1)
    for i in m[1:]:
        print(i[1:])
    cout(1, N - 1)


for i, w in enumerate(p):
    print(i, w)
print(p[:0])

dict1 = {("q","y"): 3}
print(dict1["q","y"])

dict1 = {('_UNK_', '_UNK_'): {'this': 3},
             ('_UNK_', 'this'): {'is': 3},
             ('a', 'good'): {'sentence': 2},
             ('a', 'test'): {'sentence': 1},
             ('good', 'sentence'): {'_EOS_': 2},
             ('is', 'a'): {'good': 2, 'test': 1},
             ('test', 'sentence'): {'_EOS_': 1},
             ('this', 'is'): {'a': 3}}
for key, value in dict1.items():
    sumup = sum([v for v in value.values()])
    for k, v in value.items():
        value[k] = v/sumup
    dict1[key] = value
print(dict1)

p.pop()
print(p)