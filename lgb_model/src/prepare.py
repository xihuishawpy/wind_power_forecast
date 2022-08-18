# -*-Encoding: utf-8 -*-
"""
Description: Parameter Setting
Authors: aihongfeng
Date:    2022/05/20
Function:

"""
import os

def prep_env():
    path = os.path.dirname(os.path.abspath(__file__))
    exp_ver = 16
    settings = {
        "path_to_test_x": "/home/notebook/code/group/intention_rec/TimeSeries/kdd2022/PaddleSpatial/apps/wpf_baseline_gru/kddcup22-sdwpf-evaluation/data/test_x/0001in.csv",
        "path_to_test_y": "/home/notebook/code/group/intention_rec/TimeSeries/kdd2022/PaddleSpatial/apps/wpf_baseline_gru/kddcup22-sdwpf-evaluation/data/test_y/0001out.csv",
        "data_path": "/home/notebook/data/group/intention_rec/TimeSeries/KDD2022",
        "filename": "wtbdata_245days.csv",
        "diff_angle_path": os.path.join(path, "diff_angle.csv"),
        "ab_lgb_model_path": os.path.join(
            path, "lgb_abnormal_fix_Patv_regressor.txt"
        ),
        "max_paras_path": os.path.join(path, "max_paras.csv"),
        "preprocess_data_path": os.path.join(
            path, f"wtbdata_245days_preprocess{exp_ver}.csv"
        ),
        "scaler_save_path": os.path.join(path, f"scaler{exp_ver}.npy"),
        "tsfresh_params_path": os.path.join(
            path, "kind_to_fc_parameters_top59.npy"
        ),
        "lgb_model_save_path": os.path.join(
            path, f"tmodels/lgb_regressor{exp_ver}.txt"
        ),
        "lgb_feat_import_save_path": os.path.join(
            path, f"tmodels/lgb_feat_import{exp_ver}.png"
        ),
        "checkpoints": "checkpoints",
        "start_col": 3,
        "total_size": (432 + 288) * 134,
        "pred_file": "predict.py",
        "framework": "base",
        "is_submit": True,
    }

    print(f"The experimental settings are: \n{settings}\n")
    return settings