from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self,*args,**option):
        print(""" What do you want to Know about the developer ?
            1.Name      2.Educational Level       3.Projects   4. Hobbies """)
    
    
        about_me = {'Name':"Bernabas Tekkalign Buli (BARNAAN).",'Educational Level':'BA degree Student',
                'Projects':'Movie Booking Webiste, Hotel Booking Website, Bus Booking Website and soon you can find all of the in my github  @Barnaan2',
                'Hobbies':'Sleeping , walking and Coding'}
        query = {
        1:'Name',2:'Educational Level',3:'Projects ',4:'Hobbies'
    }
        choosed = int(input(': '))
        choosed_output = ''
        try:
            choosed_output = about_me[query[choosed]]
        except:
            choosed_output = "Please check your Input"
    
        print(choosed_output)