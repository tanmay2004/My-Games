print("\nThis program will demonstrate the power of dynamic programming and backtracking. You must provide any ordinary mathematical expression without brackets and its minimum and maximum values that can be obtained after placing brackets in an optimal manner will be generated. The results may surprise you!")

s = input("\nEnter any numeric expression with *, +, - symbols only: ").replace(" ", "")
print(f"The value of the given expression using BODMAS is {eval(s)}")

curr_num = ""
num_arr = []
operators = []

for ch in s:
    if ch.isnumeric():
        curr_num += ch
    else:
        num_arr.append(int(curr_num))
        operators.append(ch)
        curr_num = ""

num_arr.append(int(curr_num))

dp_min = [[None for i in range(len(num_arr))] for j in range(len(num_arr))]
dp_max = [[None for i in range(len(num_arr))] for j in range(len(num_arr))]

back_min = [[(None, None) for i in range(len(num_arr))] for j in range(len(num_arr))]
back_max = [[(None, None) for i in range(len(num_arr))] for j in range(len(num_arr))]

def min_max(a, b, c, d):
    m1, m2 = dp_min[a][b], dp_max[a][b]
    m3, m4 = dp_min[c][d], dp_max[c][d]

    li = [
        eval(f"{m1}{operators[b]}{m3}"),
        eval(f"{m1}{operators[b]}{m4}"),
        eval(f"{m2}{operators[b]}{m3}"),
        eval(f"{m2}{operators[b]}{m4}")
    ]

    return li

for diff in range(len(num_arr)):
    for i in range(len(num_arr)-diff):
        if diff == 0:
            dp_min[i][i] = num_arr[i]
            dp_max[i][i] = num_arr[i]
        else:
            min_tmp = float('inf')
            max_tmp = float('-inf')

            for j in range(i, i+diff):
                curr = min_max(i, j, j+1, i+diff)

                for k in range(4):
                    if curr[k] > max_tmp:
                        max_tmp = curr[k]
                        back_max[i][i+diff] = (j, k)
                    if curr[k] < min_tmp:
                        min_tmp = curr[k]
                        back_min[i][i+diff] = (j, k)

            dp_min[i][i+diff] = min_tmp
            dp_max[i][i+diff] = max_tmp

def backtrack(x, y, minormax):
    if x == y:
        return str(num_arr[x])

    if minormax:
        var_j = back_max[x][y][0]
        var_k = back_max[x][y][1]
    else:
        var_j = back_min[x][y][0]
        var_k = back_min[x][y][1]

    left, right = 1, 1

    if var_k == 0:
        left = 0
        right = 0
    elif var_k == 1:
        left = 0
        right = 1
    elif var_k == 2:
        left = 1
        right = 0

    left_ans = backtrack(x, var_j, left)
    right_ans = backtrack(var_j+1, y, right)

    if x != var_j:
        left_ans = "(" + left_ans + ")"
    if var_j+1 != y:
        right_ans = "(" + right_ans + ")"

    return f"{left_ans} {operators[var_j]} {right_ans}"

minval = dp_min[0][len(num_arr)-1]
maxval = dp_max[0][len(num_arr)-1]

minexp = backtrack(0, len(num_arr)-1, 0)
maxexp = backtrack(0, len(num_arr)-1, 1)

print("\nHowever, if we were to place brackets we would get:\n")
print(f"The minimum value of this expression as {minexp} = {minval}")
print(f"The maximum value of this expression as {maxexp} = {maxval}")
