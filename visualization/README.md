## ReadMe

该脚本用于将murphi生成的状态追踪文件，生成可视化的图片或视频，方便形式化验证的具象化
具体实现方法讲解见： [Arabela blog —— 可视化方法实现](https://arabelatso.github.io/2017/05/10/visualization/)

### 使用说明

##### 环境

- python3（安装好beautifulsoup4， webkit2png——直接用pip install）
  - [webkit2png参考链接](https://github.com/adamn/python-webkit2png)
- ffmpeg
  - **ubuntu**： sudo apt-get install ffmpeg  
  - **Mac**：brew install ffmpeg

##### 使用

- 将想绘制的协议路径放入murphi_trace文件夹（命名方式见下一章）
- 或： 原murphi_trace文件夹中已经有一些现成路径可以使用


- 运行main.py
- done

### Murphi_trace文件夹

##### 文件命名

- 大小写无关
- 以“flash”或“german”等协议名称开头即可
- “.txt”结尾
- trace生成的方式：(使用murphi自带的参数 -tf) —— 因为需要完整的路径，来满足处理需要

##### 关于添加文件

- 直接将符合“文件命名”的trace文件直接复制进入即可

##### 现有文件

###### flash

flash_I2E: 初始状态为全都是I —> 有一个cache的状态变成E

flash_I2S: 初始状态为全都是I —> 有一个cache的状态变成S

flash_initI2S: 初始状态为全都是I —> 有两个cache的状态变成S

flash_initS2E: 初始有两个cache的状态为S，另一个为I —> 另一个变为E



###### German

German_IE：初始状态为全都是I —> 有一个cache的状态变成E

German_EI：初始状态有一个cache为E —> 变回I



German_IS：初始状态为全都是I —> 有一个cache的状态变成S

German_SI：初始状态有一个cache为S—> 变回I



German_SE：初始状态有一个cache为S —> 变为E



