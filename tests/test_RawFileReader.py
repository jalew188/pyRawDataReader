from pyRawDataReader.RawFileReader import RawFileReader
import sys

scanNumber = 10000
rawFile = RawFileReader(sys.argv[1])
print("GetFileName: ", rawFile.GetFileName())
print("GetCreatorID: ", rawFile.GetCreatorID())
print("GetCreationDate: ", rawFile.GetCreationDate())
print("GetMaxIntensity: ", rawFile.GetMaxIntensity())
print("GetComment1: ", rawFile.GetComment1())
print("GetComment2: ", rawFile.GetComment2())
print("GetInstName: ", rawFile.GetInstName())

print("GetMSOrderForScanNum: ", rawFile.GetMSOrderForScanNum(scanNumber))
print("GetScanEventForScanNum: ", rawFile.GetScanEventStringForScanNum(scanNumber))
print("GetNumberOfSourceFragmentsFromScanNum: ", rawFile.GetNumberOfSourceFragmentsFromScanNum(scanNumber))
if rawFile.GetNumberOfSourceFragmentsFromScanNum(scanNumber) > 0:
    print("GetSourceFragmentValueFromScanNum: ", rawFile.GetSourceFragmentValueFromScanNum(scanNumber, 0))
if rawFile.GetMSOrderForScanNum(scanNumber) > 1:
    print("GetIsolationWidthForScanNum: ", rawFile.GetIsolationWidthForScanNum(scanNumber))
    print("GetCollisionEnergyForScanNum: ", rawFile.GetCollisionEnergyForScanNum(scanNumber))
    print("GetActivationTypeForScanNum: ", rawFile.GetActivationTypeForScanNum(scanNumber))
    print("GetPrecursorMassForScanNum: ", rawFile.GetPrecursorMassForScanNum(scanNumber))
    print("GetPrecursorRangeForScanNum: ", rawFile.GetPrecursorRangeForScanNum(scanNumber))
print("GetMassAnalyzerTypeForScanNum: ", rawFile.GetMassAnalyzerTypeForScanNum(scanNumber))
print("GetNumberOfMassCalibratorsFromScanNum: ", rawFile.GetNumberOfMassCalibratorsFromScanNum(scanNumber))
print("GetMassCalibrationValueFromScanNum: ", rawFile.GetMassCalibrationValueFromScanNum(scanNumber, 0))
print("GetMassResolution: ", rawFile.GetMassResolution())
print("GetLowMass: ", rawFile.GetLowMass())
print("GetHighMass: ", rawFile.GetHighMass())
print("GetStartTime: ", rawFile.GetStartTime())
print("GetEndTime: ", rawFile.GetEndTime())
print("GetFirstSpectrumNumber: ", rawFile.GetFirstSpectrumNumber())
print("GetLastSpectrumNumber: ", rawFile.GetLastSpectrumNumber())
print("IsProfileScanForScanNum: ", rawFile.IsProfileScanForScanNum(scanNumber))
print("IsCentroidScanForScanNum: ", rawFile.IsCentroidScanForScanNum(scanNumber))

print("RTFromScanNum: ", rawFile.RTFromScanNum(scanNumber))
print("ScanNumFromRT: ", rawFile.ScanNumFromRT(30))
print("RTInSecondsFromScanNum: ", rawFile.RTInSecondsFromScanNum(scanNumber))
print("ScanNumFromRTInSeconds: ", rawFile.ScanNumFromRTInSeconds(30))

print("GetNumberOfMSOrdersFromScanNum: ", rawFile.GetNumberOfMSOrdersFromScanNum(scanNumber))
print("GetBasePeakForScanNum: ", rawFile.GetBasePeakForScanNum(scanNumber))
print("GetTrailerExtraForScanNum: ", rawFile.GetTrailerExtraForScanNum(scanNumber))
print("GetCentroidMassListFromScanNum: ", rawFile.GetCentroidMassListFromScanNum(scanNumber))
rawFile.Close()