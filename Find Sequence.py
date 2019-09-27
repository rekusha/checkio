def checkio(m):
    for i in range(len(m)):
        for j in range(len(m)):
            if j + 3 <= len(m) and j + 3 <= len(m)-1:
                if m[i][j] == m[i][j+1] == m[i][j+2] == m[i][j+3]:
                    return True

            if i + 3 <= len(m)-1:
                if m[i][j] == m[i+1][j] == m[i+2][j] == m[i+3][j]:
                    return True

            if i + 3 <= len(m)-1 and j + 3 <= len(m)-1:
                if m[i][j] == m[i+1][j+1] == m[i+2][j+2] == m[i+3][j+3]:
                    return True

            if i + 3 <= len(m)-1 and j - 3 >= 0:
                if m[i][j] == m[i+1][j-1] == m[i+2][j-2] == m[i+3][j-3]:
                    return True
    return False

if __name__ == '__main__':
    print(checkio([[2,1,1,6,1],[1,3,2,1,1],[4,1,1,3,1],[5,5,5,5,5],[1,1,3,1,1]]))

