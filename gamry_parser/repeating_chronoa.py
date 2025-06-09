import gamry_parser as parser
import pandas as pd
import re


class RepeatingChronoAmperometry(parser.GamryParser):
    """Load a ChronoAmperometry experiment generated in Gamry EXPLAIN format."""

    def curve(self, curve: int = 0):
        """retrieve chronoamperometry experiment data

        Args:
            curve (int, optional): curve to return (CHRONOA experiments typically only have 1 curve). Defaults to 1.

        Returns:
            pandas.DataFrame:
                - T: time, in seconds or Timestamp
                - Vf: potential, in V
                - Im: current, in A
        """

        assert self.loaded, "DTA file not loaded. Run ChronoAmperometry.load()"
        df = self._curves[curve]
        return df[["T", "Vf", "Im"]]

    @property
    def potentiostat(self):
        """retrieve the name of the potentiostat used for the experiment

        Args:
            None.

        Returns:
            str: name of the potentiostat
        """
        return self._header.get("PSTAT", None)

    @property
    def date(self):
        """retrieve the date of the experiment

        Args:
            None.

        Returns:
            str: date of the experiment
        """
        return self._header.get("DATE", None)

    def time(self):
        """retrieve the time of the experiment

        Args:
            None.

        Returns:
            str: time of the experiment
        """
        return self._header.get("TIME", None)

    @property
    def sample_time(self):
        """retrieve the programmed sample period

        Args:
            None.

        Returns:
            float: sample period of the potentiostat (in seconds)

        """
        return self._header.get("SAMPLETIME", None)

    @property
    def sample_count(self, curve: int = 0):
        """compute the number of samples collected for the loaded chronoamperometry experiment

        Args:
            curve (int, optional): curve to return (CHRONOA experiments typically only have 1 curve). Defaults to 1.

        Returns:
            int: number of collected samples for the specified curve

        """

        return len(self._curves[curve - 1].index) if len(self.curves) > 0 else 0

    @property
    def current_range_mode(self):
        """retrieve the current range mode used for the experiment

        Args:
            None.

        Returns:
            str: current range mode (e.g., "AUTO", "MANUAL")
        """
        return self._header.get("IERANGEMODE", None)

    @property
    def current_range(self):
        """retrieve the current range used for the experiment

        Args:
            None.

        Returns:
            float: current range used for the experiment (in A)
        """
        return int(self._header.get("IERANGE", None))

    @property
    def vstep1(self):
        """retrieve the first step potential for the experiment

        Args:
            None.

        Returns:
            float: first step potential (in V)
        """
        return self._header.get("VSTEP1", None)

    @property
    def vstep2(self):
        """retrieve the second step potential for the experiment

        Args:
            None.

        Returns:
            float: second step potential (in V)
        """
        return self._header.get("VSTEP2", None)

    @property
    def tstep1(self):
        """retrieve the first step time for the experiment

        Args:
            None.

        Returns:
            float: first step time (in seconds)
        """
        return self._header.get("TSTEP1", None)

    @property
    def tstep2(self):
        """retrieve the second step time for the experiment

        Args:
            None.

        Returns:
            float: second step time (in seconds)
        """
        return self._header.get("TSTEP2", None)

    @property
    def cycle_count(self):
        """retrieve the number of cycles for the experiment

        Args:
            None.

        Returns:
            int: number of cycles
        """
        return self._header.get("CYCLES", None) if "CYCLES" in self._header else None

    @property
    def current_stability(self):
        """retrieve the current stability for the experiment

        Args:
            None.

        Returns:
            float: current stability (in A)
        """
        return self._header.get("IESTAB", None) if "IESTAB" in self._header else None

    @property
    def control_amp_speed(self):
        """retrieve the control amp speed for the experiment

        Args:
            None.

        Returns:
            float: control amp speed (in A/s)
        """
        return self._header.get("CASPEED", None) if "CASPEED" in self._header else None

    @property
    def current_convention(self):
        """retrieve the current convention for the experiment

        Args:
            None.

        Returns:
            str: current convention (e.g., "POSITIVE", "NEGATIVE")
        """
        return self._header.get("CONVENTION", None)
