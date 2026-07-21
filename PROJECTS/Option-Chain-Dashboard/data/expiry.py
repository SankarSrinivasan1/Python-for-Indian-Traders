"""
data/expiry.py

Utility functions for working with NSE Option Chain expiry dates.

Author: Sankar Srinivasan
Book:
Python for Indian Stock Traders
"""

from datetime import datetime
from typing import List, Optional


class ExpiryManager:
    """
    Handles expiry date operations.

    Example
    -------
    >>> manager = ExpiryManager(json_data)
    >>> manager.get_all_expiries()

    >>> manager.get_nearest_expiry()

    >>> manager.is_valid_expiry("31-Jul-2026")
    """

    def __init__(self, option_chain_json: dict):
        self.data = option_chain_json

    # ----------------------------------------------------
    # Return all expiry dates
    # ----------------------------------------------------
    def get_all_expiries(self) -> List[str]:
        """
        Returns all available expiry dates.
        """

        records = self.data.get("records", {})

        expiries = records.get("expiryDates", [])

        return sorted(expiries, key=self._date_sort_key)

    # ----------------------------------------------------
    # Nearest expiry
    # ----------------------------------------------------
    def get_nearest_expiry(self) -> Optional[str]:
        """
        Returns the nearest expiry.
        """

        expiries = self.get_all_expiries()

        if not expiries:
            return None

        return expiries[0]

    # ----------------------------------------------------
    # Monthly expiry
    # ----------------------------------------------------
    def get_monthly_expiry(self) -> Optional[str]:
        """
        Returns the last expiry available.
        Usually the monthly expiry.
        """

        expiries = self.get_all_expiries()

        if not expiries:
            return None

        return expiries[-1]

    # ----------------------------------------------------
    # Validate expiry
    # ----------------------------------------------------
    def is_valid_expiry(self, expiry: str) -> bool:
        """
        Checks whether expiry exists.
        """

        return expiry in self.get_all_expiries()

    # ----------------------------------------------------
    # Number of expiries
    # ----------------------------------------------------
    def count(self) -> int:
        """
        Returns total number of expiries.
        """

        return len(self.get_all_expiries())

    # ----------------------------------------------------
    # Days to expiry
    # ----------------------------------------------------
    def days_to_expiry(self, expiry: str) -> Optional[int]:
        """
        Returns remaining calendar days.
        """

        try:
            expiry_date = datetime.strptime(expiry, "%d-%b-%Y").date()
            today = datetime.today().date()

            return (expiry_date - today).days

        except Exception:
            return None

    # ----------------------------------------------------
    # Expiry Information
    # ----------------------------------------------------
    def expiry_summary(self) -> dict:
        """
        Returns useful expiry information.
        """

        nearest = self.get_nearest_expiry()

        return {
            "total_expiries": self.count(),
            "nearest_expiry": nearest,
            "monthly_expiry": self.get_monthly_expiry(),
            "days_to_nearest": (
                self.days_to_expiry(nearest)
                if nearest
                else None
            ),
        }

    # ----------------------------------------------------
    # Internal sorter
    # ----------------------------------------------------
    @staticmethod
    def _date_sort_key(expiry: str):

        return datetime.strptime(expiry, "%d-%b-%Y")


# --------------------------------------------------------
# Standalone helper functions
# --------------------------------------------------------

def get_expiry_dates(option_chain_json: dict) -> List[str]:
    """
    Returns all expiry dates.
    """

    return ExpiryManager(option_chain_json).get_all_expiries()


def get_nearest_expiry(option_chain_json: dict) -> Optional[str]:
    """
    Returns nearest expiry.
    """

    return ExpiryManager(option_chain_json).get_nearest_expiry()


def get_monthly_expiry(option_chain_json: dict) -> Optional[str]:
    """
    Returns monthly expiry.
    """

    return ExpiryManager(option_chain_json).get_monthly_expiry()


# --------------------------------------------------------
# Example
# --------------------------------------------------------

if __name__ == "__main__":

    sample_json = {
        "records": {
            "expiryDates": [
                "24-Jul-2026",
                "31-Jul-2026",
                "28-Aug-2026",
                "25-Sep-2026",
            ]
        }
    }

    manager = ExpiryManager(sample_json)

    print("\nAvailable Expiries")
    print(manager.get_all_expiries())

    print("\nNearest Expiry")
    print(manager.get_nearest_expiry())

    print("\nMonthly Expiry")
    print(manager.get_monthly_expiry())

    print("\nSummary")
    print(manager.expiry_summary())
