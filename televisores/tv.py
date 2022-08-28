class TV:
  
  _numTV = 40
  
  def __init__(self, marca, estado):
    self._marca = marca
    self._estado = estado
    self._canal = 1
    self._volumen = 1
    self._precio = 500
    self._control = None
  
  def getMarca(self):
    return self._marca
  
  def setMarca(self,name):
    self._marca = name
  
  def getControl(self):
    return self._control
  
  def setControl(self,con):
    self._control = con

  def getPrecio(self):
    return self._precio
  
  def setPrecio(self,cost):
    self._precio = cost

  def getVolumen(self):
    return self._volumen
  
  def setVolumen(self,vol):
    self._volumen = vol

  def getCanal(self):
    return self._canal
  
  def setCanal(self,chan):
    self._canal = chan
  
  def turnOn (self):
    self._estado = True

  def turnOff (self):
    self._estado = False
  
  def getEstado (self):
    return self._estado
  
  def canalUp(self):
    if self._canal<120 and self._canal>0 and self._estado== True:
      self._canal += 1
  
  def canalDown(self):
    if self._canal<121 and self._canal>1 and self._estado== True:
      self._canal -= 1

  def volumenUp(self):
    if self._volumen<7 and self._volumen>=0 and self._estado== True:
      self._volumen += 1

  def volumenDown(self):
    if self._volumen<8 and self._volumen>0 and self._estado== True:
      self._volumen -= 1

  @classmethod
  def getNumTV(cls):
    return cls._numTV

  @classmethod
  def setNumTV(cls, num):
    cls._numTV = num

