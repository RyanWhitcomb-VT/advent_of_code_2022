
class Elf:
    def __init__(self, cal_list):
        self.cal_list = cal_list
        self.tot_cal = sum(cal_list)
        self.tot_item = count(cal_list)