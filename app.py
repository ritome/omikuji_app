from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__, static_url_path="/static")

# おみくじ結果と対応する動画、メッセージの設定
omikuji_results = {
    "大吉": {
        "video": "videos/daikichi_animation.mp4",
        "message": "今日のあなたは最高の運勢！新しいことに挑戦すると素敵な結果が待っていますよ。",
    },
    "吉": {
        "video": "videos/kichi_animation.mp4",
        "message": "今日は全体的に順調です。小さな幸せを見つけることができそうです。",
    },
    "中吉": {
        "video": "videos/chukichi_animation.mp4",
        "message": "良いことが起こりそうな予感！でも、焦らずゆっくり進みましょう。",
    },
    "小吉": {"video": "videos/shoukichi_animation.mp4", "message": "少しずつ前進している感じ。謙虚さを忘れずに。"},
    "末吉": {
        "video": "videos/suekichi_animation.mp4",
        "message": "ちょっとした困難があるかもしれませんが、最後には良い方向に向かいます。",
    },
    "凶": {
        "video": "videos/kyou_animation.mp4",
        "message": "注意が必要な一日。無理をせず、リラックスして過ごしましょう。",
    },
}


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/omikuji", methods=["POST"])
def omikuji():
    # おみくじの結果をランダムに選択
    result = random.choice(list(omikuji_results.keys()))
    return render_template(
        "omikuji.html",
        result=result,
        video=omikuji_results[result]["video"],
        message=omikuji_results[result]["message"],
    )


if __name__ == "__main__":
    app.run(debug=True)
