from typing import Dict, Optional

from tap_giftup.streams.base import GiftupBaseStream


class CompanyStream(GiftupBaseStream):
    STREAM_NAME = "company"

    def make_request(self, endpoint: Optional[str] = None, params: Optional[Dict[str, str]] = None):
        return self.giftup_client.get_company()

