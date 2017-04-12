from encoder import Model
from numpy import mean

text = [
    'Just what I was looking for. Nice fitted pants, exactly matched seam to color contrast with other pants I own. Highly recommended and also very happy!',
    'The package received was blank and has no barcode. A waste of time and money.',
    'I couldn’t figure out how to use just one and my favorite running app. I use it all the time. Good quality, You cant beat the price.',
    'Great little item. Hard to put on the crib without some kind of embellishment. My guess is just like the screw kind of attachment I had.'
]
model = Model()
text_features = model.transform(text)

for i in range(text_features.shape[0]):
    # https://github.com/openai/generating-reviews-discovering-sentiment/issues/2
    sentiment = text_features[i][2388]
    print("Sentiment for text {i}: {s}".format(i=i,s=sentiment))
