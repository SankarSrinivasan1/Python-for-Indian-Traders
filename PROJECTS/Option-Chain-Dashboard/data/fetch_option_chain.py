"""
fetch_option_chain.py

Downloads and processes NSE Option Chain data.

Author : Sankar Srinivasan
Book   : Python for Indian Stock Traders
"""

from typing import List, Dict

import pandas as pd

from data.nse_api import NSEAPI


class OptionChainFetcher:
    """
    Fetches Option Chain data and converts it into
    a clean Pandas DataFrame.
    """

    def __init__(self):
        self.api = NSEAPI()

    def fetch(self, symbol: str = "NIFTY") -> pd.DataFrame:
        """
        Download option chain data.

        Parameters
        ----------
        symbol : str

        Returns
        -------
        pandas.DataFrame
        """

        data = self.api.get_option_chain(symbol)

        records = []

        for row in data["records"]["data"]:

            strike = row.get("strikePrice")

            ce = row.get("CE", {})
            pe = row.get("PE", {})

            record = {
                "Strike":

                    strike,

                "Expiry":

                    ce.get("expiryDate")
                    or pe.get("expiryDate"),

                "CE_OI":

                    ce.get("openInterest", 0),

                "CE_Change_OI":

                    ce.get("changeinOpenInterest", 0),

                "CE_Volume":

                    ce.get("totalTradedVolume", 0),

                "CE_IV":

                    ce.get("impliedVolatility", 0),

                "CE_LTP":

                    ce.get("lastPrice", 0),

                "CE_Bid":

                    ce.get("bidprice", 0),

                "CE_Ask":

                    ce.get("askPrice", 0),

                "PE_OI":

                    pe.get("openInterest", 0),

                "PE_Change_OI":

                    pe.get("changeinOpenInterest", 0),

                "PE_Volume":

                    pe.get("totalTradedVolume", 0),

                "PE_IV":

                    pe.get("impliedVolatility", 0),

                "PE_LTP":

                    pe.get("lastPrice", 0),

                "PE_Bid":

                    pe.get("bidprice", 0),

                "PE_Ask":

                    pe.get("askPrice", 0),
            }

            records.append(record)

        df = pd.DataFrame(records)

        return df.sort_values("Strike").reset_index(drop=True)

    def fetch_by_expiry(
        self,
        symbol: str,
        expiry: str,
    ) -> pd.DataFrame:
        """
        Return only selected expiry.
        """

        df = self.fetch(symbol)

        return (
            df[df["Expiry"] == expiry]
            .sort_values("Strike")
            .reset_index(drop=True)
        )

    def available_expiries(
        self,
        symbol: str = "NIFTY",
    ) -> List[str]:
        """
        List available expiry dates.
        """

        data = self.api.get_option_chain(symbol)

        return data["records"]["expiryDates"]

    def underlying_price(
        self,
        symbol: str = "NIFTY",
    ) -> float:
        """
        Current underlying value.
        """

        data = self.api.get_option_chain(symbol)

        return data["records"]["underlyingValue"]

    def atm_strike(
        self,
        symbol: str = "NIFTY",
    ) -> int:
        """
        Find nearest ATM strike.
        """

        df = self.fetch(symbol)

        spot = self.underlying_price(symbol)

        nearest = (
            df.iloc[
                (df["Strike"] - spot)
                .abs()
                .argsort()[:1]
            ]
        )

        return int(nearest.iloc[0]["Strike"])


if __name__ == "__main__":

    fetcher = OptionChainFetcher()

    df = fetcher.fetch("NIFTY")

    print(df.head())

    print()

    print("Rows :", len(df))

    print("Spot :", fetcher.underlying_price("NIFTY"))

    print("ATM  :", fetcher.atm_strike("NIFTY"))

    print()

    print("Expiries")

    print(fetcher.available_expiries("NIFTY"))
