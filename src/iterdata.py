import openpyxl

class IterData():
 def __init__(self, raw):
  self._raw = raw
  self._dataSet1 = None
  self._dataSet2 = None
  self._trnsData = None
  self._feeTypeMapping = None
 
 def iterRead(self):
  wb = openpyxl.load_workbook(filename=self._raw, read_only=True)
  dataSet1 = 'Data Set 1'
  dataSet2 = 'Data Set 2'
  trnsData = 'Trns Data'
  feeTypeMapping = 'Fee Type Mapping'
  
  self._dataSet1 = wb[dataSet1] 
  self._dataSet2 = wb[dataSet2]
  self._trnsData = wb[trnsData]
  self._feeTypeMapping = wb[feeTypeMapping]
 
  





