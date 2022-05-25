from django.db import models

import requests
import fake_useragent
import json


class Data:
    def __init__(self):

        url = 'https://darebee.com/media/com_jamegafilter/en_gb/1.json'   #config.URL_WORKOUT
        headers = {'user-agent' : fake_useragent.UserAgent().random}
        data = json.loads(requests.get(url=url, headers=headers).text)

        for key in data:
            data[key]['thumbnail'] = str.split(('https://darebee.com/' + data[key]['thumbnail']), '#')[0]

        workouts = []
        for item in data:
            try:
                data[item]['attr']["ct10"]["value"].append('all')
                workout = {
                    'name' : data[item]['name'],
                    'focus' : ', '.join(data[item]['attr']["ct10"]["value"]),
                    'types' : ', '.join(data[item]['attr']['ct16']['value'])+', all',
                    'difficult' : ', '.join(data[item]['attr']['ct14']['value'])+', all',
                    'equirment' : ', '.join(data[item]['attr']['ct19']['value'])+', all',
                    'icon' : data[item]['thumbnail'],
                    'img' : data[item]['thumbnail'].replace('-intro.jpg', '.jpg'),
                    'muscles' : data[item]['thumbnail'].replace('/workouts', '/workouts/muscles').replace('-intro.jpg', '.jpg'),
                    }
                workouts.append(workout)
            except:
                continue
        
        self.data = workouts


class Workout(models.Model):
    name = models.CharField('name', max_length=100)
    focus = models.CharField('focus', max_length=50)
    types = models.CharField('type', max_length=50)
    difficult = models.CharField('difficult', max_length=20)
    equirment = models.CharField('equirement', max_length=50)
    icon = models.CharField('img intro', max_length=200)
    img = models.CharField('img link', max_length=200)
    muscles = models.CharField('img muscles', max_length=200)

    @classmethod
    def set_data(cls, data):
        names =[i.name for i in cls.objects.all()]
        for item in data:
            if item['name'] not in names:
                cls.objects.create(**item)
















