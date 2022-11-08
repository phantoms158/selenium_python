import time
import pytest

@pytest.mark.usefixtures("setupSelenium")
class TestOne:
    def test_e2e(self):
        print("test")
        self.driver.get()
        time.sleep(1)