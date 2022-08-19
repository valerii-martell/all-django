import datetime
import unittest

from django.test import TestCase
from channels.testing import HttpCommunicator

from .consumers import ChatConsumer


class MyTests(TestCase):
    @unittest.skip
    async def test_my_consumer(self):
        communicator = HttpCommunicator(
            ChatConsumer.as_asgi(), path="/test/", method="GET"
        )

        await communicator.send_input({"type": "chat_message", "message": "test"})
        value = await communicator.receive_output()
        print(value)
        self.assertAlmostEqual(
            value.get("text"), f'{"message": "test", "date": {datetime.date.date()}}'
        )
