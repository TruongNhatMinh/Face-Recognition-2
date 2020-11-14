Download Models folder at here: https://drive.google.com/drive/folders/1kJq1LxjAYRy1whBAooKiLd-YrKHulnV9?usp=sharing

python src/align_dataset_mtcnn.py  Dataset/FaceData/raw Dataset/FaceData/processed --image_size 160 --margin 32  --random_order --gpu_memory_fraction 0.25

python src/classifier.py TRAIN Dataset/FaceData/processed Models/20180402-114759.pb Models/facemodel.pkl --batch_size 5000

python src/face_rec_cam.py
