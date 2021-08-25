import datetime, sys, itertools, threading, pandas as pd

def csv_to_xlsx():
    file_input = "masterfile.CSV"
    file_input = "E:\\folder download\\Telegram Desktop\\MASTERFILE-104.CSV"
    file_output = "master.xlsx"
    #file_output = pd.ExcelWriter("master.xlsx")
    pd.read_csv(file_input,
                delimiter=";",
                low_memory=False,
                dtype={'NPWP': str,
                    'KD_KPP': str,
                    'KD_CABANG': str,
                    'KODE_POS': str,
                    'NOMOR_TELEPON': str,
                    'EMAIL': str,
                    'NOMOR_IDENTITAS': str,
                    'KODE_KLU': str,
                    'NIP_AR': str,
                    'NIP_JS': str,
                    'NIP_EKS': str}
                ).to_excel(file_output, index=False)
    #file_output.save()

    #lihat_typedata = pd.read_csv(file_input, delimiter=";")
    #print(lihat_typedata.dtypes)

#done = False
#def animate():
#    for c in itertools.cycle(['|', '/', '-', '\\']):
#        if done:
#            break
#        sys.stdout.write('\rTunggu sebentar ' + c)
        #time.sleep(0.1)
    #print('\ndone.')

#berapa lama selesai?
app_start = datetime.datetime.now()

#Start Waiting Proses
#t = threading.Thread(target=animate)
t = threading.Thread(target=csv_to_xlsx())
t.start()


#Waiting Proses
#csv_to_xlsx()

#berapa lama selesai.
app_stop = datetime.datetime.now()
selisih = app_stop - app_start
durasi = divmod(selisih.seconds, 60)
endTime = durasi[0], 'menit', durasi[1], 'detik'

#done = True

print("\n", durasi[0], 'menit', durasi[1], 'detik')
