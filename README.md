# iron-Notes
铁甲小记【2023-

相关地址：

1. 文档：
   1. [markdown文档](https://www.runoob.com/markdown/md-tutorial.html)
   2. [前端项目](https://github.com/PanJiaChen/vue-element-admin/blob/master/README.zh-CN.md)
2. 各类软件、环境下载地址：
   1. [vscode](https://code.visualstudio.com/)

 <details>
  <summary>更新日志</summary>
- 2023-11-27:
  1. 学习api请求：GET请求，具体更新在tools/request
  2. 更新前端项目
- 未完成:
  [X] POST
</details>

<details>
<summary>表格笔记</summary>

- 从模型尺寸和输入图片比例两种角度，在构建了移动端系列模型，方便不同场景下的灵活应用。
- 所有权重都经过 400 个 epoch 的训练，并且没有使用蒸馏技术。
-  mAP 和速度指标是在 COCO val2017 数据集上评估的，输入分辨率为表格中对应展示的。
- 使用 MNN 2.3.0 AArch64 进行速度测试。测速时，采用2个线程，并开启arm82加速，推理预热10次，循环100次。
- 高通888(sm8350)、天玑720(mt6853)和高通660(sdm660)分别对应高中低端不同性能的芯片，可以作为不同芯片下机型能力的参考。
- [NCNN 速度测试](./docs/Test_NCNN_speed.md)教程可以帮助展示及复现 YOLOv6Lite 的 NCNN 速度结果。

</details>

