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
