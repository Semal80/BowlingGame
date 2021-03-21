from Frame import Frame


class Game(Frame):

    def turn(self):
        Frame.create_list(self)
        for i in range(3):
            self.frame_open = True
            actual_name = self.name1
            while self.frame_open:
                print('Turn {}.'.format(actual_name))
                num_pins = int(input('Frame №{} Enter the number of pins hit. First throw:'.format(i + 1)))
                if (num_pins >= 0) and (num_pins < 10):
                    num_pins2 = int(input('Frame №{} Enter the number of pins hit. Second throw:'.format(i + 1)))
                    if num_pins + num_pins2 == 10:
                        print('SPARE')
                        Frame.save_score(self, actual_name, str(num_pins)+'/')
                        Frame.op_cl_frame(self, actual_name)
                        actual_name = self.name2
                    else:
                        print('OPEN')
                        Frame.save_score(self, actual_name, str(num_pins) + str(num_pins2))
                        Frame.op_cl_frame(self, actual_name)
                        actual_name = self.name2
                else:
                    print('STRIKE')
                    Frame.save_score(self, actual_name, 'X')
                    Frame.op_cl_frame(self, actual_name)
                    actual_name = self.name2


    def print_table(self):
        return print(print(self.score_list_1, self.score_list_2))

    # def close_frame(self, pins):
    #     if pins == 10:

