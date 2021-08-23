# SPDX-License-Identifier: Apache-2.0
import os
import numpy
from _tools import generate_random_images, benchmark


def main(opset=13):
    url = "https://tfhub.dev/google/imagenet/mobilenet_v3_small_075_224/feature_vector/5?tf-hub-format=compressed"
    dest = "tf-mobilenet-v3-small-075-224"
    name = "mobilenet-v3-small-075-224"
    onnx_name = os.path.join(dest, "%s-%d.onnx" % (name, opset))

    imgs = generate_random_images(shape=(1, 224, 224, 3), scale=1.)

    benchmark(url, dest, onnx_name, opset, imgs)


if __name__ == "__main__":
    main()
