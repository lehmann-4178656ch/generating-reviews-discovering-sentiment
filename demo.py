import json
import riseml

from encoder import Model
from utils import preprocess


model = Model()

def predict_json(data):
    data = json.loads(data.decode("utf-8"))
    string_data = data["text"]
    values = model.sequence_features(string_data, 2388)[2:-1]
    return json.dumps({
        'chars': [c for c in string_data],
        'values': ["%f" % v for v in values]
    }).encode("utf-8")

if __name__ == '__main__':
    riseml.serve(predict_json)

