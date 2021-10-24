from Tests.testCRUD import testAdaugaLibrarie, testStergeLibrarie, testModificaLibrarie
from Tests.testDomain import testLibrarie


def runAllTests():
    testLibrarie()
    testAdaugaLibrarie()
    testStergeLibrarie()
    testModificaLibrarie()