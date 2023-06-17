class Student:
    def __init__(self, student_id, first_name, last_name, gpa):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.gpa = gpa

    def is_conditional(self):
        if self.gpa < 2.0:
            return True
        else:
            return False
#در این کلاس، هر دانشجو با استفاده از شماره دانشجویی، نام، نام خانوادگی و معدل خود ساخته می‌شود. همچنین، با استفاده از تابع `is_conditional` بررسی می‌شود که آیا دانشجو مشروط شده است یا نه. اگر معدل دانشجو کمتر از ۲ باشد، به عنوان یک دانشجوی مشروط در نظر گرفته می‌شود.

#برای استفاده از این کلاس و بررسی وضعیت دانشجو، به صورت زیر عمل کنید:
      
 
# ساخت چند نمونه از کلاس Student
student1 = Student(1234, "John", "Doe", 3.5)
student2 = Student(5678, "Jane", "Smith", 1.8)

# بررسی وضعیت دانشجو
if student1.is_conditional():
    print(f"{student1.first_name} {student1.last_name} is on academic probation.")
else:
    print(f"{student1.first_name} {student1.last_name} is in good academic standing.")

if student2.is_conditional():
    print(f"{student2.first_name} {student2.last_name} is on academic probation.")
else:
    print(f"{student2.first_name} {student2.last_name} is in good academic standing.")
    
# در این مثال، دو نمونه از کلاس Student ساخته شد سپس با استفاده از تابع `is_conditional` بررسی می‌شود که هر دانشجو مشروط شده است یا نه و در نهایت وضعیت آن‌ها چاپ می‌شود.   
