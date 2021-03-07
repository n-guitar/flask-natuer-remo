import os

from flask import Flask, render_template, request

from api.json_dataclient import AppliancesDataClient
from air_controller import air_controller
from other_controller import other_controller
from tv_controller import tv_controller

app = Flask(__name__)
app.register_blueprint(air_controller)
app.register_blueprint(other_controller)
app.register_blueprint(tv_controller)

UPLOAD_FOLDER = './static/images/'
ALLOWED_EXTENSIONS = set(['.jpg','.jpeg'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# limit upload file size : 1MB
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
app.config.from_object(__name__)

@app.route('/')
def top():
    image_path = "./static/images"
    files = os.listdir(image_path)
    # If a file other than default.jpg exists, display image.jpg.
    if len(files) > 1:
        files.remove("default.jpg")
    image_list = list(map(lambda image: "images/" + image, files))
    return render_template('top.html', image_list=image_list)


@app.route('/air')
def air():
    appliances_air = appliances_client.appliances_get_air()
    return render_template('air.html', appliances_air=appliances_air)


@app.route('/tv')
def tv():
    appliances_tv = appliances_client.appliances_get_tv()
    return render_template('tv.html', appliances_tv=appliances_tv)


@app.route('/other')
def other():
    appliances_other = appliances_client.appliances_get_other()
    return render_template('other.html', appliances_other=appliances_other)


@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        img_file = request.files['img_file']
        print(img_file)
        _, ext = os.path.splitext(img_file.filename)
        ext = ext.lower()
        print(ext)
        if ext and ext in ALLOWED_EXTENSIONS:
            img_file.filename = "image.jpg"
            img_url = os.path.join(app.config['UPLOAD_FOLDER'], img_file.filename)
            img_file.save(img_url)
            appliances_get_all = appliances_client.appliances_get_all()
            return render_template('settings.html', appliances_get_all=appliances_get_all,result="Uploaded")
        else:
            appliances_get_all = appliances_client.appliances_get_all()
            return render_template('settings.html', appliances_get_all=appliances_get_all,result="Sony ... {} is not supported. Supports jpeg/jpg".format(ext))
    else:
        appliances_get_all = appliances_client.appliances_get_all()
        return render_template('settings.html', appliances_get_all=appliances_get_all)


if __name__ == "__main__":
    appliances_client = AppliancesDataClient()
    appliances_client.json_save()
    appliances_client.json_load()
    app.run(host='0.0.0.0', port=5000, debug=True)
