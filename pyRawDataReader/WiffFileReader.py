import os
import sys
import numpy as np

# require pythonnet, pip install pythonnet
import clr
from System import String
# sys.path.append("DLLs")
clr.AddReference("WiffFileReader")
from WiffFileReader import WiffFile

from .RawFileReader import DotNetArrayToNPArray
    
class WiffFileReader(object):
    def __init__(self, filename, **kwargs):
        self.filename = os.path.abspath(filename)
        self.filename = os.path.normpath(self.filename)
        try:
            self.source = WiffFile(self.filename)
        except:
            raise IOError(
                "Wiff file '{0}' could not be opened, is the file accessible ?".format(
                    self.filename))
                    
        self.StartTime = self.GetStartTime()
        self.EndTime = self.GetEndTime()
        self.FirstSpectrumNumber = self.GetFirstSpectrumNumber()
        self.LastSpectrumNumber = self.GetLastSpectrumNumber()
        # self.LowMass = self.GetLowMass()
        # self.HighMass = self.GetHighMass()
        # self.MassResolution = self.GetMassResolution()
        self.NumSpectra = self.GetNumSpectra()
        
    def Close(self):
        self.source.Close()

    def GetFileName(self):
        return self.source.GetFileName()

    # INSTRUMENT BEGIN
    def GetInstName(self):
        return self.source.GetInstrumentName()
    # INSTRUMENT END

    def GetScanEventStringForScanNum(self, scanNumber):
        return self.source.GetDescriptionForScanNum(scanNumber)

    def GetIsolationWidthForScanNum(self, scanNumber):
        return self.source.GetIsolationWidth(scanNumber)

    def GetCollisionEnergyForScanNum(self, scanNumber):
        return self.source.GetCollisionEnergyForScanNum(scanNumber)

    def GetActivationTypeForScanNum(self, scanNumber):
        return self.source.ScanInfos[scanNumber].FragmentationType

    def GetMassAnalyzerTypeForScanNum(self, scanNumber):
        return "QTOF"

    def GetDetectorTypeForScanNum(self, scanNumber):
        return "QTOF"

    def GetStartTime(self):
        return self.source.GetStartTime()

    def GetEndTime(self):
        return self.source.GetEndTime()

    def GetNumSpectra(self):
        """Gets the number of spectra acquired by the current controller. For non-scanning devices like
        UV detectors, the number of readings per channel is returned."""
        return self.source.GetNumSpectra()

    def GetFirstSpectrumNumber(self):
        """Gets the first scan or reading number for the current controller. If data has been acquired, this
        value is always one."""
        return self.source.GetFirstSpectrumNumber()

    def GetLastSpectrumNumber(self):
        """Gets the last scan or reading number for the current controller."""
        return self.source.GetLastSpectrumNumber()

    def ScanNumFromRT(self, RT):
        """Returns the closest matching scan number that corresponds to RT for the current controller.
        For non-scanning devices, such as UV, the closest reading number is returned. The value of
        RT must be within the acquisition run time for the current controller. The acquisition run
        time for the current controller may be obtained by calling GetStartTime and GetEndTime."""
        return self.source.GetScanNumFromRetentionTime(RT)

    def ScanNumFromRTInSeconds(self, RTInSeconds):
        """Returns the closest matching scan number that corresponds to RT for the current controller.
        For non-scanning devices, such as UV, the closest reading number is returned. The value of
        RT must be within the acquisition run time for the current controller. The acquisition run
        time for the current controller may be obtained by calling GetStartTime and GetEndTime."""
        return self.ScanNumFromRT(RTInSeconds/60)

    def RTFromScanNum(self, scanNumber):
        """Returns the closest matching run time or retention time that corresponds to scanNumber for
        the current controller. For non-scanning devices, such as UV, the scanNumber is the reading
        number."""
        return self.source.GetRetentionTimeFromScanNum(scanNumber)

    def RTInSecondsFromScanNum(self, scanNumber):
        """Returns the closest matching run time or retention time that corresponds to scanNumber for
        the current controller. For non-scanning devices, such as UV, the scanNumber is the reading
        number."""
        return self.RTFromScanNum(scanNumber)*60

    def IsProfileScanForScanNum(self, scanNumber):
        """Returns TRUE if the scan specified by scanNumber is a profile scan, FALSE if the scan is a
        centroid scan."""
        return True

    def IsCentroidScanForScanNum(self, scanNumber):
        """Returns TRUE if the scan specified by scanNumber is a centroid scan, FALSE if the scan is a
        profile scan."""
        return True

    def GetMSOrderForScanNum(self, scanNumber):
        return self.source.GetMSLevelForScanNum(scanNumber)

    def GetPrecursorMassForScanNum(self, scanNumber):
        return self.source.GetPrecursorMassFromScanNum(scanNumber)
        
    def GetBasePeakForScanNum(self, scanNumber):
        """This function returns the base peak mass and intensity of mass spectrum."""
        base_peak = self.source.GetBasePeakFromScanNum(scanNumber)
        return base_peak.Item1, base_peak.Item2

    def GetProfileMassListFromScanNum(self, scanNumber):
        peak_list = self.source.GetProfileFromScanNum(scanNumber)
        return np.array([DotNetArrayToNPArray(peak_list.Masses, float), DotNetArrayToNPArray(peak_list.Intensities, float)])

    def GetCentroidMassListFromScanNum(self, scanNumber):
        peak_list = self.source.GetCentroidFromScanNum(scanNumber)
        return np.array([DotNetArrayToNPArray(peak_list.Masses, float), DotNetArrayToNPArray(peak_list.Intensities, float)])