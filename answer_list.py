import RE4M
answer_list = RE4M.ans
with open("ANSWER.txt", "w") as f:
    for i in range(len(answer_list)):
        if i != 0:
            f.write("{} : {} \n".format(i, answer_list[i]))