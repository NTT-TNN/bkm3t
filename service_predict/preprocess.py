import numpy as np
import json
import pandas as pd
import utils


def parse_data(raw_data):
    """
    convert from string list of data to array of data
    :param raw_data: string of list dict data :
    [{'yaw': -157.6705, 'pitch': -4.33582, 'roll': -2.451883, 'Ax': 0, 'Ay': 485, 'Az': 7381, 'timestamps': 1542884104.3810017},
    {'yaw': -157.7411, 'pitch': -4.701654, 'roll': -1.870299, 'Ax': -53, 'Ay': 630, 'Az': 7189, 'timestamps': 1542884104.3893933},
    {'yaw': -157.8128, 'pitch': -5.099143, 'roll': -1.229501, 'Ax': -92, 'Ay': 793, 'Az': 6948, 'timestamps': 1542884104.3895116},
    {'yaw': -157.888, 'pitch': -5.491229, 'roll': -0.536322, 'Ax': -101, 'Ay': 972, 'Az': 6662, 'timestamps': 1542884104.3895922},
    {'yaw': -157.9806, 'pitch': -5.876004, 'roll': 0.203376, 'Ax': -78, 'Ay': 1154, 'Az': 6383, 'timestamps': 1542884104.3896697}]
    :return: dataframe of data
    """
    raw_data = raw_data.replace('[', '')
    raw_data = raw_data.replace(']', '')
    raw_data = raw_data.replace('}, {', "};{")
    raw_data = raw_data.replace("'", '"')
    raw_data = raw_data.replace('}\n{', '};{')
    print("===================", raw_data)
    lines = raw_data.split(';')

    data = dict({'timestamps': [],
                 'yaw': [],
                 'pitch': [],
                 'roll': [],
                 'ax': [],
                 'ay': [],
                 'az': []})
    for line in lines:
        try:
            line_json = json.loads(line)
            print(line_json)
        except Exception as e:
            print(e)
            continue

        data['timestamps'].append(line_json['timestamps'])
        data['yaw'].append(line_json['yaw'])
        data['pitch'].append(line_json['pitch'])
        data['roll'].append(line_json['roll'])
        data['ax'].append(line_json['Ax'] / 1638)
        data['ay'].append(line_json['Ay'] / 1638)
        data['az'].append(line_json['Az'] / 1638)

    results = pd.DataFrame(data)
    return results


def get_signal(raw_data):
    timestamps = raw_data['timestamps']

    accx = raw_data['ax'].values
    accy = raw_data['ay'].values
    accz = raw_data['az'].values

    acc_jerk_x = utils.jerk(accx, timestamps)
    acc_jerk_y = utils.jerk(accy, timestamps)
    acc_jerk_z = utils.jerk(accz, timestamps)

    gyrox = raw_data['roll'].values
    gyroy = raw_data['pitch'].values
    gyroz = raw_data['yaw'].values

    gyro_jerk_x = utils.jerk(gyrox, timestamps)
    gyro_jerk_y = utils.jerk(gyroy, timestamps)
    gyro_jerk_z = utils.jerk(gyroz, timestamps)

    acc_mag = utils.magnitude(accx, accy, accz)
    acc_jerk_mag = utils.magnitude(acc_jerk_x, acc_jerk_y, acc_jerk_z)
    gyro_mag = utils.magnitude(gyrox, gyroy, gyroz)
    gyro_jerk_mag = utils.magnitude(gyro_jerk_x, gyro_jerk_y, gyro_jerk_z)

    faccx = utils.fft(accx)
    faccy = utils.fft(accy)
    faccz = utils.fft(accz)

    facc_jerk_x = utils.fft(acc_jerk_x)
    facc_jerk_y = utils.fft(acc_jerk_y)
    facc_jerk_z = utils.fft(acc_jerk_z)

    fgyrox = utils.fft(gyrox)
    fgyroy = utils.fft(gyroy)
    fgyroz = utils.fft(gyroz)

    facc_mag = utils.fft(acc_mag)
    facc_jerk_mag = utils.fft(acc_jerk_mag)
    fgyro_mag = utils.fft(gyro_mag)
    fgyro_jerk_mag = utils.fft(gyro_jerk_mag)

    return np.array([accx, accy, accz, acc_jerk_x, acc_jerk_y, acc_jerk_z, gyrox, gyroy, gyroz,
                     gyro_jerk_x, gyro_jerk_y, gyro_jerk_z, acc_mag, acc_jerk_mag, gyro_mag, gyro_jerk_mag,
                     faccx, faccy, faccz, facc_jerk_x, facc_jerk_y, facc_jerk_z, fgyrox, fgyroy, fgyroz,
                     facc_mag, facc_jerk_mag, fgyro_mag, fgyro_jerk_mag])


def get_feature(window):
    mean = np.mean(window, axis=0)
    std = np.std(window, axis=0)
    mad = np.median(window, axis=0)
    min = np.amin(window, axis=0)
    max = np.amax(window, axis=0)
    sma = np.mean(window, axis=0)


def get_features(ax, ay, az, yaw, pitch, roll):
    pass

# data = "[{'yaw': -157.6705, 'pitch': -4.33582, 'roll': -2.451883, 'Ax': 0, 'Ay': 485, 'Az': 7381, 'timestamps': 1542884104.3810017}, " \
#        "{'yaw': -157.7411, 'pitch': -4.701654, 'roll': -1.870299, 'Ax': -53, 'Ay': 630, 'Az': 7189, 'timestamps': 1542884104.3893933}, " \
#        "{'yaw': -157.8128, 'pitch': -5.099143, 'roll': -1.229501, 'Ax': -92, 'Ay': 793, 'Az': 6948, 'timestamps': 1542884104.3895116}, " \
#        "{'yaw': -157.888, 'pitch': -5.491229, 'roll': -0.536322, 'Ax': -101, 'Ay': 972, 'Az': 6662, 'timestamps': 1542884104.3895922}, " \
#        "{'yaw': -157.9806, 'pitch': -5.876004, 'roll': 0.203376, 'Ax': -78, 'Ay': 1154, 'Az': 6383, 'timestamps': 1542884104.3896697}]"
#
# df = parse_data(data)
# print(df['ax'].values)


a = np.median([2, 80, 6])
print(a)