# predict_cat_emotion.py

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import tensorflow as tf

# モデルとクラスの読み込み（最初に1回だけ）
CLASS_NAMES = ['angry', 'sad', 'happy']
model = load_model("cat_emotion_model.h5")

def predict_emotion(img_path):
    try:
        # 画像の読み込みと前処理
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

        # 予測
        pred = model.predict(img_array)[0]
        result = CLASS_NAMES[np.argmax(pred)]
        score = round(100 * np.max(pred), 2)  # 信頼度％

        return result, score
    except Exception as e:
        print("予測中にエラーが発生しました:", e)
        return "不明", 0
