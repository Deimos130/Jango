from django.db import models

# Create your models here.


GENDER = (
    ('M','MALE'),
    ('F','FEMALE')
)

class Students(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    student = models.CharField(max_length=20)
    genger = models.CharField(max_length=1,choices=GENDER)
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='image/%d:%m:%Y',blank=True)
    def __str__(self):
        return f'{self.title} {self.student} {self.date}'
    

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = verbose_name+'и'

class Comment(models.Model):
    email = models.EmailField(max_length=50) 
    name = models.CharField(max_length=20)       
    text_comment = models.TextField(max_length=200)
    post = models.ForeignKey(Students,on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.name},{self.post}'
    
    class Meta:
        verbose_name_plural = 'Комментарий'