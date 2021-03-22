from Frame import Frame


class Game(Frame):

    def frames(self):
        Frame.create_list(self)
        for i in range(10):
            self.frame_open = True
            actual_name = self.name1
            while self.frame_open:
                print('Turn {}.'.format(actual_name))
                num_pins = int(input('Frame №{} Enter the number of pins hit. First throw:'.format(i + 1)))
                Game.ident_throw(self, num_pins, actual_name, i)
                Game.print_table(self)
                Frame.op_cl_frame(self, actual_name)
                actual_name = self.name2

    def print_table(self):
        name_str = max(len(self.name1), len(self.name2))
        frame_str = len(self.score_list_1) - 1
        frame_str2 = len(self.score_list_2) - 1
        print((name_str + 5) * '-', frame_str * 11 * '-')
        # print first row
        for i in range(frame_str + 1):
            if i == 0:
                print('| Name', (name_str - 3) * ' ', '|', end='')
            else:
                print(' Frame{}'.format(i), ' ', '|', end="")
        print()
        print((name_str + 5) * '-', frame_str * 11 * '-')
        # print second row
        for i in range(frame_str + 1):
            if i == 0:
                print('|', self.name1, (name_str - len(self.name1) + 1)*' ', '|', end='')
            else:
                print(' ', self.score_list_1[i], (6 - len(self.score_list_1[i])) * ' ', '|', end="")
        print()
        print((name_str + 5) * '-', frame_str * 11 * '-')
        # print third row
        for i in range(frame_str2 + 1):
            if i == 0:
                print('|', self.name2, (name_str - len(self.name2) + 1) * ' ', '|', end='')
            else:
                print(' ', self.score_list_2[i], (6 - len(self.score_list_2[i])) * ' ', '|', end="")
        print()
        print((name_str + 5) * '-', frame_str * 11 * '-')

    def ident_throw(self, num_pins, actual_name, i):
        if (num_pins >= 0) and (num_pins < 10) and i < 9:
            num_pins2 = int(input('Frame №{} Enter the number of pins hit. Second throw:'.format(i + 1)))
            if num_pins + num_pins2 == 10:
                print('SPARE')
                Frame.save_score(self, actual_name, str(num_pins) + '/', i)
            else:
                print('OPEN')
                Frame.save_score(self, actual_name, str(num_pins) + str(num_pins2), i)
        elif num_pins == 10 and i < 9:
            print('STRIKE')
            Frame.save_score(self, actual_name, 'X', i)

        elif i == 9:
            frame10 = ""
            num_pins2 = int(input('Frame №{} Enter the number of pins hit. Second throw:'.format(i + 1)))
            if num_pins == 10 or num_pins2 == 10 or num_pins + num_pins2 == 10:
                num_pins3 = int(input('Frame №{} Enter the number of pins hit. Second throw:'.format(i + 1)))
                if num_pins == 10:
                    frame10 += 'X'
                else:
                    frame10 += str(num_pins)
                if num_pins2 == 10:
                    frame10 += 'X'
                else:
                    frame10 += str(num_pins2)
                if num_pins3 == 10:
                    frame10 += 'X'
                else:
                    frame10 += str(num_pins3)
            else:
                frame10 += str(num_pins) + str(num_pins2)

            Frame.save_score(self, actual_name, frame10, i)
