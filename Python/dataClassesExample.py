from dataclasses import dataclass
from datetime import datetime
import requests

@dataclass
class test_result:
  test_id: str
  test_result: str
  comment: str = ""
  test_date: str = datetime.now().strftime("%m/%d/%y %H:%M:%S")
  environment: str = "192.168.176.54"

  def __eq__(self, other):
      return (self.test_id == other.test_id and self.test_result == other.test_result)

  def to_zephyr_format(self):
      idData = self.test_id.split('-')
      requestBody = {
          "projectKey": idData[0],
          "testCycleKey": idData[1],
          "testCaseKey": idData[2],
          "statusName": self.test_result,
          "testScriptResults": {"statusName":self.test_result,"actualResult":self.comment},
          "environmentName": self.environment,
      }
      return requestBody