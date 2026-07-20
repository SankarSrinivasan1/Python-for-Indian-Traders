"""
File: data/nse_api.py

Description
-----------
Utility class for downloading live option chain data from NSE India.

This module handles:

- Session creation
- Cookie management
- HTTP headers
- Automatic retry
- JSON download

Author:
Sankar Srinivasan

Repository:
option-chain-dashboard
"""

from __future__ import annotations

import requests
from typing import Dict


class NSEAPI:
    """
    Wrapper around NSE India APIs.
    """

    BASE_URL = "https://www.nseindia.com"

    OPTION_CHAIN_API = (
        "https://www.nseindia.com/api/option-chain-indices?symbol={}"
    )

    HEADERS = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/137.0 Safari/537.36"
        ),
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.nseindia.com/option-chain",
        "Connection": "keep-alive",
    }

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update(self.HEADERS)

        self.initialize_session()

    # --------------------------------------------------------

    def initialize_session(self):
        """
        Visit NSE homepage once to obtain cookies.
        """

        try:

            self.session.get(

                self.BASE_URL,

                timeout=10,

            )

        except requests.RequestException as e:

            raise RuntimeError(
                f"Unable to connect to NSE website.\n{e}"
            )

    # --------------------------------------------------------

    def refresh_session(self):
        """
        Refresh cookies.
        """

        self.session.cookies.clear()

        self.initialize_session()

    # --------------------------------------------------------

    def fetch_option_chain(
        self,
        symbol: str = "NIFTY"
    ) -> Dict:
        """
        Download option chain JSON.

        Parameters
        ----------
        symbol : str

            Example:
            NIFTY
            BANKNIFTY
            FINNIFTY

        Returns
        -------
        dict
        """

        url = self.OPTION_CHAIN_API.format(symbol.upper())

        try:

            response = self.session.get(

                url,

                timeout=15,

            )

            if response.status_code == 401:

                self.refresh_session()

                response = self.session.get(

                    url,

                    timeout=15,

                )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:

            raise RuntimeError(
                f"NSE API Error\n{e}"
            )

    # --------------------------------------------------------

    def get_records(
        self,
        symbol: str = "NIFTY"
    ) -> list:
        """
        Return option chain records only.
        """

        data = self.fetch_option_chain(symbol)

        return data.get("records", {}).get("data", [])

    # --------------------------------------------------------

    def get_expiry_dates(
        self,
        symbol: str = "NIFTY"
    ) -> list:
        """
        Return all expiry dates.
        """

        data = self.fetch_option_chain(symbol)

        return data.get("records", {}).get("expiryDates", [])

    # --------------------------------------------------------

    def get_underlying_value(
        self,
        symbol: str = "NIFTY"
    ) -> float:
        """
        Return current index value.
        """

        data = self.fetch_option_chain(symbol)

        return data.get(
            "records",
            {}
        ).get(
            "underlyingValue",
            0.0
        )


# ------------------------------------------------------------
# Example
# ------------------------------------------------------------

if __name__ == "__main__":

    api = NSEAPI()

    print("=" * 50)

    print("Underlying")

    print(api.get_underlying_value("NIFTY"))

    print("=" * 50)

    print("Expiry Dates")

    print(api.get_expiry_dates("NIFTY"))

    print("=" * 50)

    records = api.get_records("NIFTY")

    print(f"Downloaded {len(records)} option records.")
