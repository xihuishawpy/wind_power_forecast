import os

with open('prepare_origin2.py') as f:
    origin_prep = f.read()

dic = {
    'HH': [2, 4, 7],
    'HID_SZ1': [64],
    'HID_SZ2': [8, 16],
    'OUT': [108, 216],
    'PARTIAL_DATA': ['None', 140],
    'ATTN': ['True', 'False']
}
for key in dic:
    dic[key] = [str(x) if type(x)==int else x for x in dic[key]]
print(dic)
for HH in dic['HH']:
    for HID_SZ1 in dic['HID_SZ1']:
        for HID_SZ2 in dic['HID_SZ2']:
            for OUT in dic['OUT']:
                for PARTIAL_DATA in dic['PARTIAL_DATA']:
                    for ATTN in dic['ATTN']:
                        surfix = f'HHTMP_{HH}_HD1_{HID_SZ1}_HD2_{HID_SZ2}_OUT_{OUT}_PD_{PARTIAL_DATA}_AT_{ATTN}'

                        text = origin_prep.replace('HH', HH).replace('HIDSZ1', HID_SZ1).replace('HIDSZ2', 
                        HID_SZ2).replace('OUT', OUT).replace('PARTIAL_DATA', PARTIAL_DATA).replace('ATTN', ATTN)
                        prep_file = f"prep_{surfix}.py"
                        run_file = f'run_{surfix}.sh'
                        submit_file = f'falcon_submit_{surfix}.sh'
                        log_file = f'logs/log_{surfix}.txt'
                        with open(prep_file, 'w') as f:
                            f.write(text)
                        with open(run_file, 'w') as f:
                            f.write(f"python3 pipeline.py {prep_file} > {log_file} 2>&1")
                    
