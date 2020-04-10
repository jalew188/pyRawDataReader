
import sys

if len(sys.argv) < 2:
    raise RuntimeError("need arguments: tdf_directory")

analysis_dir = sys.argv[1]
if sys.version_info.major == 2:
    analysis_dir = unicode(analysis_dir)

import timsdata, sqlite3, sys, time
import numpy as np, matplotlib.pyplot as plt

tdf = timsdata.TimsData(analysis_dir)
conn = tdf.conn

def addPeaksOntoDenseProfile (indices, intensities, profile, index_range):
    for index, intensity in zip(indices, intensities):
        if index < index_range[0]:
            continue
        if index >= index_range[1]:
            break
        profile[index - index_range[0]] += intensity

def getDenseMsMsProfileForPrecursor (tdf, precursor_id, mz_index_range):
    profile_length = mz_index_range[1] - mz_index_range[0]
    profile = np.zeros(shape=profile_length, dtype=np.uint64)

    for slice in tdf.conn.execute("SELECT Frame, ScanNumBegin, ScanNumEnd FROM PasefFrameMsMsInfo "
                                  "WHERE Precursor = {0}".format(precursor_id)):
        for scan in tdf.readScans(slice[0], slice[1], slice[2]):
            addPeaksOntoDenseProfile(scan[0], scan[1], profile, mz_index_range)

    return profile

mz_index_range = (0, 400000)
profile = getDenseMsMsProfileForPrecursor(tdf, 87305, mz_index_range)

if False:
    # print sparse representation to console
    print(len(profile))
    for i, intensity in enumerate(profile):
        if intensity != 0:
            print(i, intensity)

index_axis = np.arange(*mz_index_range, dtype=np.float64)
profile_mz = tdf.indexToMz(1, index_axis)

plt.plot(profile_mz, profile)
#plt.plot(index_axis, profile)

plt.show()
