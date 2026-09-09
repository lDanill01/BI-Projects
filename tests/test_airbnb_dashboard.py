import json
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
HTML = ROOT / "dashboards" / "airbnb-exploracao" / "index.html"
DATA = ROOT / "dashboards" / "airbnb-exploracao" / "data.js"


def load_dashboard_data():
    text = DATA.read_text(encoding="utf-8")
    payload = text.split("window.AIRBNB_DATA = ", 1)[1].split(";\n", 1)[0]
    return json.loads(payload)


class AirbnbDashboardTests(unittest.TestCase):
  def test_dashboard_publishes_real_dataset_summary_and_filters(self):
    self.assertTrue(HTML.exists())
    self.assertTrue(DATA.exists())
    html = HTML.read_text(encoding="utf-8")
    data = load_dashboard_data()

    self.assertIn("htmx.org", html)
    self.assertIn("filter-region", html)
    self.assertIn("filter-room", html)
    self.assertEqual(data["meta"]["source"], "Airbnb_Open_Data.csv")
    self.assertEqual(data["meta"]["rows"], 102599)
    self.assertEqual(data["summary"]["listings"], 102599)


  def test_dashboard_data_supports_rankings_and_detail_table(self):
    data = load_dashboard_data()

    self.assertGreaterEqual(len(data["roomTypes"]), 4)
    self.assertGreaterEqual(len(data["regions"]), 5)
    self.assertGreaterEqual(len(data["neighbourhoods"]), 10)
    self.assertGreaterEqual(len(data["sampleListings"]), 50)
    self.assertTrue({"id", "name", "region", "roomType", "price", "availability"} <= set(
        data["sampleListings"][0]
    ))


if __name__ == "__main__":
    unittest.main()
