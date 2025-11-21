from flask import Flask, jsonify
from apkpure.apkpure import ApkPure

app = Flask(__name__)
api = ApkPure()

# قائمة التطبيقات التي تريد عرضها
APP_NAMES = ["PUBG Mobile", "Free Fire", "Snapchat", "Instagram", "WhatsApp"]

@app.route('/')
def home():
    return '✅ API جاهز'

@app.route('/api/apps')
def get_apps():
    apps_data = []
    for name in APP_NAMES:
        try:
            info = api.get_info(name=name)
            apps_data.append({
                'name': info.name,
                'package': info.package_name,
                'version': info.version,
                'size': info.size,
                'description': info.description,
                'image': info.icon,
                'download': info.download_url
            })
        except Exception as e:
            apps_data.append({
                'name': name,
                'error': str(e)
            })
    return jsonify(apps_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
