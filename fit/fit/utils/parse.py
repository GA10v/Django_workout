import json
import requests
import fake_useragent



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
                workout = {
                    'name' : data[item]['name'],
                    'focus' : ', '.join(data[item]['attr']["ct10"]["value"]),
                    'types' : ', '.join(data[item]['attr']['ct16']['value']),
                    'difficult' : ', '.join(data[item]['attr']['ct14']['value']),
                    'equirment' : ', '.join(data[item]['attr']['ct19']['value']),
                    'img_intro' : data[item]['thumbnail'],
                    'img' : data[item]['thumbnail'].replace('-intro.jpg', '.jpg'),
                    'muscles' : data[item]['thumbnail'].replace('/workouts', '/workouts/muscles').replace('-intro.jpg', '.jpg'),
                    }
                workouts.append(workout)
            except:
                continue
        
        self.data = workouts






