# -*- coding: utf-8 -*-
"""
@author: Yaxin Guo
@software: PyCharm
@file: eval.py
@email:guoyaxin_cong@163.com
@time: 2024/3/18 8:28
"""
import sys
import os
import json


def eval_crmus(pred_f1, golden_f1, pred_f2, golden_f2):
    # 依次读取文件内容
    pred_cr, gold_cr, pred_mu, gold_mu = [], [], [], []
    try:
        with open(file=pred_f1, mode="r", encoding="utf-8") as fin:
            pred_cr = json.load(fin)
        succ_info = "predict file CR load succeed..."
        print(succ_info)
    except Exception as e:
        err_info = "predict file CR load failed. please upload a json file. err: {}".format(e)
        print(err_info)
        exit(-1)
    try:
        with open(file=golden_f1, mode="r", encoding="utf-8") as fin:
            gold_cr = json.load(fin)
        succ_info = "golden file CR load succeed..."
        print(succ_info)
    except Exception as e:
        err_info = "golden file CR load failed. please upload a json file. err: {}".format(e)
        print(err_info)
        exit(-1)

    try:
        with open(file=pred_f2, mode="r", encoding="utf-8") as fin:
            pred_mu = json.load(fin)
        succ_info = "predict file MU load succeed..."
        print(succ_info)
    except Exception as e:
        err_info = "predict file MU load failed. please upload a json file. err: {}".format(e)
        print(err_info)
        exit(-1)
    try:
        with open(file=golden_f2, mode="r", encoding="utf-8") as fin:
            gold_mu = json.load(fin)
        succ_info = "golden file MU load succeed..."
        print(succ_info)
    except Exception as e:
        err_info = "golden file MU load failed. please upload a json file. err: {}".format(e)
        print(err_info)
        exit(-1)

    # 计算常识推理任务准确率：
    right_count_cr = 0
    for item_p, item_g in zip(pred_cr, gold_cr):
        if item_p['answer'] == item_g['answer']:
            right_count_cr += 1
    acc1 = right_count_cr / len(gold_cr)

    # 计算寓意理解任务准确率：
    right_count_mu = 0
    for item_p, item_g in zip(pred_mu, gold_mu):
        if item_p['answer'] == item_g['answer']:
            right_count_mu += 1
    acc2 = right_count_mu / len(gold_mu)

    s = 0.4 * acc1 + 0.6 * acc2

    return acc1, acc2, s


if __name__ == '__main__':
    pred_file1 = sys.argv[1]
    golden_file1 = sys.argv[2]

    pred_file2 = sys.argv[3]
    golden_file2 = sys.argv[4]

    if not os.path.exists(pred_file1):
        print("predict file CR load failed. please upload a json file.err:predict file is not existing.")
        exit(-1)
    elif not os.path.exists(golden_file1):
        print("golden file CR load failed. please upload a json file.err:golden file is not existing.")
        exit(-2)
    elif not os.path.exists(pred_file2):
        print("predict file MU load failed. please upload a json file.err:predict file is not existing.")
        exit(-3)
    elif not os.path.exists(golden_file2):
        print("golden file MU load failed. please upload a json file.err:golden file is not existing.")
        exit(-4)

    adv_acc1, adv_acc2, Score = eval_crmus(pred_file1, golden_file1, pred_file2, golden_file2)

    print(json.dumps({"Acc1": adv_acc1, "Acc2": adv_acc2, "Score": Score}))

''' shell
python eval.py prediction_file1 dev_CRMUS_CR_file2 prediction_file3 dev_CRMUS_MU_file4
eg: python eval_ccl_public.py ./submit/valid_submit_CR.json ./submit/dev_CRMUS_CR.json ./submit/valid_submit_MU.json ./submit/dev_CRMUS_MU.json
'''
