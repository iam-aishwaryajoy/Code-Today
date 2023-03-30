from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from import_lib import *



class Model:
    def _init__(self):
        self.model = None

    def call_model(self):
        model_path = 'models/hypermodel.h5'
        self.model = load_model(model_path)
        print('HYPERMODEL loaded. Check http://127.0.0.1:5000/')

    def preprocess(self, img_path):
        img = cv2.imread(img_path)
        img = cv2.resize(img,(28,28),3)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = img.reshape((1,28,28))

        img = img.astype('float32')
        img = img / 255.0
        return img

    def predict(self, img):
        Labels = ["Top/Tshirt", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot", "None"]
        img = self.preprocess(img)
        preds = self.model.predict(img)
        if np.max(preds)< 0.5:
            result = Labels[10]
        else:
            preds = preds.argmax(axis=1)
            label = Labels[preds[0]]
            result = label
        return result

if __name__ == '__main__':
    app = Flask(__name__)
    model = Model()
    model.call_model()

    @app.route('/', methods=['GET'])
    def index():
        return render_template('index.html')


    @app.route('/predict', methods=['GET', 'POST'])
    def upload():
        if request.method == 'POST':
            f = request.files['file']

            basepath = os.path.dirname(__file__)
            file_path = os.path.join(
                basepath, 'uploads', secure_filename(f.filename))
            f.save(file_path)

            result = model.predict(file_path)

            return result
        return None

    app.run(debug=True)

