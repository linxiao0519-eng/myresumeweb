from flask import Flask, render_template

app = Flask(__name__)

# 1. 首頁：基本資料
@app.route("/")
def index():
    return render_template("index.html")

# 2. 興趣何倫碼
@app.route("/holland")
def holland():
    return render_template("holland.html")

# 3. 自傳履歷
@app.route("/resume")
def resume():
    return render_template("resume.html")

# 4. 相關工作
@app.route("/work")
def work():
    return render_template("work.html")

# 5. 相關連結
@app.route("/link")
def link():
    return render_template("link.html")

@app.route("/vocab_tool")
def vocab_tool():
    return render_template("vocab_tool.html")

@app.route("/job_backend")
def job_backend():
    return render_template("job_backend.html")

@app.route("/job_db")
def job_db():
    return render_template("job_db.html")

@app.route("/job_game")
def job_game():
    return render_template("job_game.html")

# --- Vercel 部署關鍵修正 ---
# 確保這行在最外面，讓 Vercel 抓到 app 物件
app = app 

# 本地端測試依然可用
if __name__ == "__main__":
    app.run(debug=True)