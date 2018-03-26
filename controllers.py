from google.appengine.api import users
from flask import render_template, \
    make_response, session
from datetime import datetime
from zipfile import ZipFile
from StringIO import StringIO
from repository import RunRepository, WeightRepository

import csv


ERIDANUS_TIME_FORMAT = '%I:%M %p'
ERIDANUS_DATE_FORMAT = '%d %b %Y'


class AuthController(object):
    def __init__(self):
        self.nickname = None
        self.logout_url = None
        self._fetch_user_data()

    def _fetch_user_data(self):
        if not session.has_key('nickname'):
            user = users.get_current_user()
            if user:
                session['nickname'] = user.nickname()
                _auth_domain = None
                session['logout_url'] = users.create_logout_url('/', _auth_domain)

    @property
    def is_authenticated(self):
        return session['nickname'] is not None

    @property
    def is_authorized(self):
        return self.is_authenticated 

    def render_view(self, url, dict):
        if not self.is_authorized:
            return 'You''re not authorized to use this website. <a href="{}">Log out</a>'.format(session['logout_url'])
        render_template(url, vm=dict)

    def render_form_template(self, url, form=None):
        if not self.is_authorized:
            return 'You''re not authorized to use this website. <a href="{}">Log out</a>'.format(session['logout_url'])
        return render_template(url, form=form)


class AdminController(AuthController):

    def __init__(self):
        super(AdminController, self).__init__()
        
    def export(self):
        run_csv=self._build_run_csv()
        weight_csv=self._build_weight_csv()
        in_memory = StringIO()
        zip = ZipFile(in_memory, "a")
        zip.writestr("run.csv", run_csv)
        zip.writestr("weight.csv", weight_csv)
        # fix for Linux zip files read in Windows
        for file in zip.filelist:
            file.create_system = 0    
        zip.close()
        in_memory.seek(0) 
        response = make_response(in_memory.read())
        response.headers["Content-Disposition"] = "attachment; filename=eridanus_data.zip"
        response.headers['Cache-Control'] = 'no-cache'
        response.headers['Content-Type'] = 'application/zip'
        #in_memory.seek(0)    
        #response.write(in_memory.read()) #?
        return response


    def _build_run_csv(self):
        items = self._fetch_all_run()
        stream = StringIO()
        fieldnames = ['usernickname', 'activity_date', 'activity_time', 'time', 'distance', 'speed', 'calories', 'notes', 'creation_datetime']
        csvwriter = csv.DictWriter(stream, fieldnames=fieldnames, dialect='excel')
        csvwriter.writeheader()
        for item in items:
            csvwriter.writerow({
                'usernickname': item.usernickname, 
                'activity_date': self._get_activity_date(item),
                'activity_time': self._get_activity_time(item),
                'duration': self._get_duration(item),
                'distance': item.distance,
                'speed': item.speed,
                'calories': item.calories,
                'notes': item.notes,
                'creation_datetime': item.creation_datetime
                })
        return stream.getvalue()

    def _build_weight_csv(self):
        items = self._fetch_all_weights()
        
        stream = StringIO()
        csvwriter = csv.writer(stream, dialect='excel')
        fieldnames = ['usernickname', 'weight', 'creation_datetime']
        csvwriter = csv.DictWriter(stream, fieldnames=fieldnames, dialect='excel')
        csvwriter.writeheader()
        for item in items:
            csvwriter.writerow({
                'usernickname': item.usernickname, 
                'weight': item.weight,
                'creation_datetime': item.creation_datetime
                })
        return stream.getvalue()

    def _build_csv(self, items):
        pass

    def _fetch_all_run(self):
        repo = RunRepository()
        return repo.fetch_all()

    def _fetch_all_weights(self):
        repo = WeightRepository()
        return repo.fetch_all()

    def _get_activity_date(self, model):
        if model.activity_date:
            return model.activity_date
        else:
            return model.date

    def _get_activity_time(self, model):
        if model.activity_time:
            return model.activity_time
        else:
            return datetime.strptime(u'20:30', '%H:%M').time()

    def _get_duration(self, model):
        if model.duration:
            return model.duration
        else:
            return model.time

    def import_data(self):
        pass

    def index(self):
        return render_template('admin/home.html')
