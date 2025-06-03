from PIL import Image
import os
import numpy as np

src_folder = "style/cropped"
dst_folder = "style_cleaned"
os.makedirs(dst_folder, exist_ok=True)

for fname in os.listdir(src_folder):
    if fname.lower().endswith(".png"):
        # 이미지 열기 및 흑백화
        img = Image.open(os.path.join(src_folder, fname)).convert("L")

        # NumPy 배열로 변환
        img_np = np.array(img)

        # threshold 적용 (0 또는 255로 변환)
        threshold = 200
        img_bin = np.where(img_np > threshold, 255, 0).astype(np.uint8)

        # 다시 이미지로 변환
        img_cleaned = Image.fromarray(img_bin, mode="L")

        # 리사이즈
        img_cleaned = img_cleaned.resize((128, 128), Image.Resampling.LANCZOS)

        # 저장
        img_cleaned.save(os.path.join(dst_folder, fname))
