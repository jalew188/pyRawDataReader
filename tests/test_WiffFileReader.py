from pyRawMSDataReader.WiffFileReader import WiffFileReader
import sys

scanNumber = 10000
rawFile = WiffFileReader(sys.argv[1])
print("GetFileName: ", rawFile.GetFileName())
print("GetInstName: ", rawFile.GetInstName())

print("GetMSOrderForScanNum: ", rawFile.GetMSOrderForScanNum(scanNumber))
print("GetScanEventForScanNum: ", rawFile.GetScanEventStringForScanNum(scanNumber))
if rawFile.GetMSOrderForScanNum(scanNumber) > 1:
    print("GetIsolationWidthForScanNum: ", rawFile.GetIsolationWidthForScanNum(scanNumber))
    print("GetCollisionEnergyForScanNum: ", rawFile.GetCollisionEnergyForScanNum(scanNumber))
    print("GetActivationTypeForScanNum: ", rawFile.GetActivationTypeForScanNum(scanNumber))
    print("GetPrecursorMassForScanNum: ", rawFile.GetPrecursorMassForScanNum(scanNumber))
    print("IsolationCenter: ", rawFile.source.GetScanInfo(scanNumber).IsolationCenter)
print("GetMassAnalyzerTypeForScanNum: ", rawFile.GetMassAnalyzerTypeForScanNum(scanNumber))
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

print("GetBasePeakForScanNum: ", rawFile.GetBasePeakForScanNum(scanNumber))
print("GetCentroidMassListFromScanNum: ", rawFile.GetCentroidMassListFromScanNum(scanNumber))
print("GetCentroidMassListFromScanNum: ", rawFile.GetProfileMassListFromScanNum(scanNumber))
rawFile.Close()