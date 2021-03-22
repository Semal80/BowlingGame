class Frame:

    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        self.score_list_1 = []
        self.score_list_2 = []
        self.frame_open = True
        self.score1 = 0
        self.score2 = 0


    def create_list(self):
        self.score_list_1.append(self.name1)
        self.score_list_2.append(self.name2)
        # print(self.score_list_1, self.score_list_2)

    def save_score(self, name, result, frame):
        if name == self.name1:
            self.score_list_1.append(result)
        else:
            self.score_list_2.append(result)

    def op_cl_frame(self, name):
        if name == self.name2:
            self.frame_open = False
            return self.frame_open

    def score(self):
        # testing
        # score_list1 = ['Neo', '45', '54', '36', '27', '09', '63', '81', '18', '90', '72']
        # score_list1 = ['Neo', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'XXX']
        # score_list1 = ['Neo', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '5/', '555']
        # score_list1 = ['Neo', '80', '72', '60', '62', '08', '61', '90', '80', '81', '52']
        # score_list1 = ['Neo', '81', '7/', '53', '0/', '7/', '9/', '90', '8/', '81', '551']
        # score_list1 = ['Neo', '81', 'X', '6/', '81', '9/', 'X', 'X', 'X', '9/', 'XX8']
        Frame.calculate_score(self, self.score_list_1)
        Frame.calculate_score(self, self.score_list_2)


    def calculate_score(self, score_list):
        score_list_add = []
        last = score_list[-1]
        last_list = []
        score_list.remove(last)
        for i in last:
            if i == 'X':
                score_list.append(i)
            else:
                score_list.append(i)
        score = 0

        for i in range(1, 10):
            if score_list[i] == 'X' and score_list[i + 1] == 'X' and score_list[i + 2] == "X":
                score += (10 + 10 + 10)
                score_list_add.append(30)
            elif score_list[i] == 'X' and score_list[i + 1] == 'X' and len(score_list[i + 2]) != 'X':
                score += (10 + 10) + int(score_list[i + 2][0])
                score_list_add.append((10 + 10) + int(score_list[i + 2][0]))
            elif score_list[i] == 'X' and len(score_list[i + 1]) == 2 and (score_list[i + 1][1] == '/'):
                score += (10 + 10)
                score_list_add.append((10 + 10))
            elif score_list[i] == 'X' and len(score_list[i + 1]) == 2 and (score_list[i + 1][1] != '/'):
                score += (10 + int(score_list[i + 1][0]) + int(score_list[i + 1][1]))
                score_list_add.append((10 + int(score_list[i + 1][0]) + int(score_list[i + 1][1])))
            elif len(score_list[i]) == 2 and score_list[i][1] == '/' and score_list[i + 1] == 'X':
                score += (10 + 10)
                score_list_add.append((10 + 10))
            elif len(score_list[i]) == 2 and score_list[i][1] == '/':
                score += (10 + int(score_list[i + 1][0]))
                score_list_add.append((10 + int(score_list[i + 1][0])))
            elif len(score_list[i]) == 2 and score_list[i][1] != '/':
                score += (int(score_list[i][0]) + int(score_list[i][1]))
                score_list_add.append((int(score_list[i][0]) + int(score_list[i][1])))
            else:
                score_list_add.append('uuuuu')

        score_list_add.append(0)
        for i in range(10, len(score_list)):
            if score_list[i] == 'X':
                score += 10
                score_list_add[9] += 10
            else:
                score += int(score_list[i])
                score_list_add[9] += int(score_list[i])

        if score_list[0] == self.name1:
            self.score1 = score
            score_list_add.insert(0, self.name1)
            print(score_list_add)
        else:
            self.score2 = score
            score_list_add.insert(0, self.name2)
            print(score_list_add)



