from django.db import models
import json
import requests
import fake_useragent


class Focus(models.Model):
    '''1: full-body, 2: upper-body, 3: lower-body, 4: abs'''
    name = models.CharField('focus name', max_length=15)


class Types(models.Model):
    '''1: yoga, 2: hiit, 3: stretching, 4: wellness, 5: strength, 6: cardio, 7: combat'''
    name = models.CharField('types name', max_length=15)


class Difficult(models.Model):
    '''1: light, 2: easy, 3: normal, 4: hard, 5: advanced'''
    name = models.CharField('difficult name', max_length=15)


class Equirment(models.Model):
    '''1: none, 2: dumbbells, 3: bar, 4: other'''
    name = models.CharField('equirment name', max_length=15)


class Workout(models.Model):
    '''
    focus:\n
    2: full-body, 3: upper-body, 4: lower-body, 5: abs\n
    types:
    2: yoga, 3: hiit, 4: stretching, 5: wellness, 6: strength, 7: cardio, 8: combat\n
    difficult:
    2: light, 3: easy, 4: normal, 5: hard, 6: advanced\n
    equirment:\n
    2: none, 3: dumbbells, 4: bar, 5: other
    '''
    name = models.CharField('name', max_length=100)
    icon = models.CharField('img intro', max_length=200)
    img = models.CharField('img link', max_length=200)
    muscles = models.CharField('img muscles', max_length=200)
    focus = models.ManyToManyField(Focus, default='all')
    types = models.ManyToManyField(Types, default='all')
    difficult = models.ManyToManyField(Difficult, default='all')
    equirment = models.ManyToManyField(Equirment, default='all')


class Walk(models.Model):
    difficult = models.CharField(max_length=10)
    distance = models.IntegerField()
    route = models.JSONField()
    



class Data:
    def __init__(self) -> None:

        url = 'https://darebee.com/media/com_jamegafilter/en_gb/1.json'
        headers = {'user-agent' : fake_useragent.UserAgent().random}
        data = json.loads(requests.get(url=url, headers=headers).text)
        for key in data:
                data[key]['thumbnail'] = str.split(('https://darebee.com/' + data[key]['thumbnail']), '#')[0]

        workouts = []
        names=[]

        for item in data:
            try:

                workout = {
                    'name' : data[item]['name'],
                    'icon' : data[item]['thumbnail'],
                    'img' : data[item]['thumbnail'].replace('-intro.jpg', '.jpg'),
                    'muscles' : data[item]['thumbnail'].replace('/workouts', '/workouts/muscles').replace('-intro.jpg', '.jpg'),
                    'focus' : data[item]['attr']["ct10"]["value"],
                    'types' : data[item]['attr']['ct16']['value'],
                    'difficult' : data[item]['attr']['ct14']['value'],
                    'equirment' : data[item]['attr']['ct19']['value'],
                    }
                
                name_id = {
                    'name' : data[item]['name'],
                    'icon' : data[item]['thumbnail'],
                    'img' : data[item]['thumbnail'].replace('-intro.jpg', '.jpg'),
                    'muscles' : data[item]['thumbnail'].replace('/workouts', '/workouts/muscles').replace('-intro.jpg', '.jpg'),
                }

                workouts.append(workout)
                names.append(name_id)
            except:
                continue
        
        self.data = workouts
        self.names = names



def get_rout():
    with open('./cache/base_1500.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in data:
        Walk.objects.create(**i)

    with open('./cache/base_1500.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in data:
        Walk.objects.create(**i)

    with open('./cache/base_3000.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for i in data:
        Walk.objects.create(**i)
'''==================================================='''







