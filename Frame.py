class Frame:

    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        self.score_list_1 = []
        self.score_list_2 = []
        self.frame_open = True

    def create_list(self):
        self.score_list_1.append(self.name1)
        self.score_list_2.append(self.name2)
        print(self.score_list_1, self.score_list_2)

    def save_score(self, name, result):
        if name == self.name1:
            self.score_list_1.append(result)
        else:
            self.score_list_2.append(result)

    def op_cl_frame(self, name):
        if name == self.name2:
            self.frame_open = False
            return self.frame_open

