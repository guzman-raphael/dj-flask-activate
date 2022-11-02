from flask import Flask, request
import time
import importlib
import pipeline

app = Flask(__name__)

@app.route("/student")
def student():
    importlib.reload(pipeline)
    schema = pipeline.schema
    schema.activate(f"{request.args.get('prefix')}_university")
    print("--- imported ---", flush=True)
    # do stuff
    time.sleep(5)
    return dict(schema=str(schema),
                message=pipeline.Student().message(),
                records=pipeline.Student.fetch(
                    as_dict=True
                )
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, threaded=True)
