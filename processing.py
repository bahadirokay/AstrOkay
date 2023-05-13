import numpy as np
import rawpy
from PIL import Image
from astropy.io import fits
import dbastrokay
import os
from sqlalchemy import create_engine, MetaData, Table, select

def covert_dng_to_png(table_name):
    # Veritabanı bağlantısı yap
    engine = create_engine('sqlite:///astrophotography.db')
    metadata = MetaData()

    # Dosya bilgilerini içeren tabloyu seç
    files = Table(table_name, metadata, autoload=True, autoload_with=engine, sqlite3_pragma_table_info=
                                                                        "pragma_table_info")

    # .dng uzantılı dosyaları seçmek için sorgu yap
    query = select([files]).where(files.c.filename.like("%.dng"))

    # Sorguyu çalıştır
    result_set = engine.execute(query)

    # Her bir dosya için işlem yap
    for row in result_set:
        # Dönüştürülmüş png dosyasının ismini oluştur
        png_filename = os.path.splitext(row.filename)[0] + ".png"

        # Dönüştürme işlemini yap
        im = Image.open(row.path)
        im.save(png_filename)

        # Dng dosyasını veritabanından sil
        delete_query = files.delete().where(files.c.filename == row.filename)
        engine.execute(delete_query)

        # Png dosyasının bilgilerini veritabanına ekle
        insert_query = files.insert().values(filename=png_filename, path=os.path.abspath(png_filename))
        engine.execute(insert_query)


def flat_processing():
    ''''İşlem Adımları:

    Veritabanındaki tüm Flat Frame dosya yollarını al.
    Her bir Flat Frame için aşağıdaki işlemleri yap:
    Dosya yolu ve boyut bilgilerini al.
    .fits uzantılı dosyaları oku ve flat_frame_data değişkenine at.
    .png veya .jpg uzantılı dosyaları oku ve flat_frame_data değişkenine at.
    Flat Frame'i normalize et.
    Flat Frame'i kaydet.'''

    # Veritabanındaki Flat Frame dosya yollarını al
    flat_frames = dbastrokay.get_data('FlatFrame')
    # Flat Frame'leri topla ve normalize et
    master_flat = np.zeros((flat_frames[0][3], flat_frames[0][4]), dtype=np.float32)
    for flat_frame in flat_frames:
        # Dosya yolu ve boyut bilgilerini al
        file_path = flat_frame[2]
        file_size_width = flat_frame[3]
        file_size_height = flat_frame[4]
        # .fits uzantılı dosyaları oku ve normalize et
        if file_path.endswith(('.fits', '.FITS')):
            with fits.open(file_path) as hdul:
                #Oku
                flat_frame_data = hdul[0].data.astype(np.float32)
                #Normalize et
                flat_frame_normalized = flat_frame_data / np.mean(flat_frame_data)
        elif file_path.endswith(('.DNG', '.dng')):
            # Oku
            with rawpy.imread(file_path) as raw:
                # Raw verisini döndürür
                raw_data = raw.raw_image_visible.astype(np.float32)
                # Boyut bilgilerini al
                height, width = raw_data.shape
                # Normalize et
                flat_frame_normalized = raw_data / np.mean(raw_data)
        else:
            #Aç
            with Image.open(file_path) as img:
                #Oku
                flat_frame_data = np.array(img).astype(np.float32)
                #Normalize et(RGB'deb Grayscale'ye çevirir)
                flat_frame_normalized = np.dot(flat_frame_data[..., :3], [0.2989, 0.5870, 0.1140]) / np.mean(
                    flat_frame_data)
        # Flat Frame'leri birleştir
        master_flat += flat_frame_normalized
    # Master Flat'i normalize et
    master_flat /= len(flat_frames)

    # Master Flat'i kaydet
    if not os.path.exists("./master_flat"):
        os.makedirs("./master_flat")
    np.save("./master_flat/master_flat.npy", )
    project_folder = os.path.abspath("./master_flat")
    # Fit uzantılı Dark Flat ismini oluştur
    filename = "master_flat.fits"
    # Proje Klasörü ve İsmini kombine et
    output_path = os.path.join(project_folder, filename)
    hdu = fits.PrimaryHDU(master_flat)
    hdu.writeto(output_path, overwrite=True)
    dbastrokay.add_data('MasterFlatFrame', (filename, output_path, master_flat.shape[1], master_flat.shape[0]))

    #print(dbastrokay.get_folder(''))


