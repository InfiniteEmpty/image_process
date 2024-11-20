import cv2
import numpy as np


def show_signed(label, input, max):
    posi = (input * (input >= 0))
    posi = posi.astype(np.float32)
    # posi = posi / max
    max_color = np.max(posi)
    if max_color > max / 10:
        posi = posi / max_color
    else:
        posi = posi / (max / 10)

    negt = -input * (input < 0)
    negt = negt.astype(np.float32)
    # negt = negt / max
    max_color = np.max(negt)
    if max_color > max / 10:
        negt = negt / max_color
    else:
        negt = negt / (max / 10)

    last = np.zeros_like(posi)
    last = last.astype(np.float32)

    cv2.imshow(label, cv2.merge([last, posi, negt]))
