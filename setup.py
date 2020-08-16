import setuptools
import distutils.sysconfig
from distutils.command import install, build, build_ext, install_data, install_lib
import os

# package .dll files into "site-packages", making .dll files visible for python and clr (pythonnet)
# this class and cmdclass is modified from pythonnet setup.py (for Python.Runtime.dll)
class InstallDataPythonnet(install_data.install_data):
    def run(self):
        install_cmd = self.get_finalized_command("install")
        install_platlib = os.path.relpath(install_cmd.install_platlib, self.install_dir)
        print(install_platlib)
        for i, data_files in enumerate(self.data_files):
            if isinstance(data_files, str):
                pass
            else:
                dest = data_files[0].format(install_platlib=install_platlib)
                self.data_files[i] = dest, data_files[1]

        return install_data.install_data.run(self)

cmdclass={
    "install_data": InstallDataPythonnet,
    # "install": InstallPythonnet,
    # "build_ext": BuildExtPythonnet,
    # "install_lib": InstallLibPythonnet,
}

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyRawMSFileReader",
    version="0.0.1",
    author="Zeng, Wen-Feng",
    author_email="jalew.zwf@qq.com",
    description="Accessing Raw/Wiff/... mass spectrum raw files using python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jalew188/pyRawDataReader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=["pythonnet"],
    cmdclass=cmdclass,
    data_files=[('{install_platlib}',
        [
        # "DLLs/WiffFileReader.dll",
        # "DLLs/SciexToolKit.dll",
        "DLLs/ThermoFisher.CommonCore.Data.dll",
        "DLLs/ThermoFisher.CommonCore.RawFileReader.dll",
        # "DLLs/Clearcore2.Domain.Acquisition.Methods.MassSpec.dll",
        # "DLLs/Sciex.FMan.dll",
        # "DLLs/Clearcore2.Data.dll",
        # "DLLs/Clearcore2.RawXYProcessing.dll",
        # "DLLs/Sciex.Data.Processing.dll",
        # "DLLs/Sciex.Data.SimpleTypes.dll",
        # "DLLs/Sciex.Data.XYData.dll",
        # "DLLs/Clearcore2.InternalRawXYProcessing.dll",
        # "DLLs/Clearcore2.Utility.dll",
        # "DLLs/Clearcore2.Data.Acquisition.Client.dll",
        # "DLLs/Clearcore2.Data.Client.dll",
        # "DLLs/Clearcore2.DataService.dll",
        # "DLLs/Clearcore2.Data.Common.dll",
        # "DLLs/Clearcore2.Data.AnalystDataProvider.dll",
        # "DLLs/Sciex.Clearcore.FMan.dll",
        # "DLLs/Clearcore2.Data.WiffReader.dll",
        # "DLLs/Clearcore2.Data.Acquisition.Contracts.dll",
        # "DLLs/Clearcore2.Data.Core.dll",
        # "DLLs/Clearcore2.Data.Contracts.dll",
        # "DLLs/Clearcore2.Data.Wiff2.dll",
        # "DLLs/Clearcore2.StructuredStorage.dll",
        # "DLLs/Sciex.Wiff.dll",
        # "DLLs/Clearcore2.Compression.dll",
        # "DLLs/Clearcore2.Domain.Acquisition.dll",
        # "DLLs/Clearcore2.Data.CommonInterfaces.dll",
        # "DLLs/Clearcore2.Infrastructure.dll",
        # "DLLs/Clearcore2.UserLog.Types.dll",
        # "DLLs/Clearcore2.Muni.dll",
        # "DLLs/Clearcore2.Devices.Types.dll",
        # "DLLs/Clearcore2.XmlHelpers.dll",
        # "DLLs/Clearcore.Licensing.dll",
        # "DLLs/Clearcore2.Processing.dll",
        # "DLLs/Clearcore2.ProjectUtilities.dll",
        # "DLLs/timsdata.dll",
        # "DLLs/libtimsdata.so",
        ])],
)