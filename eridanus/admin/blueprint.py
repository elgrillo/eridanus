from flask import Blueprint, make_response, render_template, session
from StringIO import StringIO
from zipfile import ZipFile
from .services import ExportDataService


admin = Blueprint('admin', __name__, template_folder='templates')


def _zip(file, data_streams):
    zip = ZipFile(file, 'a')
    for key in data_streams:
        filename = key + '.csv'
        zip.writestr(filename, data_streams[key])
    for f in zip.filelist:
        f.create_system = 0
    zip.close()
    file.seek(0)
    return file


def _zip_in_memory(data_streams):
    file = StringIO()
    return _zip(file, data_streams)


@admin.route('/', methods=['GET'])
def index():
        return render_template('admin/home.html')


@admin.route('/export/<format>/', methods=['GET'])
def export(format):
    service = ExportDataService()
    username = session['nickname']
    data = {}
    data['run'] = service.get_run_data(format, username)
    data['weight'] = service.get_weight_data(format, username)
    zip_stream = _zip_in_memory(data)
    response = make_response(zip_stream.read())
    response.headers["Content-Disposition"] = 'attachment;' \
        + 'filename=eridanus_data.zip'
    response.headers['Cache-Control'] = 'no-cache'
    response.headers['Content-Type'] = 'application/zip'
    # in_memory.seek(0)    
    # response.write(in_memory.read()) #?
    return response


@admin.route('/import/', methods=['GET'])
def import_index():
    return NotImplemented
