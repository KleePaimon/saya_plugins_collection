import re

from graia.saya import Saya, Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from graia.application.event.messages import *
from graia.application.event.mirai import *


# 插件信息
__name__ = "MessagePrinter"
__description__ = "打印收到的消息"
__author__ = "SAGIRI-kawaii"
__usage__ = ""


saya = Saya.current()
channel = Channel.current()


@channel.use(ListenerSchema(listening_events=[GroupMessage]))
async def group_message_listener(
    message: MessageChain,
    sender: Member,
    group: Group
):
    message_serialization = message.asSerializationString()
    message_serialization = message_serialization.replace(
        "[mirai:source:" + re.findall(r'\[mirai:source:(.*?)]', message_serialization, re.S)[0] + "]",
        ""
    )
    # print(message_serialization)
    print(f"接收到来自群组 <{group.name} ({group.id})> 中成员 <{sender.name} ({sender.id})> 的消息：{message.asDisplay()}")


@channel.use(ListenerSchema(listening_events=[FriendMessage]))
async def friend_message_listener(
    message: MessageChain,
    sender: Friend
):
    print(f"接收到来自好友 <{sender.nickname} ({sender.id})> 的消息：{message.asDisplay()}")


@channel.use(ListenerSchema(listening_events=[TempMessage]))
async def temp_message_listener(
    message: MessageChain,
    sender: Member
):
    print(f"接收到来自 <{sender.name} ({sender.id})> 的临时消息：{message.asDisplay()}")
