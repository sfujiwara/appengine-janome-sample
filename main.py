# -*- coding: utf-8 -*-

import os
import flask
from janome.tokenizer import Tokenizer


app = flask.Flask(__name__)
app.config.update(
    DEBUG=False,
    JSON_AS_ASCII=False,
)

TOKENIZER = Tokenizer(udic=os.environ["USER_DICTIONARY"])


def token_to_dict(token):
    result = {
        "surface": token.surface,
        "part_of_speach": token.part_of_speech.split(","),
        "infl_type": token.infl_type,
        "infl_form": token.infl_form,
        "base_form": token.base_form,
        "reading": token.reading,
        "phonetic": token.phonetic,
        "node_type": token.node_type
    }
    return result


@app.route("/", methods=["GET", "POST"])
def main_page():
    text = flask.request.args.get("text")
    return flask.jsonify({"tokens": [token_to_dict(t) for t in TOKENIZER.tokenize(text)]})
