import json
import riseml

from encoder import Model
from utils import preprocess



def predict_json(data):
    model = Model()
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

def predict_json2(data):
    data = json.loads(data.decode("utf-8"))
    string_data = data["text"]
    model = Model(nsteps=len(string_data)+3)
    lines_in = [string_data]
    cell_data = model.cell_transform(lines_in)
    cell_data = cell_data[:, :, 2388][0]
    print(cell_data)

    data = {
        'chars': [lines_in[0][i] for i in range(len(lines_in[-1]))],
        'values': ["%f" % cell_data[2+i] for i in range(len(lines_in[-1]))]
    }
    return json.dumps(data).encode("utf-8")

if __name__ == '__main__':
    riseml.serve(predict_json2)

