from flask import Flask, request
import time
import imp

app = Flask(__name__)

@app.route("/student")
def student():
    pipeline=imp.load_module(f"{request.args.get('prefix')}_pipeline", *imp.find_module('pipeline'))
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