def dark_processing():
    # Veritabanındaki Dark Frame dosya yollarını al
    dark_frames = dbastrokay.get_data('DarkFrame')

    # Normalize edilmiş dark frame'leri tutacak listeyi tanımla
    normalized_dark_frames = []

    # Dark Frame'leri işle
    for dark_frame in dark_frames:
        # Dosya yolu ve boyut bilgilerini al
        file_path = dark_frame[2]
        file_size_width = dark_frame[3]
        file_size_height = dark_frame[4]

        # .fits uzantılı dosyaları oku ve analiz et
        if file_path.endswith('.fits'):
            with fits.open(file_path) as hdul:
                # Oku
                dark_frame_data = hdul[0].data.astype(np.float32)
        elif file_path.endswith(('.DNG', '.dng')):
            # Oku
            with rawpy.imread(file_path) as raw:
                # Raw verisini döndürür
                raw_data = raw.raw_image_visible.astype(np.float32)
                # Boyut bilgilerini al
                height, width = raw_data.shape
                # Normalize et
                dark_frame_data = raw_data / np.mean(raw_data)
        else:
            # .png veya .jpg uzantılı dosyaları oku
            with Image.open(file_path) as img:
                # RGB'yi Grayscale'e dönüştür ve oku
                gray_img = img.convert('L')
                dark_frame_data = np.array(gray_img).astype(np.float32)

        # Dark frame'leri normalize et ve listeye ekle
        dark_frame_normalized = dark_frame_data / np.mean(dark_frame_data)
        normalized_dark_frames.append(dark_frame_normalized)

    # Normalize edilmiş tüm dark frame'leri topla
    master_dark_frame_normalized = np.mean(normalized_dark_frames, axis=0)

    # Master dark frame'i kaydet
    if not os.path.exists("./master_dark"):
        os.makedirs("./master_dark")
    master_dark_frame_name = "./master_dark/master_dark_frame.npy"
    np.save(master_dark_frame_name, master_dark_frame_normalized)
    project_folder = os.path.abspath("./master_dark")
    # Fit uzantılı Dark Flat ismini oluştur
    filename = "master_dark.fits"
    # Proje Klasörü ve İsmini kombine et
    output_path = os.path.join(project_folder, filename)
    hdu = fits.PrimaryHDU(master_dark_frame_normalized)
    hdu.writeto(output_path, overwrite=True)
    dbastrokay.add_data('MasterDarkFrame', (filename, output_path, master_dark_frame_normalized.shape[0],
                                            master_dark_frame_normalized.shape[1]))

