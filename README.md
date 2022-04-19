<div align="center">

# Anti Flash

<!-- prettier-ignore-start -->
<!-- markdownlint-disable-next-line MD036 -->
_🎇 反闪照 🎇_
<!-- prettier-ignore-end -->

</div>
<p align="center">
  
  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_antiflash/blob/beta/LICENSE">
    <img src="https://img.shields.io/github/license/MinatoAquaCrews/nonebot_plugin_antiflash?color=blue">
  </a>
  
  <a href="https://github.com/nonebot/nonebot2">
    <img src="https://img.shields.io/badge/nonebot2-2.0.0beta.2-green">
  </a>
  
  <a href="https://github.com/MinatoAquaCrews/nonebot_plugin_antiflash/releases/tag/v0.2.3">
    <img src="https://img.shields.io/github/v/release/MinatoAquaCrews/nonebot_plugin_antiflash?color=orange">
  </a>
  
</p>

</p>

## 版本

v0.2.3

⚠ 适配nonebot2-2.0.0beta.2

👉 适配alpha.16版本参见[alpha.16分支](https://github.com/MinatoAquaCrews/nonebot_plugin_antiflash/tree/alpha.16)

[更新日志](https://github.com/MinatoAquaCrews/nonebot_plugin_antiflash/releases/tag/v0.2.3)

## 安装

1. 通过`pip`或`nb`安装；

2. 在`env`内设置：

	```python
	ANTI_FLASH_ON=true                          # 全局开关
	ANTI_FLASH_GROUP=["123456789", "987654321"] # 默认开启的群聊，但可通过指令开关
	ANTI_FLASH_PATH="your-path-to-config.json"  # 配置文件路径，默认同插件代码路径
	```

	`ANTI_FLASH_GROUP`会在每次初始化时写入配置文件，在群组启用反闪照，可通过指令更改。

	**修改** 配置文件即读即改，可后台修改。

## 功能

1. 全局开关**仅超管**配置，不支持指令修改全局开关；

2. 各群聊均配置开关，需**管理员及超管权限**进行修改；

## 命令

开启/启用/禁用反闪照