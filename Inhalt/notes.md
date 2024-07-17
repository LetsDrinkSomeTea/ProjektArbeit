# Face-Swapping


# Reenactment
Example Video: [You Won’t Believe What Obama Say In This Video](https://www.youtube.com/watch?v=cQ54GDm1eL0)

Methode für beides: FSGAN (Face Swapping GAN (Generative Adversarial Network)))

Gute Quelle für Detection Methods: ```Deepfake: An Overview```


Tools:
- DeepFaceLab: https://github.com/iperov/DeepFaceLab
- DeepFaceLive: https://github.com/iperov/DeepFaceLive
- FSGAN: https://github.com/YuvalNirkin/fsgan

Praktische Anwendung:
- How to DeepFaceLab
  - Extract Images
  - Extract Faces
  - Select Data
  - Train Face Detection
    - XSeg Generic
    - XSeg Manuell
  - Training
    - Quick96
      - 10.000
      - 50.000
    - SAEHD
      - nicht pretrained
        - 10.000
        - 50.000
      - 100.000 pretrained
        - 10.000
        - 50.000
  - Merge
    - XSeg
    - SAEHD
    - Verschiedene Merge Einstellungen


```
1) clear workspace.bat
2) extract images from video data_src.bat
3) cut video (drop video on me).bat
3) extract images from video data_dst FULL FPS.bat
3.optional) denoise data_dst images.bat
4) data_src faceset extract MANUAL.bat
4) data_src faceset extract.bat
4.1) data_src view aligned result.bat
4.2) data_src sort.bat
4.2) data_src util add landmarks debug images.bat
4.2) data_src util faceset enhance.bat
4.2) data_src util faceset metadata restore.bat
4.2) data_src util faceset metadata save.bat
4.2) data_src util faceset pack.bat
4.2) data_src util faceset resize.bat
4.2) data_src util faceset unpack.bat
4.2) data_src util recover original filename.bat
5) data_dst faceset extract + manual fix.bat
5) data_dst faceset extract MANUAL.bat
5) data_dst faceset extract.bat
5) data_dst faceset MANUAL RE-EXTRACT DELETED ALIGNED_DEBUG.bat
5.1) data_dst view aligned results.bat
5.1) data_dst view aligned_debug results.bat
5.2) data_dst sort.bat
5.2) data_dst util faceset pack.bat
5.2) data_dst util faceset resize.bat
5.2) data_dst util faceset unpack.bat
5.2) data_dst util recover original filename.bat
5.XSeg Generic) data_dst whole_face mask - apply.bat
5.XSeg Generic) data_src whole_face mask - apply.bat
5.XSeg) data_dst mask - edit.bat
5.XSeg) data_dst mask - fetch.bat
5.XSeg) data_dst mask - remove.bat
5.XSeg) data_dst trained mask - apply.bat
5.XSeg) data_dst trained mask - remove.bat
5.XSeg) data_src mask - edit.bat
5.XSeg) data_src mask - fetch.bat
5.XSeg) data_src mask - remove.bat
5.XSeg) data_src trained mask - apply.bat
5.XSeg) data_src trained mask - remove.bat
5.XSeg) train.bat
6) export AMP as dfm.bat
6) export SAEHD as dfm.bat
6) train AMP SRC-SRC.bat
6) train AMP.bat
6) train Quick96.bat
6) train SAEHD.bat
7) merge AMP.bat
7) merge Quick96.bat
7) merge SAEHD.bat
8) merged to avi.bat
8) merged to mov lossless.bat
8) merged to mp4 lossless.bat
8) merged to mp4.bat
10.misc) make CPU only.bat
10.misc) start EBSynth.bat
```