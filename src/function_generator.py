import pyvisa
import numpy as np
from pyvisa.resources import USBInstrument


class FunctionGenerator:
    """
    Class representing an Agilent 33220A function generator connected via USB.
    """

    def __init__(self) -> None:
        self.instrument: USBInstrument | None = None
        self.rm = pyvisa.ResourceManager()
        self.PEAK_TO_PEAK = 10  # volts

    def select_instrument(self, rm: pyvisa.ResourceManager, resource_name) -> None:
        """
        Used to connect instrument with resource name 
        """
        # Close existing connection
        if self.instrument:
            self.instrument.close()

        instrument = rm.open_resource(resource_name)
        self.instrument = instrument
        self.set_voltage(0)
        self.set_frequency(1500)
        self.set_function("SIN")

    def set_voltage(self, voltage: float) -> None:
        if self.instrument:
            try:
                self.instrument.write("VOLT:UNIT VPP")
                self.instrument.write("VOLT:OFFS -5V")
                self.instrument.write("OUTP:LOAD INF")
                self.instrument.write(f"VOLT {voltage}")
                volt_read = np.float64(self.instrument.query("VOLT?").strip())
                volt_unit = self.instrument.query("VOLT:UNIT?").strip()
                print(f"Current voltage: {volt_read:.4f} {volt_unit}")
            except pyvisa.errors.Error as e:
                print(f"Error setting voltage: {e}")
        else:
            print("Function generator not selected!")

    def set_frequency(self, frequency: int) -> None:
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

    def set_function(self, function: str) -> None:
        # function can be something like SQU or SIN
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
#            peak to peak voltage 12volts or 10v
