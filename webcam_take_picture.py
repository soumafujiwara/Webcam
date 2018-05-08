# -*- coding: utf-8 -*-
import numpy as np
import cv2
import os #rename用モジュール

#######################パラメータ変更部分######################
#webカメラから画像を保存する方法。
#[s]キーで保存。
i = 51#保存した写真名の番号。
###########################################################

cap = cv2.VideoCapture(0)

while(True):
    # フレームをキャプチャする
    ret, frame = cap.read()


    # 画面に表示する
    cv2.imshow('frame',frame)

    # キーボード入力待ち
    key = cv2.waitKey(1) & 0xFF

    # oが押された場合は終了する
    if key == ord('o'):
        break
    # sが押された場合は保存する
    if key == ord('s'):
        i = i+1
        path = str("{0:06d}".format(i)) + '.jpg'

        cv2.imwrite(path,frame)

# キャプチャの後始末と，ウィンドウをすべて消す
cap.release()
cv2.destroyAllWindows()
