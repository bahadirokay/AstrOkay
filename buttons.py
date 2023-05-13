from PyQt6.QtWidgets import QListWidget
from test_ui import Ui_AstrOkay
import dbastrokay


"""pushButton komutları test_ui.py dosyasında olduğu için ve hata ile karşılaşmamak için __init__ fonksiyonunu oluşturdum
        Gerekli olup olmadığını bilmiyorum. İlk denememde çalıştığı için programcılığın ilk kuralı olan çalışıyorsa
            dokunma'yı uyguladım ve böylece bıraktım."""
def __init__(self):
    super().__init__()
    self.listWidget = QListWidget(self)
    self.ui = Ui_AstrOkay()
    self.ui.setupUi(self)
    self.ui.retranslateUi(self)


"""lcd number güncellenmesini her fonksiyonda yazamamak için bir fonksiyon oluşturdum. Yapılan işlem veri fonkisyon
    içindeki ilk koda yorum satırı olarak eklenmiştir."""
def lcd(self):
    #veritabanında Light Frame olarak girilen verileri say.
    light_frames_count = len(dbastrokay.get_data('LightFrame'))
    #11 Numaralı Lcd Number'da sayılan veritabanını integer olarak yazdır.
    self.ui.lcdNumber_11.display(light_frames_count)
    flat_frames_count = len(dbastrokay.get_data('FlatFrame'))
    self.ui.lcdNumber_2.display(flat_frames_count)
    dark_frames_count = len(dbastrokay.get_data('DarkFrame'))
    self.ui.lcdNumber_3.display(dark_frames_count)
    darkflat_frames_count = len(dbastrokay.get_data('DarkFlatFrame'))
    self.ui.lcdNumber_4.display(darkflat_frames_count)
    bias_frames_count = len(dbastrokay.get_data('BiasFrame'))
    self.ui.lcdNumber_5.display(bias_frames_count)
    master_flat_frames_count = len(dbastrokay.get_data('MasterFlatFrame'))
    self.ui.lcdNumber_7.display(master_flat_frames_count)
    master_dark_frames_count = len(dbastrokay.get_data('MasterDarkFrame'))
    self.ui.lcdNumber_8.display(master_dark_frames_count)
    master_darkflat_frames_count = len(dbastrokay.get_data('MasterDarkFlatFrame'))
    self.ui.lcdNumber_9.display(master_darkflat_frames_count)
    master_bias_frames_count = len(dbastrokay.get_data('MasterBiasFrame'))
    self.ui.lcdNumber_10.display(master_bias_frames_count)
    mother_frame_count = len(dbastrokay.get_data('MotherFrame'))
    self.ui.lcdNumber_6.display(mother_frame_count)

"""Hangi butonun hangi fonkisyon ile çalıştığını belirliyen fonksiyon ilk satırdaki yorum saturı
    diğerleri içinde geçerlidir."""

def start_button(self):
    self.ui.pushButton_34.clicked.connect(self.start_button)
def frame_button(self):
    #main.py'da bulunan light_frames fonksiyonuna buton ata.
    self.ui.pushButton.clicked.connect(self.light_frames)
    self.ui.pushButton_2.clicked.connect(self.flat_frames)
    self.ui.pushButton_3.clicked.connect(self.dark_frames)
    self.ui.pushButton_4.clicked.connect(self.darkflat_frames)
    self.ui.pushButton_5.clicked.connect(self.bias_frames)
    self.ui.pushButton_16.clicked.connect(self.mother_frames)
    self.ui.pushButton_20.clicked.connect(self.master_darkflat_frames)
    self.ui.pushButton_21.clicked.connect(self.master_dark_frames)
    self.ui.pushButton_32.clicked.connect(self.master_flat_frames)
    self.ui.pushButton_33.clicked.connect(self.master_bias_frames)


"""Hangi clean butonunun hangi fonkisyona atandığını belirten fonkisyon"""
def clean_button(self):
    #Light Frame alanında bulunan clean butonunu işleve koymak için delete_light fonksiyonu tanımla.
    self.ui.pushButton_30.clicked.connect(self.delete_light)
    self.ui.pushButton_10.clicked.connect(self.delete_flat)
    self.ui.pushButton_11.clicked.connect(self.delete_dark)
    self.ui.pushButton_12.clicked.connect(self.delete_darkflat)
    self.ui.pushButton_13.clicked.connect(self.delete_bias)
    self.ui.pushButton_18.clicked.connect(self.delete_mother)
    self.ui.pushButton_26.clicked.connect(self.delete_masterflat)
    self.ui.pushButton_28.clicked.connect(self.delete_masterdark)
    self.ui.pushButton_31.clicked.connect(self.delete_masterdarkflat)
    self.ui.pushButton_22.clicked.connect(self.delete_masterbias)





