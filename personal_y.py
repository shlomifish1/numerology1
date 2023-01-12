from datetime import date
import name
today = date.today()


class This_Year:
    def __init__(self):
        # self.this_month = None
        # self.this_year = None
        self.shana_nisteret_calc = None
        self.shana_ishit_calc = None
        self.final_short_this_year = None
        self.this_year_list = None
        self.this_year = int(today.strftime("%Y"))
        self.this_month = int(today.strftime("%m"))
        self.this_year_list = [x for x in str(self.this_year)]
        self.final_short_this_year = map(int, self.this_year_list)
        self.final_short_this_year = sum(self.final_short_this_year)



    def shana_ishit(self, day, month, bd_month):
        self.shana_ishit_calc = int(day + month + self.final_short_this_year)
        if bd_month > int(self.this_month):
            self.shana_ishit_calc -= 1
        if bd_month > 6:
            self.shana_ishit_calc += 1
        if self.shana_ishit_calc > 9:
            self.shana_ishit_calc = name.NamesData().sum_num(self.shana_ishit_calc)
        return self.shana_ishit_calc

    def shana_nisteret(self, destiny, ishit):
        self.shana_nisteret_calc = int(ishit + destiny)
        if self.shana_nisteret_calc > 9:
            self.shana_nisteret_calc = name.NamesData().sum_num(self.shana_nisteret_calc)
        return self.shana_nisteret_calc

    def calculet_age(self, year_of_birth, bd_month):
        age = int(self.this_year - year_of_birth)
        if bd_month > int(self.this_month):
            age -= 1
        return age

    #הערה - להוסיף שנת לידה וחודש לידה ולשלוף אותם






    #def shana_ishit(self):
        # if p_month < 7:
        #     shana_ishit = int(p_day + p_month + self.this_year)
        # else:
        #     shana_ishit = int(p_day + p_month + self.this_year + 1)
        #
        # if p_month < self.this_month:
        #     shana_ishit -= 1
        # print(shana_ishit)

