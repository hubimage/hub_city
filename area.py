'''
*
* @ constructor 名称：area
* @ description 作用：compute_area
* @ param{String}: area
* @ author 作者：JunJieLv（20231017）
*
'''


def compute_area(real_area=None, ima_area=None, image_size=None, conf=0.9):
    percentage = ima_area / (image_size[0] * image_size[1])

    # print("percenta", ima_area,image_size,percentage)
    real_area *= percentage
    real_area *= conf
    return real_area

