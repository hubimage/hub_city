from hub_city.app.image import hub_city, ModelParas
from hub_city.app.utils import exception_handler
import inspect
# todo 2025年5月25日加
from hub_city.app import image
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
               name=None,
               task=None):
    # coe = Coe()
    # paras = compute_coefs(coe, 3)
    # todo 2025年2月25日 不用模型 直接四种模型数据写死在 里面
    # trans = 0
    # if not name: # name为空 todo 2025年2月24日加
    #     hub_city.load_model("./model.obj")
    # else:
    #     hub_city.load_model("./hub_city-20250221.obj", name=name)
    # todo 2025年3月11日加 增加 task 参数 指定 神经网络的模型
    hub_city.load_model(model_path="./green.obj", name='', task="mask_cnn")
    # todo 2025年2月25日加 注释掉推理过程中的打印信息
    image.__debug__console__ = False
    src, dst, area, video_id = hub_city.inference(src=src,
                                                  dst_size=dst_size,
                                                  min_area=min_area,
                                                  draw_color_fill=draw_color_fill,
                                                  video_id=video_id,
                                                  params=0,
                                                  mode=1,  # todo 2025年3月11日加 mode =1 深度学习推理 =0 传统模型推理
                                                  )
    return src, dst, area, video_id


@exception_handler
def show(name, image, delay):
    hub_city.imshow(name, image, delay)

# todo 2025年2月25日加
# print(dir(ModelParas))
# print(ModelParas.__dict__)
# # 使用inspect模块的getmembers()函数查看MyClass类的所有属性, inspect属性可以解密到隐藏的属性参数
# print(inspect.getmembers(ModelParas))
# todo python二进制加密
# 查看Python类的所有属性
# 在Python中，查看一个类的所有属性可以通过多种方式实现。最常用的方法是使用内置的dir()函数，它可以列出对象的所有属性和方法。此外，还可以通过对象的__dict__属性或vars()函数来获取属性字典，或者使用inspect模块来进行更深入的反射操作。
#
# 使用dir()函数
#
# dir()函数可以在不带参数时列出当前范围内的变量、方法和定义的类型列表；带参数时，它会返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，则会尽可能收集参数信息。例如：
#
# class MyClass:
# def __init__(self):
# self.attribute = "value"
#
# # 使用dir()函数查看MyClass类的所有属性
# print(dir(MyClass))
# 通过__dict__属性
#
# 每个Python对象都有一个__dict__属性，它包含了对象的属性字典。通过这个属性，可以直接访问对象的所有属性和它们的值。例如：
#
# class MyClass:
# def __init__(self):
# self.attribute = "value"
#
# # 实例化MyClass
# my_object = MyClass()
#
# # 通过__dict__属性查看所有属性
# print(my_object.__dict__)
# 使用vars()函数
#
# vars()函数返回对象的__dict__属性，如果对象有__dict__属性的话。它与直接访问__dict__属性类似，但是vars()可以用于任何对象，不仅仅是实例。例如：
#
# class MyClass:
# def __init__(self):
# self.attribute = "value"
#
# # 实例化MyClass
# my_object = MyClass()
#
# # 使用vars()函数查看所有属性
# print(vars(my_object))
# 使用inspect模块
#
# inspect模块提供了许多与Python对象交互的函数，其中getmembers()函数可以获取对象的所有成员，包括属性和方法。例如：
#
# import inspect
#
# class MyClass:
# def __init__(self):
# self.attribute = "value"
#
# # 使用inspect模块的getmembers()函数查看MyClass类的所有属性
# print(inspect.getmembers(MyClass))
# 通过这些方法，开发者可以方便地查看和访问Python类的所有属性，从而更好地理解和使用类的结构。