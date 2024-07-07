from django.db import models

# Django ORM (Object Relational Mapping) create table UserInfo
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(max_length=3)


# SQL command query to create table UserInfo
# create table UserInfo(
#     id int primary key auto_increment,
#     name varchar(32),
#     password varchar(64),
#     age int
# );
    
class Department(models.Model):
    depart_name = models.CharField(max_length=32)
    depart_menber = models.IntegerField(max_length=3)