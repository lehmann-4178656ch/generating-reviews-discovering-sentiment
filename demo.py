from numpy import mean
import riseml

from encoder import Model
from utils import preprocess


model = Model()

def predict(data):
    lines_in = []
    lines_out = []
    string_data = data.decode("utf-8")
    for i in range(len(string_data)):
        lines_in.append(string_data[:i])
    text_features = model.transform(lines_in)

    # https://github.com/openai/generating-reviews-discovering-sentiment/issues/2
    sentiments = text_features[:, 2388]

    for i in range(len(sentiments)):
        lines_out.append("Sentiment for text '{i}': {s}".format(
            i=lines_in[i], s=sentiments[i]))
    result = '\n'.join(lines_out)
    return result.encode("utf-8")

riseml.serve(predict)
