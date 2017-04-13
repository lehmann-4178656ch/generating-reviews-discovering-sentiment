import json
import riseml

from encoder import Model
from utils import preprocess

model = Model()

def predict_json(data):
    data = json.loads(data.decode("utf-8"))
    lines_in = []
    string_data = data["text"]
    for i in range(1, len(string_data)):
        lines_in.append(string_data[:i])
    text_features = model.transform(lines_in)

    # https://github.com/openai/generating-reviews-discovering-sentiment/issues/2
    sentiments = text_features[:, 2388]
    data = {
        'chars': [lines_in[i][i] for i in range(len(lines_in[-1]))],
        'values': ["%f" % sentiments[i] for i in range(len(lines_in[-1]))]
    }
    return json.dumps(data).encode("utf-8")

if __name__ == '__main__':
    riseml.serve(predict_json)

