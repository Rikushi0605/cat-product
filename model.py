from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf

# モデルロード（起動時に一度だけ呼ぶ想定）
model = load_model("cat_emotion_model.h5")
CLASS_NAMES = ['angry', 'sad', 'happy']

def predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    
    pred = model.predict(img_array)[0]
    pred_label = CLASS_NAMES[np.argmax(pred)]
    pred_score = np.max(pred)
    return pred_label, pred_score
