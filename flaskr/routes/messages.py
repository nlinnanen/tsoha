from flaskr import app
from ..db.messages import create_message, update_message, delete_message
from flask import render_template, request, session

from flaskr.db import messages

@app.route("/conversations/<id>/messages", methods=["POST"])
def create_message(id):
    conversation_id = id
    message = request.form["message"]
    sender_id = session["user_id"]
    created_message = messages.create_message(message, conversation_id, sender_id)
    return render_template("message.html", message=created_message)


@app.route("/messages/<id>", methods=["PUT"])
def update_message(id):
    message = request.form["message"]
    updated_message = messages.update_message(id, message)
    return render_template("message.html", message=updated_message)

@app.route("/messages/<id>", methods=["DELETE"])
def delete_message(id):
    messages.delete_message(id)
    return ""
    # return render_template("info.html", info="Successfully deleted message")
