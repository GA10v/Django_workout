from django.db import models
import json
import requests
import fake_useragent

# Create your models here.
class Focus(models.Model):
    '''1: full-body, 2: upper-body, 3: lower-body, 4: abs'''
    name = models.CharField('focus name', max_length=15, null=True)
    def __str__(self):
        return self.name.upper()


class Types(models.Model):
    '''1: yoga, 2: hiit, 3: stretching, 4: wellness, 5: strength, 6: cardio, 7: combat'''
    name = models.CharField('types name', max_length=15, null=True)
    def __str__(self):
        return self.name.upper()


class Difficult(models.Model):
    '''1: light, 2: easy, 3: normal, 4: hard, 5: advanced'''
    name = models.CharField('difficult name', max_length=15, null=True)
    def __str__(self):
        return self.name.upper()


class Equirment(models.Model):
    '''1: none, 2: dumbbells, 3: bar, 4: other'''
    name = models.CharField('equirment name', max_length=15, null=True)
    def __str__(self):
        return self.name.upper()


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
    name = models.CharField('name', max_length=100, null=True)
    icon = models.CharField('img intro', max_length=200, null=True)
    img = models.CharField('img link', max_length=200, null=True)
    muscles = models.CharField('img muscles', max_length=200, null=True)
    focus = models.ManyToManyField(Focus, default='all')
    types = models.ManyToManyField(Types, default='all')
    difficult = models.ManyToManyField(Difficult, default='all')
    equirment = models.ManyToManyField(Equirment, default='all')


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


def get_workout():
    data = Data()
    n=[]
    c=1
    for i in data.names:
        if i['name'] not in n:
            Workout.objects.create(id=c,name=i['name'],icon=i['icon'],img=i['img'],muscles=i['muscles'])
            c+=1
            n.append(i['name'])
        else:
            continue


def get_ftde():
    f=["all","full-body","upper-body","lower-body","abs"]
    t=["all","yoga","hiit","stretching","wellness","strength","cardio","combat"]
    d=["all","light","easy","normal","hard","advanced"]
    e=["all","none","dumbbells","bar","other"]

    c=1
    for i in f:
        Focus.objects.create(name=i, id=c)
        c+=1

    c=1
    for i in t:
        Types.objects.create(name=i, id=c)
        c+=1

    c=1
    for i in d:
        Difficult.objects.create(name=i, id=c)
        c+=1

    c=1
    for i in e:
        Equirment.objects.create(name=i, id=c)
        c+=1


def get_m2m():
    f_all=Focus.objects.get(name='all')
    f_full=Focus.objects.get(name='full-body')
    f_upper=Focus.objects.get(name='upper-body')
    f_lower=Focus.objects.get(name='lower-body')
    f_abs=Focus.objects.get(name='abs')

    data=Data()
    for i in data.data:
        wk=Workout.objects.get(name=i['name'])
        for q in i['focus']:
            if q == 'all':
                f_all.workout_set.add(wk)
            elif q=='full-body':
                f_full.workout_set.add(wk)
            elif q=='upper-body':
                f_upper.workout_set.add(wk)
            elif q=='lower-body':
                f_lower.workout_set.add(wk)
            elif q=='abs':
                f_abs.workout_set.add(wk)

    '''============== M2M Types - Workout ======================================='''

    t_all=Types.objects.get(name='all')
    t_yoga=Types.objects.get(name='yoga')
    t_hiit=Types.objects.get(name='hiit')
    t_stretching=Types.objects.get(name='stretching')
    t_wellness=Types.objects.get(name='wellness')
    t_strength=Types.objects.get(name='strength')
    t_cardio=Types.objects.get(name='cardio')
    t_combat=Types.objects.get(name='combat')


    data=Data()
    for i in data.data:
        wk=Workout.objects.get(name=i['name'])
        for q in i['types']:
            if q == 'all':
                t_all.workout_set.add(wk)
            elif q=='yoga':
                t_yoga.workout_set.add(wk)
            elif q=='hiit':
                t_hiit.workout_set.add(wk)
            elif q=='stretching':
                t_stretching.workout_set.add(wk)
            elif q=='wellness':
                t_wellness.workout_set.add(wk)
            elif q=='strength':
                t_strength.workout_set.add(wk)
            elif q=='cardio':
                t_cardio.workout_set.add(wk)
            elif q=='combat':
                t_combat.workout_set.add(wk)

    '''============== M2M Difficult - Workout ======================================='''

    d_all=Difficult.objects.get(name='all')
    d_light=Difficult.objects.get(name='light')
    d_easy=Difficult.objects.get(name='easy')
    d_normal=Difficult.objects.get(name='normal')
    d_hard=Difficult.objects.get(name='hard')
    d_advanced=Difficult.objects.get(name='advanced')


    data=Data()
    for i in data.data:
        wk=Workout.objects.get(name=i['name'])
        for q in i['difficult']:
            if q == 'all':
                d_all.workout_set.add(wk)
            elif q=='light':
                d_light.workout_set.add(wk)
            elif q=='easy':
                d_easy.workout_set.add(wk)
            elif q=='normal':
                d_normal.workout_set.add(wk)
            elif q=='hard':
                d_hard.workout_set.add(wk)
            elif q=='advanced':
                d_advanced.workout_set.add(wk)

    '''============== M2M Equirment - Workout ======================================='''

    e_all=Equirment.objects.get(name='all')
    e_none=Equirment.objects.get(name='none')
    e_dumbbells=Equirment.objects.get(name='dumbbells')
    e_bar=Equirment.objects.get(name='bar')
    e_other=Equirment.objects.get(name='other')


    data=Data()
    for i in data.data:
        wk=Workout.objects.get(name=i['name'])
        for q in i['equirment']:
            if q == 'all':
                e_all.workout_set.add(wk)
            elif q=='none':
                e_none.workout_set.add(wk)
            elif q=='dumbbells':
                e_dumbbells.workout_set.add(wk)
            elif q=='bar':
                e_bar.workout_set.add(wk)
            elif q=='other':
                e_other.workout_set.add(wk)