def dark_flat_processing():
    """
    Veritabanındaki Flat Frame ve Dark Frame'leri kullanarak Dark Flat'i oluşturur.

    Parameters
    ----------
    'database_file_path : str
        Veritabanı dosyasının yolu.

    Returns
    -------
    dark_flat : numpy.ndarray
        Oluşturulan Dark Flat verisi.'
    """

    # Veritabanındaki Flat Frame dosya yollarını al
    flat_frames = dbastrokay.get_data('FlatFrame')

    # Veritabanındaki Dark Frame dosya yollarını al
    dark_frames = dbastrokay.get_data('DarkFrame')

    # Flat Frame'leri işle
    flat_data_list = []
    for flat_frame in flat_frames:
        # Dosya yolu ve boyut bilgilerini al
        file_path = flat_frame[2]
        file_size_width = flat_frame[3]
        file_size_height = flat_frame[4]

        # .fits uzantılı dosyaları oku ve normalize et
        if file_path.endswith('.fits'):
            #Aç
            with fits.open(file_path) as hdul:
                #Oku
                flat_frame_data = hdul[0].data.astype(np.float32)
                #Normalize et
                flat_frame_normalized = flat_frame_data / np.mean(flat_frame_data)
        elif file_path.endswith(('.DNG', '.dng')):
            # Oku
            with rawpy.imread(file_path) as raw:
                # Raw verisini döndürür
                raw_data = raw.raw_image_visible.astype(np.float32)
                # Boyut bilgilerini al
                height, width = raw_data.shape
                # Normalize et
                flat_frame_normalized = raw_data / np.mean(raw_data)
        # .png veya .jpg uzantılı dosyaları oku
        else:
            #Aç
            with Image.open(file_path) as img:
                #Oku
                flat_frame_data = np.array(img).astype(np.float32)
                #RGB'yi Grayscale'ye çevir ve Normalize et
                flat_frame_normalized = np.dot(flat_frame_data[..., :3], [0.2989, 0.5870, 0.1140]) / np.mean(
                    flat_frame_data)

        # Boyutları uyumlu hale getir
        flat_frame_resized = np.array(Image.fromarray(flat_frame_normalized)
                                      .resize((file_size_width, file_size_height)))
        flat_data_list.append(flat_frame_resized)
    # Tüm Flat Frame'leri birleştir ve ortalamasını alarak Master Flat'i oluştur
    master_flat = np.mean(flat_data_list, axis=0)

    # Dark Frame'leri işle
    dark_data_list = []
    for dark_frame in dark_frames:
        # Dosya yolu ve boyut bilgilerini al
        file_path = dark_frame[2]
        file_size_width = dark_frame[3]
        file_size_height = dark_frame[4]

        # .fits uzantılı dosyaları oku
        if file_path.endswith('.fits'):
            #Aç
            with fits.open(file_path) as hdul:
                #Oku
                dark_frame_data = hdul[0].data.astype(np.float32)
                #Normalize et
                dark_frame_resized = np.array(
                    Image.fromarray(dark_frame_data).resize((file_size_width, file_size_height)))
        elif file_path.endswith(('.DNG', '.dng')):
            # Oku
            with rawpy.imread(file_path) as raw:
                # Raw verisini döndürür
                raw_data = raw.raw_image_visible.astype(np.float32)
                # Boyut bilgilerini al
                height, width = raw_data.shape
                # Normalize et
                dark_frame_resized = raw_data / np.mean(raw_data)
        # .png veya .jpg uzantılı dosyaları oku
        else:
            #Aç
            with Image.open(file_path) as img:
                #Oku
                dark_frame_data = np.array(img).astype(np.float32)
                #RGB'yi Graysclaye'ye çevir ve normalize et
                dark_frame_resized = np.dot(dark_frame_data[..., :3], [0.2989, 0.5870, 0.1140]) / np.mean(
                    dark_frame_data)
        #Normalize dosyaları listeye ekle
        dark_data_list.append(dark_frame_resized)
    # Tüm Dark Frame'leri birleştir ve ortalamasını alarak Master Dark'ı oluştur
    master_dark = np.mean(dark_data_list, axis=0)
    # Master Flat'i Master Dark ile bölerek Dark Flat'i oluştur
    dark_flat = master_flat / master_dark
    # Dark Flat'i fits formatında kaydet
    # Proje Klasörünü seç
    if not os.path.exists("./dark_flat"):
        os.makedirs("./dark_flat")
    np.save("./dark_flat/dark_flat.npy", dark_flat)
    project_folder = os.path.abspath("./dark_flat")
    # Fit uzantılı Dark Flat ismini oluştur
    filename = "dark_flat.fits"
    # Proje Klasörü ve İsmini kombine et
    output_path = os.path.join(project_folder, filename)
    # Dark Flat'i fits formatında kaydet
    hdu = fits.PrimaryHDU(dark_flat)
    hdu.writeto(output_path, overwrite=True)
    dbastrokay.add_data('MasterDarkFlatFrame', (filename, output_path, dark_flat.shape[1], dark_flat.shape[0]))
    return dark_flat

