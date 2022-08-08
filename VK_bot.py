import vk_api
import os

vk_session = vk_api.VkApi(token=os.environ.get('TOKEN'))
id1 = os.environ.get('ID1')
id2 = os.environ.get('ID2')


def send_message(id_, some_text):
    vk_session.method("messages.send", {"user_id": id_, "message": some_text, "random_id": 0})
