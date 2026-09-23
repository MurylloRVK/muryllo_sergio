from flask import flask, render_templete, request request

app = flask(__name__,
            templete_folder="HTML",)
            statisc_folder="STATIC")
@app.route("/")

if __name__ == "__main__":
    app.run(debug=True)