def bias_processing():
    """
    Veritabanındaki Bias Frame'leri kullanarak Master Bias'i oluşturur ve fits formatında kaydeder.

    Parameters
    ----------
    'database_file_path : str
        Veritabanı dosyasının yolu.
    'output_path : str
        Kaydedilecek Master Bias dosyasının yolu.

    Returns
    -------
    master_bias : numpy.ndarray
        Oluşturulan Master Bias verisi.'
    """

    # Veritabanındaki Bias Frame dosya yollarını al
    bias_frames = dbastrokay.get_data('BiasFrame')

    # Bias Frame'leri işle
    bias_data_list = []
    for bias_frame in bias_frames:
        # Dosya yolu ve boyut bilgilerini al
        file_path = bias_frame[2]
        file_size_width = bias_frame[3]
        file_size_height = bias_frame[4]

        # .fits uzantılı dosyaları oku
        if file_path.endswith('.fits'):
            #Aç
            with fits.open(file_path) as hdul:
                #Oku
                bias_frame_data = hdul[0].data.astype(np.float32)
                #Normalize Et
                bias_frame_resized = np.array(
                    Image.fromarray(bias_frame_data).resize((file_size_width, file_size_height)))
        elif file_path.endswith(('.DNG', '.dng')):
            # Oku
            with rawpy.imread(file_path) as raw:
                # Raw verisini döndürür
                raw_data = raw.raw_image_visible.astype(np.float32)
                # Boyut bilgilerini al
                width, height = raw_data.shape
                # Normalize et
                bias_frame_resized = raw_data / np.mean(raw_data)
        # .png veya .jpg uzantılı dosyaları oku
        else:
            #Aç
            with Image.open(file_path) as img:
                #Oku
                bias_frame_data = np.array(img).astype(np.float32)
                #RGB'den Grayscale'ye çevir ve normalize et
                bias_frame_resized = np.dot(bias_frame_data[..., :3], [0.2989, 0.5870, 0.1140]) / np.mean(
                    bias_frame_data)
        #Listeye ekle
        bias_data_list.append(bias_frame_resized)

    # Tüm Bias Frame'leri birleştir ve ortalamasını alarak Master Bias'i oluştur
    master_bias = np.mean(bias_data_list, axis=0)
    if not os.path.exists("./master_bias"):
        os.makedirs("./master_bias")
    np.save("./master_bias/master_bias.npy", master_bias)
    project_folder = os.path.abspath("./master_bias")
    # Fit uzantılı Dark Flat ismini oluştur
    filename = "master_bias.fits"
    # Proje Klasörü ve İsmini kombine et
    output_path = os.path.join(project_folder, filename)
    hdu = fits.PrimaryHDU(master_bias)
    hdu.writeto(output_path, overwrite=True)
    dbastrokay.add_data('MasterBiasFrame', (filename, output_path, master_bias.shape[1], master_bias.shape[0]))
    return master_bias

