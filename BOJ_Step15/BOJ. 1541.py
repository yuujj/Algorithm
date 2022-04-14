### 잃어버린 괄호 ###
line = input()

if line[0] == '-':
    nums = line.split('-')
    nums_ = ['-'+str(sum(map(int,n.split('+')))) for n in nums]
    answer = sum(map(int, nums_))

else:
    nums = line.split('-')
    nums_ = ['-' + str(sum(map(int, n.split('+')))) for idx, n in enumerate(nums)]
    nums_[0] = nums_[0][1:]
    answer = sum(map(int, nums_))
print(answer)