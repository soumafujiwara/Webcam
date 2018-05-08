#!/usr/bin/env python
# coding=utf-8

import cv2
import colorTracking #カラートラッキングとPID入力の生成
from cv_bridge import CvBridge, CvBridgeError   # Image型からcv2での画像の方に変換するために必要

# マウスクリックの処理
def onMouse(event, x, y, flags, param):
    # 左クリックしたとき
    if event == cv2.EVENT_LBUTTONDOWN:
        clr.extractColor(x,y,0)     # クリックしたピクセルの色情報を抽出し，[colorStep]番目の色として保存する
        return

if __name__=="__main__":

    # 各インスタンスの宣言
    clr = colorTracking.Ct(1, 30, 200)#カラートラッキング用 (トラッキングする色の数，HSV値の許容値，画像配列の走査範囲),名前＝インポートファイル.クラス名()
    capture = cv2.VideoCapture(0)

    if capture.isOpened() is False:
        raise("IO Error")

    #カメラの表示
    cv2.namedWindow("Capture", cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback("Capture", onMouse)

    while True:
        clr.calCenterofWeight(capture)
        showStatus()

        #カメラの表示
        ret, image = capture.read()
        if ret == False:
            continue
        cv2.imshow("Capture", image)
        if cv2.waitKey(33) >= 0:
            cv2.imwrite("image.png", image)
            break
    cv2.destroyAllWindows()
