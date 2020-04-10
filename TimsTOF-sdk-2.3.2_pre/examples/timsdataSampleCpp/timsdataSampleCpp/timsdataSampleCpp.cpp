#include <iostream>
#include <string>
#include <iomanip>
#include "CppSQLite3.h"
#include "timsdata_cpp.h"

#define OUTPUT_PRECISION 8
#define OUTPUT_WIDTH 9

void dumpFrame(timsdata::TimsData& data, int64_t frameId, int scanEnd);

// When you start this test programs, timsdata.dll is usually not found.
// Either copy the DLL into a place where it is found.
// Or add the following line in the project settings unter Debugging/Environment
// PATH=%PATH%;$(SolutionDir)\..\..\win32

// Simple sample program for using the C++ wrapper of the timsdata DLL.
// Please note: this sample is by design very simple, some error handling might be missing.
// Also note: string to/from timsdata are UTF8, this sample does not convert the "native" encoded 
// string to/from UTF-8, it will only work as long as all string only use 7 bit ASCII characters.
int main(int argc, char* argv[])
{
    if(argc != 2)
    {
        std::cerr << "Usage:" << std::endl;
        std::cerr << argv[0] << " <TDF file>" << std::endl;
        return -1;
    }

    std::cout.precision(OUTPUT_PRECISION);

    std::string tdfDirectory(argv[1]);
    std::string tdfFile = tdfDirectory + "\\analysis.tdf";

    try
    {
        // Open the binary file
        timsdata::TimsData data(tdfDirectory);  // NOTE: UTF-8 conversion needed here!

        // Open the database
        CppSQLite3DB db;
        db.open(tdfFile.c_str());  // NOTE: UTF-8 conversion needed here!

        // example: get the number of frames (spectra)
        auto frames = db.execScalar("select count(*) from frames;");

        std::cout << "TDF file " << tdfDirectory << " contains " << frames << " frames." << std::endl;

        // get information about each frame
        auto query = db.execQuery("select Id, Time, NumScans from frames;");

        while(!query.eof())
        {
            auto time     = query.getFloatField("Time");
            auto id       = query.getIntField("Id");
            auto numScans = query.getIntField("NumScans");

            std::cout << "Frame " << id << " has retention time " << time << " seconds" << std::endl;
            dumpFrame(data, id, numScans);

            query.nextRow();
        }
    }
    catch(std::exception& e)
    {
        std::cerr << "Exception: " << e.what() << std::endl;
    }
    catch(CppSQLite3Exception& e)
    {
        std::cerr << "CppSQLite3Exception: " << e.errorMessage() << std::endl;
    }

	return 0;
}


void dumpFrame(timsdata::TimsData& data, int64_t frameId, int scanEnd)
{
    auto scans = data.readScans(frameId, 0, scanEnd);

    // dump part of the data - for this sample dump a maximum of 15 scans
    // and for each of these scan a maximum of 10 data points
    auto maxScan = std::min(size_t(15), scans.getNbrScans());
    for(auto scan = size_t(0); scan < maxScan; ++scan)
    {
        std::cout << "Scan " << scan << std::endl;
        auto maxPeaks = std::min(size_t(10), scans.getNbrPeaks(scan));

        auto xAxis = scans.getScanX(scan);
        auto yAxis = scans.getScanY(scan);

        std::cout << "x (raw) : ";
        for(size_t counter = 0; counter < maxPeaks; ++counter)
        {
            std::cout << std::setw(OUTPUT_WIDTH) << xAxis[counter] << " ";
        }
        std::cout << std::endl;

        std::cout << "x (mass): ";
        std::vector<double> xAxisMasses;
        std::vector<double> indices(xAxis.begin(), xAxis.end());

        data.indexToMz(frameId, indices, xAxisMasses);

        for(size_t counter = 0; counter < maxPeaks; ++counter)
        {
            std::cout << std::setw(OUTPUT_WIDTH) << xAxisMasses[counter] << " ";
        }
        std::cout << std::endl;

        std::cout << "y       : ";
        for(size_t counter = 0; counter < maxPeaks; ++counter)
        {
            std::cout << std::setw(OUTPUT_WIDTH) << yAxis[counter] << " ";
        }
        std::cout << std::endl << std::endl;

    }
}

