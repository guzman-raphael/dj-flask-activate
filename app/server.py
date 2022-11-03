from flask import Flask, request
import datajoint as dj
import os
import time
import imp
from functools import wraps

app = Flask(__name__)

def protected_route(function):
    @wraps(function)
    def wrapper(**kwargs):
        try:
            dj.conn(host=os.getenv("DJ_ROOT_HOST"),
                    user=request.args.get('user'),
                    password=request.args.get('password'),
                    reset=True)
            return function(**kwargs)
        except Exception as e:
            return str(e), 401

    wrapper.__name__ = function.__name__
    return wrapper

@app.route("/student")
@protected_route
def student():
    pipeline=imp.load_module(f"{request.args.get('prefix')}_pipeline",
                             *imp.find_module('pipeline'))
    pipeline.schema.activate(f"{request.args.get('prefix')}_university")
    print("--- imported ---", flush=True)
    # do stuff
    time.sleep(5)
    return dict(schema=str(pipeline.schema),
                message=pipeline.Student().message(),
                records=pipeline.Student.fetch(
                    as_dict=True
                )
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=True)

# notes:
# - https://stackoverflow.com/questions/11170949/how-to-make-a-copy-of-a-python-module-at-runtime
# - validate if memory will continue to grow without being garbage collected...