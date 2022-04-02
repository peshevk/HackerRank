if __name__ == '__main__':

    score_list = []
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score in score_list:
            records.append([name, score])
        else:
            score_list.append(score)
            records.append([name, score])
    score_list = sorted(score_list, reverse=True)

    for record in sorted(records):
        if record[1] == score_list[-2]:
            print(record[0])
