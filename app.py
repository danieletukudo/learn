from flask import Flask, request,jsonify,url_for
import os
import gen
app = Flask(__name__)


# UPLOAD_FOLDER = os.path.join("static", "static")


@app.route("/market", methods = ["POST"])
def market():
    ques = request.form.get("text")

    result = gen.create_completion(ques)

    return result

if __name__ == "__main__":
    app.run(port=8080,debug=True)


