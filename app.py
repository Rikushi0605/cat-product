from flask import Flask, render_template, request
import os
from recommender import recommend_cats
from model import predict
from predict_cat_emotion import predict_emotion

app = Flask(__name__)

UPLOAD_FOLDER = './static/dog_image'
app.config['UPLOAD_FOLDER'] = 'static/dog_image'

# ホームページ（ポータル）
@app.route('/')
def home():
    return render_template('home.html')

# 猫種診断フォーム
@app.route('/recommend')
def recommend():
    return render_template('index.html')

# 猫種診断結果
@app.route('/result', methods=['POST'])
def result():
    user_input = {
        'personality': request.form.get('personality'),
        'environment': request.form.get('environment'),
        'lifestyle': request.form.get('lifestyle'),
        'experience': request.form.get('experience'),
        'grooming': request.form.get('grooming'),
        'allergy': request.form.get('allergy')
    }

    recommended_cats = recommend_cats(user_input)
    return render_template('result.html', cats=recommended_cats, user_tags=user_input)

# 画像アップロードページ（GET）
@app.route("/analyze")
def analyze():
    return render_template("analyze.html")

# アップロードされた画像の処理（POST）
@app.route("/upload", methods=["POST"])
def upload():
    if "upload_file" not in request.files:
        return "ファイルがありません"

    file = request.files["upload_file"]
    if file.filename == "":
        return "ファイルが選択されていません"

    # ファイルの保存
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # 感情予測
    result, score = predict_emotion(filepath)
    img_path = "/" + filepath  # HTMLで表示するためにURL形式に

    return render_template("emotion_result.html", result=result, score=score, img_path=img_path)
if __name__ == '__main__':
    app.run(debug=True)
