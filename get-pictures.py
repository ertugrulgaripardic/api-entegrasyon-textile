import xml.etree.ElementTree as ET
import openpyxl

def parse_xml_to_excel(xml_file, excel_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Yeni bir Excel çalışma kitabı oluştur
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Ürün Resimleri"

    # Başlıkları yaz
    ws.append(["UrunKartiID", "Resim1", "Resim2", "Resim3", "Resim4", "Resim5", "Resim6", "Resim7", "Resim8", "Resim9", "Resim10", "Resim11", "Resim12", "Resim13"])

    for urun in root.findall('.//Urun'):
        urun_karti_id = urun.find('UrunKartiID').text
        resimler = urun.findall('.//Resimler/Resim')
        resim_urls = [resim.text for resim in resimler]
        
        # Ürün Kartı ID ve resim URL'lerini yaz
        row = [urun_karti_id] + resim_urls
        ws.append(row)

    # Excel dosyasını kaydet
    wb.save(excel_file)

# Kullanım
xml_file = 'urunler.xml'  # XML dosyasının yolu
excel_file = 'urunler_resimler.xlsx'  # Kaydedilecek Excel dosyasının adı
parse_xml_to_excel(xml_file, excel_file)
