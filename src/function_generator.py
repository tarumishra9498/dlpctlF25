import pyvisa
import numpy as np
from pyvisa.resources.serial import SerialInstrument


class FunctionGenerator:
    """
    Class representing an Agilent 33220A function generator connected via USB.
    """

    def __init__(self) -> None:
        self.devices = self.get_instruments()
        self.instrument: SerialInstrument | None = None
        self.rm = pyvisa.ResourceManager()

    def get_instruments(self) -> dict:
        """
        Returns a dict with resources as the keys and idns as the values
        """
        devices = {}
        for resource in self.rm.list_resources():
            try:
                with self.rm.open_resource(resource) as instrument:
                    # linters will complain about using a `Resource` as a `SerialInstrument`
                    # so we assert that it is a SerialInstrument
                    assert instrument is SerialInstrument
                    idn = instrument.query("*IDN?").strip()
                    devices[resource] = idn

            except Exception:
                devices[resource] = "VISA Device (No IDN)"
        return devices

    def select_instrument(self, idn: str) -> None:
        """
        Used to connect instrument with name `idn`
        """
        # Close existing connection
        if self.instrument:
            self.instrument.close()

        instrument = self.rm.open_resource(self.devices[idn])
        assert instrument is SerialInstrument
        self.instrument = instrument

    def __del__(self) -> None:
        if self.instrument:
            self.instrument.close()
