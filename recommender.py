from cat_data import cat_data

# ユーザーの入力をタグに変換するマッピング
tag_map = {
    'personality': {
        '穏やか': ['穏やか', '落ち着いている', '温厚'],
        '活発': ['活発', 'エネルギッシュ', '好奇心旺盛'],
        '甘えん坊': ['甘えん坊', '抱っこ好き'],
        '独立心が強い': ['独立心']
    },
    'environment': {
        'マンション': ['室内飼い', 'ペット可賃貸', 'マンション'],
        '一軒家': ['屋外飼い', '一軒家'],
        'ペット可賃貸': ['室内飼い', 'ペット可賃貸']
    },
    'lifestyle': {
        '在宅時間が長い': ['在宅時間が長い', '甘えん坊'],
        '外出が多い': ['独立心', '活発'],
        '子どもがいる': ['社交的', '友好的']
    },
    'experience': {
        '未経験(猫を飼ったことがない)': ['初心者向き'],
        '他の動物': ['他の動物と共存可'],  # 猫データにないなら削除も可
        '犬を飼ったことがある': ['犬を飼ったことがある']  # 猫データにないなら削除も可
    },
    "grooming": {
    "毎日でも構わない": ["長毛", "ブラッシング重視"],
    "週に数回程度": ["中程度のお手入れ", "短毛"],
    "なるべく手がかからない方がよい": ["短毛", "お手入れ簡単"]
    },
    'allergy': {
        'なし': [],
        'あり': ['アレルギー対応']
    }
}

def recommend_cats(user_input):
    # ユーザー入力からタグリスト作成
    user_tags = []
    for key, val in user_input.items():
        user_tags.extend(tag_map.get(key, {}).get(val, []))

    scored = []
    for cat in cat_data:
        score = sum(tag in cat['tags'] for tag in user_tags)
        scored.append((score, cat))

    scored.sort(key=lambda x: x[0], reverse=True)
    top3 = [cat for score, cat in scored[:3]]
    return top3
