from hub_city.app.image import hub_city, ModelParas
from hub_city.app.utils import exception_handler


class Coe:
    def __init__(self):
        self.a1 = 0
        self.b1 = 0
        self.c1 = 0
        self.a2 = 0
        self.b2 = 0
        self.c2 = 0
        self.n = 0
        # print("Coe", 1)


def compute_coefs(c, sigma):
    q = 1.887
    q1 = 6.064818
    q2 = 36.782017373124
    q3 = -35.782017373124
    c.a1 = 1.57825 - q * 4.10 + q2 * 0.167
    # print(c.a1)
    c.b1 = q * 2.741 + q1 * 1.804 + q2 * 0.215
    # print(c.b1)
    c.c1 = q1 * 1.635 + q2 * 0.078 - q3 * 0.4
    # print(c.c1)

    c.a2 = q * 2.65 + q2 * 0.437 + c.a1
    # print(c.a2)
    c.b2 = q2 * q2 * 0.05 + 3.39 * c.a2 + c.a1
    # print(c.b2)
    c.c2 = (c.a2 + c.b2) / 2 + q2 * 0.354
    # print(c.c2)
    return [c.a1, c.b1, c.c1, c.a2, c.b2, c.c2]


def compute_q(sigma):
    if sigma >= 2:
        q = 0.785 * sigma - 0.468
    else:
        q = 0.3
    q1 = 3.214 * q
    q2 = q1 * q1
    q3 = 1 - q2
    return [q, q1, q2, q3]


def compute_p(sigma):
    if sigma >= 2:
        q = 0.785 * sigma - 0.468
    else:
        q = 0.3
    q1 = 3.214 * q
    q2 = q1 * q1
    q3 = q2 - 1
    return q3


def model_load(src,
               dst_size,
               min_area,
               draw_color_fill,
               video_id,
               name=''):
    coe = Coe()
    paras = compute_coefs(coe, 3)
    # trans = 0
    # hub_city.load_model("./model.obj")
    hub_city.load_model("./hub_city-20250221.obj", name=name)
    src, dst, area, video_id = hub_city.inference(src=src,
                                                  dst_size=dst_size,
                                                  min_area=min_area,
                                                  draw_color_fill=draw_color_fill,
                                                  video_id=video_id,
                                                  params=paras, )
    return src, dst, area, video_id


@exception_handler
def show(name, image, delay):
    hub_city.imshow(name, image, delay)
