import os
import sys
import numpy as np

# require pythonnet, pip install pythonnet
import clr
from System import String, List
# sys.path.append("DLLs")
clr.AddReference("WiffFileReader")
import WiffFileReader

from .RawFileReader import DotNetArrayToNPArray
    
class WiffFileReader(object):
    def __init__(self, filename, **kwargs):
        self.filename = os.path.abspath(filename)
        self.filename = os.path.normpath(self.filename)
        
        self.source = WiffFileReader.wiffFile(self.filename)

        if not self.source.IsOpen:
            raise IOError(
                "RAWfile {0} could not be opened, is the file accessible ?".format(
                    self.filename))
                    
        self.StartTime = self.GetStartTime()
        self.EndTime = self.GetEndTime()
        self.FirstSpectrumNumber = self.GetFirstSpectrumNumber()
        self.LastSpectrumNumber = self.GetLastSpectrumNumber()
        self.LowMass = self.GetLowMass()
        self.HighMass = self.GetHighMass()
        # self.MassResolution = self.GetMassResolution()
        self.NumSpectra = self.GetNumSpectra()
        
    