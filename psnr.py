import math
import cv2
import sys


def mean_square_error(matrix1, matrix2):
    m = len(matrix1)
    n = len(matrix1[0])

    sum = 0.0
    for i in range(m):
        for j in range(n):
            diff = int(matrix1[i][j]) - int(matrix2[i][j])
            sum += (diff) ** 2

    return sum / (m*n)


def psnr(img1, img2):

    img1_dimensions = [len(img1), len(img1[0])]
    img2_dimensions = [len(img2), len(img2[0])]

    if img1_dimensions != img2_dimensions:
        print("Images must have equal dimensions")
        return

    mse = mean_square_error(img1, img2)

    if mse == 0:
        return 100

    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX) - 10 * math.log10(mse)


def main():
    arguments = sys.argv

    if len(arguments) < 3:
        print("Please, pass 2 image paths")
        return

    first_path = arguments[1]
    second_path = arguments[2]

    first_imagem = cv2.imread(first_path, cv2.IMREAD_GRAYSCALE)
    second_image = cv2.imread(second_path, cv2.IMREAD_GRAYSCALE)

    print("PSNR:", psnr(first_imagem, second_image))


if __name__ == "__main__":
    main()
