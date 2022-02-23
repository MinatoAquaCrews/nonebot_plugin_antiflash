from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageSegment
from nonebot.rule import Rule
from nonebot import on_message
import re
import nonebot
from pydantic import ConfigError

global_config = nonebot.get_driver().config
if not hasattr(global_config, "anti_flash_on"):
    ANTI_FLASH_ON = False
else:
    ANTI_FLASH_ON = nonebot.get_driver().config.anti_flash_on

if not hasattr(global_config, "anti_flash_group"):
    anti_flash_group = []
    if ANTI_FLASH_ON:
        raise ConfigError("Anti-flash group should not be empty when anti-flash is enabled!")
else:
    anti_flash_group = nonebot.get_driver().config.anti_flash_group

__anti_flash_vsrsion__ = "v0.2.1"

async def _checker(bot: Bot, event: GroupMessageEvent) -> bool:
    msg = str(event.get_message())
    return True if 'type=flash' in msg and ANTI_FLASH_ON else False

flashimg = on_message(priority=1,rule=Rule(_checker))
@flashimg.handle()
async def _(bot: Bot, event: GroupMessageEvent):
    gid = str(event.group_id)
    if gid in anti_flash_group:
        msg = str(event.get_message())
        comment = re.compile(r'file=(.*?).image',re.S)
        comment1 = str(comment.findall(msg))
        reg = "[^0-9A-Za-z\u4e00-\u9fa5]"
        text = comment1
        x=str(re.sub(reg, '', text.upper()))
        id = event.get_user_id()
        url = ('https://gchat.qpic.cn/gchatpic_new/' + id + '/2640570090-2264725042-' + x.upper() + '/0?term=3')

        await flashimg.send((MessageSegment.image(url)), at_sender=False)