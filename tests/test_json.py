import json
import unittest

from base import (
    JSONBool,
    JSONCompose,
    JSONDict,
    JSONFloat,
    JSONInt,
    JSONList,
    JSONMaster,
    JSONObject,
    JSONSingleton,
    JSONStr,
)
from encoders import JSONObjectEncoder


class JsonTest(unittest.TestCase):
    def setUp(self):
        self.test1 = JSONObject(
            [
                {"Float": 2.3, "Int": 1, "Str": "string"},
                {"Dict": {"Float": 0.0, "List": [1, 2, 3]}},
            ]
        )
        self.test2 = JSONObject(True)
        self.test3 = JSONObject(
            {"List": [True, False], "Bool": True, "Dict": {"Float": 3.2}}
        )

    def test_types(self):
        """Assert all child types are the correct ones"""

        self.assertIsInstance(self.test1, JSONList)
        self.assertIsInstance(self.test1[0], JSONDict)
        self.assertIsInstance(self.test1[0]["Float"], JSONFloat)
        self.assertIsInstance(self.test1[0]["Int"], JSONInt)
        self.assertIsInstance(self.test1[0]["Str"], JSONStr)

        self.assertIsInstance(self.test1[1], JSONDict)
        self.assertIsInstance(self.test1[1]["Dict"], JSONDict)
        self.assertIsInstance(self.test1[1]["Dict"]["Float"], JSONFloat)
        self.assertIsInstance(self.test1[1]["Dict"]["List"], JSONList)

        self.assertIsInstance(self.test3, JSONDict)
        self.assertIsInstance(self.test3["List"], JSONList)
        self.assertIsInstance(self.test3["List"][0], JSONBool)
        self.assertIsInstance(self.test3["List"][1], JSONBool)
        self.assertIsInstance(self.test3["Bool"], JSONBool)
        self.assertIsInstance(self.test3["Dict"], JSONDict)
        self.assertIsInstance(self.test3["Dict"]["Float"], JSONFloat)

    def test_json_serializable(self):

        self.assertEqual(
            json.dumps(self.test1).replace('"', "'"), self.test1.__repr__()
        )
        self.assertEqual(
            json.dumps(self.test2, cls=JSONObjectEncoder).replace('"', "'"),
            self.test2.__repr__().lower(),
        )
        self.assertEqual(
            json.dumps(self.test3, cls=JSONObjectEncoder).replace('"', "'"),
            self.test3.__repr__().replace("True", "true").replace("False", "false"),
        )