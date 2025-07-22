import pyvisa
import numpy as np
from pyvisa.resources.serial import SerialInstrument


class FunctionGenerator:
    """
    Class representing an Agilent 33220A function generator connected via USB.
    """

    def __init__(self) -> None:
        self.instrument: SerialInstrument | None = None
        self.rm = pyvisa.ResourceManager()

    def select_instrument(
        self, rm: pyvisa.ResourceManager, device: SerialInstrument
    ) -> None:
        """
        Used to connect instrument with name `idn`
        """
        # Close existing connection
        if self.instrument:
            self.instrument.close()

        instrument = rm.open_resource(idn)
        assert instrument is SerialInstrument
        self.instrument = instrument
        self.set_voltage()
        self.set_frequency()
        self.set_function()

    def set_voltage(self, voltage: float) -> None:
        if self.instrument:
            try:
                self.instrument.write("VOLT:UNIT VPP")
                self.instrument.write("VOLT:OFFS 0V")
                self.instrument.write("OUTP:LOAD INF")
                self.instrument.write(f"VOLT {voltage}")
                volt_read = np.float64(self.instrument.query("VOLT?").strip())
                volt_unit = self.instrument.query("VOLT:UNIT?").strip()
                print(f"Current voltage: {volt_read:.4f} {volt_unit}")
            except pyvisa.errors.Error as e:
                print(f"Error setting voltage: {e}")
        else:
            print("Function generator not selected!")

    def set_frequency(self, frequency) -> None:
        if self.instrument:
            try:
                self.instrument.write(f"FREQ {frequency}")
                print(
                    f"Current frequency: {np.float64(self.instrument.query('FREQ?')):.4f} Hz"
                )
            except pyvisa.errors.Error as e:
                print(f"Error setting frequency: {e}")
        else:
            print("Function generator not selected!")

    def set_function(self, function) -> None:
        if self.instrument:
            try:
                self.instrument.write(f"FUNC {function}")
                print(f"Current function: {self.instrument.query('FUNC?').strip()}")
            except pyvisa.errors.Error as e:
                print(f"Error setting function: {e}")
        else:
            print("Function generator not selected!")

    def __del__(self) -> None:
        if self.instrument:
            self.instrument.close()


#            1000-3000 ; 1500 frequency
#            -5v offset
#            peak to peak voltage 12volts or 10v
