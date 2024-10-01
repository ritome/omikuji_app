from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__, static_url_path="/static")

# おみくじ結果と対応する動画、メッセージの設定
omikuji_results = {
    "大吉": {
        "video": "videos/daikichi_animation.mp4",
        "message": "今日はとってもラッキーですね。一日爽やかに過ごせるでしょう。",
    },
    "吉": {"video": "videos/kichi_animation.mp4", "message": "良いことがありそうです！"},
    "中吉": {"video": "videos/chukichi_animation.mp4", "message": "まあまあの一日になるでしょう。"},
    "小吉": {"video": "videos/shoukichi_animation.mp4", "message": "ちょっと良いことがあるかも？"},
    "末吉": {"video": "videos/suekichi_animation.mp4", "message": "あまり期待しすぎないように。"},
    "凶": {
        "video": "videos/kyou_animation.mp4",
        "message": "凶です。今日は少し注意が必要ですが、誰かに優しくするといいことあるかも?!",
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
