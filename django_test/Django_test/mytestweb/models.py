from django.db import models

# 部門表
class Department(models.Model):
    depart_name = models.CharField(verbose_name="Department Name", max_length=32)
    depart_member = models.IntegerField(verbose_name="Department Member")

# Django ORM (Object Relational Mapping) create table UserInfo
# 員工表
class UserInfo(models.Model):
    name = models.CharField(verbose_name="Empolyee Name", max_length=32)
    password = models.CharField(verbose_name="Password", max_length=64)
    age = models.IntegerField(verbose_name="Age")
    account = models.DecimalField(verbose_name="Account", max_digits=10, decimal_places=2, default=0)

    # 設定資料庫資料為1=Male, 2=Female
    gender_choices = ((1, "Male"),(2, "Female"))
    gender = models.SmallIntegerField(verbose_name="Gender", choices=gender_choices)


    # Department表與UserInfo表建立關聯
    # 約束 
    # - to -> 那個表做關聯
    # - to_field -> 那個欄位做關聯
    # - on_delete=models.CASCADE -> 當有關聯的資料被刪除時連同有關聯的表資料會一起刪除
    # depart_foreignkey = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE)

# SQL command query to create table UserInfo
# create table UserInfo(
#     id int primary key auto_increment,
#     name varchar(32),
#     password varchar(64),
#     age int
# );
    


