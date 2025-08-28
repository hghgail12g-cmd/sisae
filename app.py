from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

# اختبار بسيط عشان تشوف إن السيرفر شغال
@app.route("/ping")
def ping():
    return jsonify({"message": "pong"})

# عرض نسخة الموقع (HTML) من نفس المجلد
@app.route("/")
def index():
    return send_from_directory(".", "index_desktop.html")  # غير index.html لاسم ملف موقعك

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
