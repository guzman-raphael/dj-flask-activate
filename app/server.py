from flask import Flask, request
import time
import importlib

app = Flask(__name__)

@app.route("/student")
def student():
    import pipeline
    importlib.reload(pipeline)
    pipeline.schema.activate(f"{request.args.get('prefix')}_university")
    print("--- imported ---", flush=True)
    # do stuff
    time.sleep(5)
    return dict(id=str(pipeline.schema))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=True)
