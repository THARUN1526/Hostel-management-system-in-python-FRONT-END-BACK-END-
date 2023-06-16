from django.db import models

# Create your models here.

class Hostel(models.Model):
    hostel_name = models.CharField(max_length=30,primary_key=True)
    no_of_rooms = models.IntegerField()
    no_of_students = models.IntegerField()

    def __str__(self):
        return self.hostel_name

class Room(models.Model):
    hostel = models.ForeignKey(Hostel,related_name="hostel_room", on_delete=models.CASCADE)
    room_name = models.CharField(max_length=10,primary_key=True)
    capacity = models.IntegerField()
    room_fees = models.IntegerField()

    def __str__(self):
        return self.room_name

class Mess(models.Model):
    mess_name = models.CharField(max_length = 13)
    mess_fees = models.IntegerField()

    def __str__(self):
        return self.mess_name

class Student(models.Model):
    hostel = models.ForeignKey(Hostel,related_name="hostel_students", on_delete=models.CASCADE)
    room = models.ForeignKey(Room,related_name="room_students", on_delete=models.CASCADE)
    mess = models.ForeignKey(Mess,related_name="mess_students", on_delete=models.CASCADE)
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length = 30)
    student_branch = models.CharField(max_length = 30)
    student_phone = models.IntegerField()
    student_age = models.IntegerField()
    address_area = models.CharField(max_length = 100)
    address_city = models.CharField(max_length = 40)
    address_state = models.CharField(max_length = 40)
    medical_status = models.CharField(max_length = 300)
    def __str__(self):
        return self.student_name

class Fees(models.Model):
    student = models.ForeignKey(Student,related_name = "student_fees", on_delete=models.CASCADE)
    fees_status = models.CharField(max_length=10)

    def __str__(self):
        return self.student.student_name

class Staff(models.Model):
    hostel = models.ForeignKey(Hostel,related_name="hostel_staff",on_delete=models.CASCADE)
    staff_id = models.IntegerField(primary_key=True)
    staff_name = models.CharField(max_length=30)
    staff_duty = models.CharField(max_length=30)

    def __str__(self):
        return self.staff_name

class Parents(models.Model):
    student = models.ForeignKey(Student,related_name="student_parents",on_delete=models.CASCADE)
    father_name = models.CharField(max_length = 30)
    mother_name = models.CharField(max_length = 30)
    father_phone = models.IntegerField()
    mother_phone = models.IntegerField()

    def __str__(self):
        return self.student.student_name

class Visitors(models.Model):
    student = models.ForeignKey(Student,related_name="student_visitors",on_delete=models.CASCADE)
    out_time = models.DateTimeField()
    in_time = models.DateTimeField()
    visitor_phone = models.IntegerField()
    visitor_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.visitor_name
