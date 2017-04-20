import argparse
import timeit

from encoder import Model
from utils import preprocess


model = Model()

input_texts = [
  "The package received was blank and has no barcode. A waste of time and money.",
  "Just what I was looking for. Nice fitted pants, exactly matched seam to color contrast with other pants I own. Highly recommended and also very happy!",
  "This is one of Crichton's best books. The characters of Karen Ross, Peter Elliot, Munro, and Amy are beautifully developed and their interactions are exciting, complex, and fast-paced throughout this impressive novel. And about 99.8 percent of that got lost in the film. Seriously, the screenplay AND the directing were horrendous and clearly done by people who could not fathom what was good about the novel. I can't fault the actors because frankly, they never had a chance to make this turkey live up to Crichton's original work. I know good novels, especially those with a science fiction edge, are hard to bring to the screen in a way that lives up to the original. But this may be the absolute worst disparity in quality between novel and screen adaptation ever.  The book is really, really good. The movie is just dreadful."
]

def transform(text):
    lines_in = []
    for i in range(1, len(text)):
        lines_in.append(text[:i])
    model.transform(lines_in)


def sequence_features(text):
    model.sequence_features(text, 2388)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--repeat', type=int, default=1)
    parser.add_argument('--number', type=int, default=3)
    args = parser.parse_args()

    for text in input_texts:
        print('Timeit for: {}...'.format(text[:60]))
        print(timeit.repeat('transform(text)', repeat=args.repeat,
            number=args.number, globals=globals()))
        print(timeit.repeat('sequence_features(text)', repeat=args.repeat,
            number=args.number, globals=globals()))
