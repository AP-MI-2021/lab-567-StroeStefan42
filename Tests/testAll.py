from Tests.testCRUD import testAdaugaLibrarie, testStergeLibrarie, testModificaLibrarie, testGetById
from Tests.testDomain import testLibrarie
from Tests.testFunctionalitati import testDiscount, testModificareGen, testPretMinim, testOrdonareDupaPret, testNrTitluriPeGen
from Tests.testUndo_Redo import test_undo_redo

def runAllTests():
    testLibrarie()
    testAdaugaLibrarie()
    testStergeLibrarie()
    testModificaLibrarie()
    testGetById()
    testDiscount()
    testModificareGen()
    testPretMinim()
    testOrdonareDupaPret()
    testNrTitluriPeGen()
    test_undo_redo()