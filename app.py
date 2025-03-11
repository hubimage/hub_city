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
    video_path = "trim_ipseek_copy.mp4"  # 视频路径 todo 2025年2月24日加 视频时长 20秒 分析用时  57S
    # video_path = "de.mp4"   # todo 2025年2月24日加 视频时长 8分19秒  分析用时 668.2571303844452秒 11分
    save_image_size = (1500, 800)  # 保存图像尺寸
    image_threshold = 50000  # 精度阈值
    upload_step = 20  # 上传间隔
    url = 'http://192.168.111.27:8118/fly/smart-fly-monitor/reportWithFile'  # 上传目标url
    token = ""  # 上传token
    real_area = 30  # 真实面积 单位: 平方千米
    longitude = 118.666098  # 精度
    latitude = 37.40491  # 维度
    object_name = ""


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
    def __init__(self, _show_=False, _text_=True, _stream_=False, _save_=False, _post_ = False):
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
        self._post_ = _post_
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
                                              video_id=self.video_frame_id,
                                              name=config_var.object_name
                                              )
        # print("dddddd")
        # self.video_frame_id += 1
        # How it works How it works
        real_area = 30
        font_color = (255, 255, 255)
        result, result_area = image_draw(real_area, area, dst, self.dst_size, fill=font_color)
        # todo 2025年2月25日 更改  去吊self._post_, 加在 内部
        #   任务1: 保存数据
        #   任务2: 上传数据
        #   version 1
        # if self._post_:
        #     self.post_filters(result_area, real_area, video_id, result)
        # todo version 2
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
                    # todo 2025年2月25日加
                    if self._post_:
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
    rtsp_stream = stream_inference(_show_=False,)
    rtsp_stream.video_init()


if __name__ == "__main__":
    config_var = BaseVar()
    main()
# (I)
# 《行业大模型构建经验分享》 (10:40-12:00)
# 主讲人: 科大讯飞星火军团行业 AI 工程中心产品总监
# 潘振兴
# (三)《排水大模型应用系统开发经验分享》
# (13:30-14:30)
# 主讲人: 山东正元航空遥感技术有限公司遥感与智慧应用中心副经理宫龙
# 1. 为啥选择？
# 2. 交互方式：
#   1. 语音识别输入。
#   2. 点线面 画框交互方式。
# 2. 知识库问答:
#   本地知识库加载后 先搜索本地知识库 然后加载网络数据库(可能是第三方收集的)
# 3. 界面设计：
#   UI层上面加一个指令层,指令调用UI层。
# 4. 管网查询: 交并查询
#   小模型查询: 交 并 数据操作
#   统计: 条件统计 自然语言输入 调出 各种弹出框
#       隐患统计：
#       管线统计：
#       我们只是简单的做了工作，前期只是在做一些准备工作，实际开发中 我们只用了1个多月时间
#       查询易涝点：
#       查询防汛物资:
#       查询防汛人员定位信息:
#       合同处理：工单处理 有一个流程。
#       报警信息: 语言播报。
#   私密数据在本地 不在他们那边的。
#   讯飞输入法: 输入法就是用的讯飞输入法。
#   任务链：
#   华为 做 图片
#   讯飞 做 语音
#   讯飞说 3000条以上QA
#   大屏自动问数: 问表或图 自动生成 表或图
#   收费方式: tokens 按照tokens收费的
#       目前 所有的收费方式都是这样的。
#       我们现在有些事情是商量的干的,收费并没有那么高。
#       知识库这个事情 应该比较简单的了 deepseek有api 能直接接到我们的系统里面。
#       知识库更新 一年更新一次 就了不得了
#       外挂知识库 并不需要训练， 需要训练的话收费就比较高了,因为我们没有算力
#       如果不及时更新数据库的话 别人查询最近报警信息 还是查询的1年前的呢?
#



