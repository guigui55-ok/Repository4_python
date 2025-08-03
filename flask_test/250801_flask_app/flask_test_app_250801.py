from flask import Flask, request, jsonify

app = Flask(__name__)

# サンプルエンドポイント一覧
AVAILABLE_ENDPOINTS = [
    "/test",
    "/endpoints",
    "/echo"
]


@app.route("/test", methods=["GET"])
def test_endpoint():
    """
    アクセステスト用エンドポイント
    """
    try:
        return jsonify({"message": "API接続成功"}), 200
    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500


@app.route("/endpoints", methods=["GET"])
def list_endpoints():
    """
    提供されているエンドポイント一覧を返す
    """
    try:
        return jsonify({"endpoints": AVAILABLE_ENDPOINTS}), 200
    except Exception as e:
        return jsonify({"error": True, "message": f"エンドポイント一覧取得に失敗しました: {str(e)}"}), 500


@app.route("/echo", methods=["POST"])
def echo_data():
    """
    受け取ったJSONデータをそのまま返す
    """
    try:
        if not request.is_json:
            return jsonify({"error": True, "message": "不正なJSON形式です"}), 400
        
        data = request.get_json()
        return jsonify({"received_data": data}), 200
    except Exception as e:
        return jsonify({"error": True, "message": str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """
    存在しないエンドポイントにアクセスした場合のエラーハンドリング
    """
    return jsonify({"error": True, "message": "エンドポイントが見つかりません"}), 404

from flask import render_template

@app.route("/", methods=["GET"])
def home_page():
    return render_template("index.html")

if __name__ == "__main__":
    # Flaskアプリ起動
    # デバッグモード有効化（開発用）
    app.run(host="0.0.0.0", port=5000, debug=True)
