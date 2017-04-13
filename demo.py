import argparse
from io import BytesIO
from numpy import mean
import riseml

from encoder import Model
from utils import preprocess

from image_gen import gen_image

model = Model()

def predict_sentiment(data):
    text_features = model.transform([data.decode("utf-8")])
    output_image = BytesIO()
    img = gen_image([" "], text_features[:, 2388])
    img.save(output_image, format='JPEG')
    return output_image.getvalue()

def predict_image(data):
    lines_in = []
    lines_out = []
    string_data = data.decode("utf-8")
    for i in range(1, len(string_data)):
        lines_in.append(string_data[:i])
    text_features = model.transform(lines_in)

    # https://github.com/openai/generating-reviews-discovering-sentiment/issues/2
    sentiments = text_features[:, 2388]
    output_image = BytesIO()
    img = gen_image(lines_in, sentiments)
    img.save(output_image, format='JPEG')
    return output_image.getvalue()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', action='store_true')
    args = parser.parse_args()

    if args.image:
        riseml.serve(predict_image)
    else:
        riseml.serve(predict_sentiment)

