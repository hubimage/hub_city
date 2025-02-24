from hub_city.app import image
from area import compute_area

'''
*
* @ constructor 名称：video_init
* @ description 作用：video_init
* @ param{String}: path
* @ author 作者：JunJieLv（20230817）
*
'''


def video_init(path, name, size):
    state = None
    video = image.Video(name, size)
    # 这个位置如果错误，不会执行下面的代码，并且会卡在这里
    video_ = video.video(path)
    write = video.save
    state = image.video_object(video_, 1)
    return [video_, write, state]
    # if not cv.video_object(video_, 1):
    #     assert "video open wrong"  # wring in open



'''
*
* @ constructor 名称：video_set
* @ description 作用：video_set
* @ param{String}: cap
* @ author 作者：JunJieLv（20231027）
*
'''


def video_set(cap, count_):
    frames_num = int(cap.get(7))
    # count_ = 0
    cap.set(1, count_)
    return [frames_num, count_]

