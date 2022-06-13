from random import randint
from fpdf import FPDF
class Cv_template1 (FPDF):

    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_left_margin(10)
        self.set_right_margin(10)
    
    def reset_margin(self):
        self.set_left_margin(10)
        self.set_right_margin(10)

    def add_picture(self, path):
        top_left_x, top_left_y = 0, 0
        with self.round_clip(x=top_left_x + 12, y=top_left_y + 2, r=38):
            self.image(  path, 10, 0, 60)
    
    def add_name_title(self, name, title):
        self.set_draw_color(r=0, g=0, b=0)
        self.set_line_width(1.5)
        self.set_font("helvetica", "B", 20)
        self.cell(50)
        self.cell(0, 0, name, border=0,)
        self.set_font("helvetica", size =15)
        self.ln(10)
        self.cell(50)
        self.cell(0, 0, title, border=0,)
        self.line(x1=55, y1=30, x2=200, y2=30)
        self.ln(20)
    
    def add_contact(self, contacts):
        self.set_right_margin(40)
        self.set_font("helvetica", "B", size=15)
        self.set_y(50)
        self.cell(0, 5, "Contact:", new_x="LMARGIN", new_y="NEXT")
        self.set_line_width(0.5)
        self.line(x1=10, y1=55, x2=50, y2=55)
        for contact in contacts:
            self.set_left_margin(10)
            self.set_font("helvetica", "B", size=12)
            self.cell(2)
            self.cell(0, 5, contact[0] + " :", new_x="LMARGIN", new_y="NEXT")
            self.set_font("helvetica", size=10)
            self.set_left_margin(13)
            self.write( txt = contact[1])
            self.ln(3)
        self.reset_margin()
    
    def add_list(self, parent, childs):
        self.set_font("helvetica", "B", size=12)
        self.ln(10)
        self.cell(0, 5, parent + ":", new_x="LMARGIN", new_y="NEXT")
        self.line(x1=10, y1=self.get_y(), x2=50, y2=self.get_y())
        self.set_font("helvetica", size=10)
        self.ln(2)
        for child in childs:
            self.cell(2)
            self.cell(0, 5, child, new_x="LMARGIN", new_y="NEXT")
    
    def second_column(self):
        self.set_y(40)
        self.set_left_margin(70)

    def add_summary(self, summary):
        self.set_font("helvetica", "B", size=15)
        self.cell(10, 10, "Summary: ", new_x="LMARGIN", new_y="NEXT")
        self.line(x1=70, y1=self.get_y(), x2=200, y2=self.get_y())
        self.ln(3)
        self.set_font("helvetica", size=12)
        self.write( txt = summary)
        self.ln(10)

    def add_education(self, educations):
        self.set_font("helvetica", "B", size=15)
        self.cell(10, 10, "Education: ", new_x="LMARGIN", new_y="NEXT")
        self.line(x1=70, y1=self.get_y(), x2=200, y2=self.get_y())
        self.ln(3)
        self.set_font("helvetica", size=12)
        self.set_left_margin(75)
        for education in educations:
            self.write( txt = education)
            self.ln(5)
        self.ln(5)
        self.set_left_margin(70)
    
    def add_experience(self, experiences):
        if experiences == None:
            return None
        self.set_font("helvetica", "B", size=15)
        self.cell(10, 10, "Experience: ", new_x="LMARGIN", new_y="NEXT")
        self.line(x1=70, y1=self.get_y(), x2=200, y2=self.get_y())
        self.ln(3)
        self.set_font("helvetica", size=12)
        self.set_left_margin(75)
        for experience in experiences:
            self.write( txt = experience)
            self.ln(8)
        self.ln(5)
        self.set_left_margin(70)
    
    def add_paragraph( self, title, paragraph):
        self.set_font("helvetica", "B", size=15)
        self.cell(10, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.line(x1=70, y1=self.get_y(), x2=200, y2=self.get_y())
        self.ln(3)
        self.set_font("helvetica", size=12)
        self.write( txt = paragraph)
        self.ln(10)
        self.set_left_margin(70)


if __name__ == "__main__":
    from faker import Faker
    import random
    import csv
    import datetime

    fake = Faker('id_ID')
    fake_eng = Faker()
    csv_reader = list()
    with open('./skillset_list.csv') as csv_file:
            csv_reader =list( csv.reader(csv_file, delimiter=','))
            # print(type(csv_reader))
    
    for i in range(5):
        cv = Cv_template1()

        # year = random.randint(1980, 2006)
        name = fake.name()
        cv.add_picture("https://source.unsplash.com/random")
        cv.add_name_title(name,fake.bs())

        contacts = [['email',  name.replace(' ', '.')[:10]+str(random.randint(0,1000))+"@"+fake.free_email_domain()], 
                    ['phone', fake.phone_number()],
                    ['address', fake.address()],
                    ]
        cv.add_contact(contacts)

        list_name1, list_name2, = "General Skill", str()
        list_content1, list_content2 = list(), list()

        num_skill = random.randint(4,9)
        list_content1 = random.sample(csv_reader[0][1:], num_skill)
        cv.add_list(list_name1, list_content1)

        spc_skil = random.choice(csv_reader[1:])
        spc_skil = [i for i in spc_skil if not i == '']
        num_skill = random.randint(4,8)
        list_name2 = spc_skil[0]
        list_content2 = random.sample(spc_skil[1:], num_skill)
        cv.add_list(list_name2, list_content2)

        cv.second_column()

        paragraphs = fake_eng.paragraph(nb_sentences=5)
        par_string = str()
        for x in paragraphs: par_string += x
        cv.add_summary(par_string)

        cv.add_paragraph("motto",  fake.catch_phrase())

        educations = list()
        now =datetime.datetime.now().year
        year =now - random.randint(10, 20)
        for j in range(0, random.randint(1,3)):
            school = "university of "+ fake.city()+' ('+str(year)+'-'
            year += random.randint(2,5)
            school +=str(year)+')'
            if year >= now -3 :
                break
            educations.append(school)
        cv.add_education(educations)

        experiences = list()
        year += random.randint(-3,3)
        for j in range(0, random.randint(1, 5)):
            experience = fake.job() + " ," + fake.company() +' ('+str(year)+'-'
            year += random.randint(2,5)
            if year >= now  :
                experience +=str(now)+')'
                experiences.append(experience)
                break
            experience +=str(year)+')'
            experiences.append(experience)
        cv.add_experience(experiences)





        # print(i)
        
        cv.output(f"./pdf/classGenerated{i}.pdf")

