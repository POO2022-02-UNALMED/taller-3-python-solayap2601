class Control:
  
  def __init__(self):
    self._tv = None
  
  def turnOn (self):
    self._tv._estado = True

  def turnOff (self):
    self._tv._estado = False
  
  def canalUp(self):
    if self._tv._canal<120 and self._tv._canal>0 and self._tv._estado== True:
      self._tv._canal += 1
  
  def canalDown(self):
    if self._tv_canal<121 and self._tv._canal>1 and self._tv._estado== True:
      self._tv._canal -= 1

  def volumenUp(self):
    if self._tv._volumen<7 and self._tv._volumen>=0 and self._tv._estado== True:
      self._tv._volumen += 1
  
  def volumenDown(self):
    if self._tv._volumen<8 and self._tv._volumen>0 and self._tv._estado== True:
      self._tv._volumen -= 1
  
  def setCanal(self, cha):
    if cha<120 and cha>0 and self._tv._estado== True:
      self._tv._canal = cha

  def enlazar(self, tele):
    self._tv = tele
    tele._control = self

  def getTv(self):
    return self._tv

  def setTv(self, tele):
    self._tv = tele
