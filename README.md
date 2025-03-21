# hub_city
hub_city is library for smart city Identification and detection. such as soil、green. 

## Installation

The recommended way to install hub_city is with [pip](https://pypi.org/project/hub-city/0.4/):

```sh
pip install hub-city
```

For others installation instructions, not supported.

## Documentation

You can find the documentation for hub-city on [ReadTheDocs](). This includes API documentation, contributing instructions, and several [tutorials](). For more details, check out our [paper](), [podcast episode](), [tutorial](https://www.youtube.com/watch), and [blog post](https://).

<p float="left">
  
</p>

## Example Usage

The following sections give basic examples of what you can do with hub-city.

First we'll import various classes and functions used in the following sections:

```python
# usage Version 0.0.7
# step 1： how to install package
#   pip install hub_city==0.0.7
# step 2： how to create the services
from hub_city.app import web
web.hub_services()
# step 3: Now, You can send a post image request on port 8089
Running on all addresses (0.0.0.0)
Running on http://127.0.0.1:8089
Running on http://192.168.31.233:8089
# step 4: http://127.0.0.1:8089/hubcity/rest/services/village/AiServer
{"consume_time": "423.12 ms", "image_w": 2560, "image_h": 1440, "coord": [{"left": 570, "top": 1189, "width": 269, "height": 141}, {"left": 1912, "top": 807, "width": 198, "height": 119}, {"left": 1865, "top": 590, "width": 228, "height": 70}, {"left": 1857, "top": 416, "width": 185, "height": 122}, {"left": 330, "top": 1275, "width": 188, "height": 59}, {"left": 193, "top": 1100, "width": 194, "height": 115}, {"left": 1284, "top": 1145, "width": 143, "height": 77}, {"left": 2308, "top": 914, "width": 126, "height": 78}, {"left": 1460, "top": 1057, "width": 188, "height": 109}, {"left": 1138, "top": 975, "width": 162, "height": 75}, {"left": 1860, "top": 968, "width": 140, "height": 82}, {"left": 61, "top": 907, "width": 320, "height": 153}, {"left": 1703, "top": 815, "width": 136, "height": 69}, {"left": 1587, "top": 491, "width": 240, "height": 134}, {"left": 1873, "top": 1162, "width": 148, "height": 77}, {"left": 2182, "top": 1080, "width": 250, "height": 210}, {"left": 1610, "top": 1228, "width": 235, "height": 78}, {"left": 1847, "top": 1257, "width": 102, "height": 53}, {"left": 2017, "top": 717, "width": 95, "height": 58}, {"left": 33, "top": 787, "width": 161, "height": 83}, {"left": 1694, "top": 631, "width": 123, "height": 70}, {"left": 1777, "top": 745, "width": 123, "height": 61}], "type": "village"}
```
## Update records
<!--
[release-0.2]
Fix the problem for post data fail. 

[release-0.3](https://github.com/hubimage/hub_city/releases/tag/release-0.3)  

First proposed the MOP ((Mixture of Parameter, 混合参数模型))architecture, loading different data according to different parameters.

[release-0.4](https://github.com/hubimage/hub_city/releases/tag/release-0.4)  

1. change the config var
   
2. add name in config var
-->

|Version|explain|
|:-:|:-:|
[Release-0.2](https://github.com/hubimage/hub_city/releases/tag/release-0.2)| Fix the problem for post data fail.
[Release-0.3](https://github.com/hubimage/hub_city/releases/tag/release-0.3)| First proposed the MOP ((Mixture of Parameter, 混合参数模型))architecture
[Release-0.4](https://github.com/hubimage/hub_city/releases/tag/release-0.4)| Change the config var and ADD name
[Release-0.0.5](https://github.com/hubimage/hub_city/releases/tag/Release-0.0.5)|Increasing neural network inference but not supporting inference from multiple images
[Release-0.0.6](https://github.com/hubimage/hub_city/releases/tag/Release-0.0.6)|2025-03-20 add remote sensing image recognition of village clusters
[Release-0.0.7](https://github.com/hubimage/hub_city/releases/tag/Release-0.0.7)|add Deploy testing services on March 21, 2025<br> add Service inference JSON format on March 21, 2025<br>
