# import image as img
from hub_city.app import image as img
from area import compute_area
from hub_city.app.font import draw_image
# from font import draw_image
def get_image(video_):
    ret, im0 = img.video_object(video_, 0)
    if not ret:
        return ret, im0
    return ret, im0


def save_image(filename, image):
    pass
    save = img.Save()
    save.save(filename, image)


def create_dir(dirs="result"):
    img.check_dirs(dirs=dirs)


'''
*
* @ constructor 名称：image_draw
* @ description 作用：image_draw
* @ param{String}: area
* @ author 作者：JunJieLv（20230817）
*
'''


def image_draw(real_area, area, dst, size, fill):
    area = compute_area(real_area, area, size, 0.9)
    # dst = draw_image(dst, xy=(1600, 30), text="工地名称:%s" % ("施工二期"))
    # dst = draw_image(dst, xy=(1600, 60), text="工地面积:%s" % (str(real_area) + "km²"))
    # result = draw_image(dst, xy=(1600, 90), text="裸土面积:%s" % (str(round(area, 2)) + "km²"))
    dst = draw_image(dst, xy=(size[0] * 0.8, 30), text="工地名称:%s" % (str("施工二期")), fill=fill)
    dst = draw_image(dst, xy=(size[0] * 0.8, 60), text="工地面积:%s" % (str(real_area) + "km²"), fill=fill)
    result = draw_image(dst, xy=(size[0] * 0.8, 90), text="裸土面积:%s" % (str(round(area, 2)) + "km²"), fill=fill)
    # result = draw_image(dst, xy=(size[0] * 0.8, 120), text="%s" % (time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))))
    # result = draw_image(dst, xy=(size[0] * 0.8, 150),
    #                     text="时间:%s" % (time.strftime('', time.localtime(time.time()))))
    return result, area
