import os
from model import model_load, ModelParas, show
from imagePro import get_image, image_draw, save_image, create_dir
from video import video_init, video_set
from logg import log_warn, log_fatal, log_error
from hub_city.app.utils import exception_handler
from hub_city.app import web
import time
# video_format = 0

'''
*
* @ constructor 名称：BaseVar
* @ description 作用：BaseVar
* @ param{String}: None
* @ author 作者：JunJieLv（20231027）
* @ update time: 20250220
*
'''


class BaseVar(object):
    video_path = "trim_ipseek_copy.mp4"  # 视频路径
    save_image_size = (1500, 800)  # 保存图像尺寸
    image_threshold = 50000  # 精度阈值
    upload_step = 20  # 上传间隔
    url = 'http://192.168.111.27:8118/fly/smart-fly-monitor/reportWithFile'  # 上传目标url
    token = ""  # 上传token
    real_area = 30  # 真实面积 单位: 平方千米
    longitude = 118.666098  # 精度
    latitude = 37.40491  # 维度


def console(log_text):
    print(log_text)
    log_warn(log_text)


def upload(url=None, fields=None):
    if fields is None:
        fields = {}
    data = web.encoder(fields)
    web.post(url=url,
             data=data,
             headers={
                 'Content-Type': data.content_type,
                 "token": config_var.token
             }
             )


'''
*
* @ constructor 名称：stream_inference
* @ description 作用：stream_inference
* @ param{String}: None
* @ author 作者：JunJieLv（20231027）
* @ update time: 20250521
*
'''


class stream_inference(object):
    def __init__(self, _show_=False, _text_=True, _stream_=False, _save_=False):
        self.dst_size = config_var.save_image_size
        self.video_path = config_var.video_path
        self.image_threshold = config_var.image_threshold
        self.video_frame_id = 0
        self.total_time = 0
        self.save_flag = 0
        self._show_ = _show_
        self._text_ = _text_
        self._stream_ = _stream_
        self._save_ = _save_
        # self.video_run()

    def video_init(self):
        camera, write, state = video_init(self.video_path, name="temp", size=self.dst_size)
        if not state:
            log_error("processing IPCamera: " + self.video_path + " " + "Error: stream read fail ... ")
            return
        if self._stream_:
            frames_num = -1
            count = -1
        else:
            [frames_num, count] = video_set(camera, 1)
        create_dir("./result")
        self.image_pre(frames_num, count, camera,write)

    def image_pre(self, frames_num, count, camera,write):
        if frames_num < 0:
            ret = 2025
            while ret:
                count = count + 1
                self.image_impro(count, camera,write)
        else:
            while count < frames_num:
                count = count + 1
                self.image_impro(count, camera,write)

        text = "End------total 耗时: {}秒".format(self.total_time)
        if self._text_:
            console(text)

    @exception_handler
    def image_impro(self, count, camera, write):
        # count = count + 1

        text = "processing IPCamera: " + self.video_path + " " + str(count) + "-th frame ... "
        if self._text_:
            console(text)

        ret, im0 = get_image(camera)
        if not ret:
            return
        start_time = time.time()
        self.video_frame_id = count

        src, dst, area, video_id = model_load(src=im0,
                                              dst_size=self.dst_size,
                                              min_area=self.image_threshold,
                                              draw_color_fill=(0, 0, 255),  # red
                                              video_id=self.video_frame_id
                                              )

        # self.video_frame_id += 1

        real_area = 30
        font_color = (255, 255, 255)
        result, result_area = image_draw(real_area, area, dst, self.dst_size, fill=font_color)

        self.post_filters(result_area, real_area, video_id, result)

        if self._show_:
            show("image", result, 1)
            pass
        if self._save_:
            write(result)
        spend_time = time.time() - start_time
        text = "processing area: " + str(area) + " " + "video id: " + str(video_id) + "耗时: {}秒".format(spend_time)
        if self._text_:
            console(text)
        self.total_time += spend_time

    @exception_handler
    def post_filters(self,
                     result_area=0.0,
                     real_area=1.0,
                     video_id=0,
                     result=0
                     ):
        if (result_area / real_area) < 1:
            self.save_flag += 1
            if not self.save_flag % config_var.upload_step:
                if os.path.exists("result"):
                    save_image("./result/result1_%s.png" % video_id, result)
                    fields = {
                        "monitorvalue": str(result_area),
                        "monitorname": "裸土面积",
                        "monitorrate": str(result_area / real_area),
                        "x": str(config_var.longitude),
                        "y": str(config_var.latitude),
                        "siteid": "null",
                        "sitearea": str(config_var.real_area),
                        "file": ("result1_%s.png" % video_id, open(
                            "./result/result1_%s.png" % video_id,
                            'rb'), "image/png")
                    }
                    upload(url=config_var.url, fields=fields)


def main():
    rtsp_stream = stream_inference(_show_=True,)
    rtsp_stream.video_init()


if __name__ == "__main__":
    config_var = BaseVar()
    main()
