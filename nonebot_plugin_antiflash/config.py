from nonebot.log import logger
from typing import List
from pydantic import BaseModel, Extra
import nonebot

class AntiFlashConfig(BaseModel, extra=Extra.ignore):
    
    anti_flash_on: bool = True
    anti_flash_group: List[str] = []

class AntiFlashHandler:
    
    def __init__(self, config):
        self.on: bool = config.anti_flash_on
        self.group_on: List[str] = config.anti_flash_group
        
        if not self.on:
            logger.warning(f"已全局禁用群聊反闪照，指令：开启/禁用反闪照")
            
        if len(self.group_on) == 0 and self.on == True:
            logger.warning(f"Anti-flash on but group is empty!")
    
    def check_permission(self, gid: str) -> bool:
        return False if gid not in self.group_on else True
    
    def add_group(self, gid: str) -> None:
        '''
            已有则不进行操作，说明已启用
        '''
        if gid not in self.group_on:
            self.group_on.append(gid)
    
    def remove_group(self, gid: str) -> None:
        '''
            本不存在则不进行操作，说明已禁用
        '''
        try:
            self.group_on.remove(gid)
        except ValueError:
            pass

config: AntiFlashConfig = AntiFlashConfig.parse_obj(nonebot.get_driver().config.dict())
handler = AntiFlashHandler(config)