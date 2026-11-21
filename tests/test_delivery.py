"""核对交接文件中的来源依据。"""
import unittest
from inspect_delivery import read_table


class DeliveryTest(unittest.TestCase):
    def test_linked_records(self):
        tickets = read_table("tickets.json")
        by_id = {r["ticket"]: r for r in tickets}
        self.assertTrue(all(r["order_line"] == by_id[r["linked"]]["order_line"]
                            for r in tickets if r["linked"]))
        self.assertTrue({r["ticket"] for r in read_table("decisions.json")} <= set(by_id))
        self.assertTrue({r["ticket"] for r in read_table("started.json")} <= set(by_id))
        self.assertTrue(any(r["selection"] == "常规抽查" for r in read_table("decisions.json")))