def light_frame_processing():
    """
    Veritabanındaki Light Frame'leri işleyerek, Master Dark, Master Flat, Dark Flat ve Master Bias kullanarak işlenmiş
    verileri kaydeder.

    Parameters
    ----------
    'database_file_path : str
        Veritabanı dosyasının yolu.
    'output_path : str
        İşlenmiş verilerin kaydedileceği klasörün yolu.

    Returns
    -------
    processed_data : list
        İşlenmiş verilerin dosya yollarını içeren bir liste.
    """

    # Veritabanından LightFrame'leri al
    light_frames = dbastrokay.get_data('LightFrame')

    processed_data = []

    master_dark_file_name = 'master_dark.fits'
    master_dark_folder_path = os.path.abspath('./master_dark')
    master_dark_file_path = os.path.join(master_dark_folder_path, master_dark_file_name)
    with fits.open(master_dark_file_path) as hdul:
        master_dark = hdul[0].data.astype(np.float32)

    if os.path.exists("./master_flat"):
        # Master Flat'ı al
        master_dark_file_name = 'master_flat.fits'
        master_dark_folder_path = os.path.abspath('./master_flat')
        master_flat_file_path = os.path.join(master_dark_folder_path, master_dark_file_name)
        with fits.open(master_flat_file_path) as hdul:
            master_flat = hdul[0].data.astype(np.float32)
    elif os.path.exists("./dark_flat"):
        # Dark Flat'ı al
        master_dark_file_name = 'dark_flat.fits'
        master_dark_folder_path = os.path.abspath('./dark_flat')
        dark_flat_file_path = os.path.join(master_dark_folder_path, master_dark_file_name)
        with fits.open(dark_flat_file_path) as hdul:
            dark_flat = hdul[0].data.astype(np.float32)
    elif os.path.exists("./master_bias"):
        # Master Bias'ı al
        master_dark_file_name = 'master_bias.fits'
        master_dark_folder_path = os.path.abspath('./master_bias')
        master_bias_file_path = os.path.join(master_dark_folder_path, master_dark_file_name)
        with fits.open(master_bias_file_path) as hdul:
            master_bias = hdul[0].data.astype(np.float32)

    # LightFrame'leri işle
    for light_frame in light_frames:
        # Dosya yolu ve boyut bilgilerini al
        file_path = light_frame[2]
        file_size_width = light_frame[3]
        file_size_height = light_frame[4]

        # .fit uzantılı dosyaları oku
        if file_path.endswith('.fit'):
            with fits.open(file_path) as hdul:
                light_frame_data = hdul[0].data.astype(np.float32)
        elif file_path.endswith(('.DNG', '.dng')):
            # Oku
            with rawpy.imread(file_path) as raw:
                # Raw verisini döndürür
                raw_data = raw.raw_image_visible.astype(np.float32)
                # Boyut bilgilerini al
                height, width = raw_data.shape
                # Normalize et
                light_frame_data = raw_data / np.mean(raw_data)

        # .png, .jpg gibi resim dosyaları oku
        else:
            image = Image.open(file_path)
            light_frame_data = np.array(image).astype(np.float32)

        # Dark Frame'i çıkar
        if os.path.exists('./master_dark'):
            light_frame_data -= master_dark
        # Flat Field'ı uygula
        elif os.path.exists('./master_bias'):
            light_frame_data -= master_bias
        elif os.path.exists('/master_flat'):
            light_frame_data /= master_flat
            light_frame_data *= np.median(master_flat)

        if os.path.exists('./dark_flat'):
            # Dark Flat'ı uygula
            light_frame_data /= dark_flat

        # 0-1 arasına normalize et
        light_frame_data /= np.max(light_frame_data)

        # İşlenmiş veriyi kaydet
        file_name = "sonunda"
        output_file_path = os.path.join(file_name)

        """# Eğer dosya .fits uzantılı ise
        if file_path.endswith('.fits'):
            hdul[0].data = light_frame_data
            os.path.join(dbastrokay.get_folder('FolderName'), output_file_path)
            hdul.writeto(output_file_path, overwrite=True)
        else:
            # Resim dosyaları için kayıt işlemi
            os.path.join(dbastrokay.get_folder('FolderName'), output_file_path)
            im = Image.fromarray(light_frame_data.astype('uint8'))
            im.save(output_file_path)"""
        if file_path.endswith('.fits'):
            hdul[0].data = light_frame_data
            my_path = "/Users/bahadirokay/Desktop"
            output_file_path = my_path + output_file_path.split("/")[-1]
            hdul.writeto(output_file_path, overwrite=True)
        else:
            # Resim dosyaları için kayıt işlemi
            path = dbastrokay.get_folder('FolderName')
            if path is None:
                print('Klasör bulunamadı')
            else:
                print('Klasör bulundu')
            output_file_path = os.path.join(path, os.path.basename(output_file_path))
            im = Image.fromarray(light_frame_data.astype('uint8'))
            im.save(output_file_path)

            print('işlem tamamlandı.')

            # İşlenmiş verinin dosya yolunu listeye ekle
        processed_data.append(output_file_path)

        return processed_data

    return processed_data
