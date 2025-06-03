from PIL import Image
import os
import numpy as np

# 입력 및 출력 디렉토리 설정
src_folder = "style/cropped"
dst_folder = "style_cleaned"
os.makedirs(dst_folder, exist_ok=True)

# 이미지 처리 루프
for fname in os.listdir(src_folder):
    if fname.lower().endswith(".png"):
        src_path = os.path.join(src_folder, fname)

        # 이미지 열기 및 흑백 변환
        img = Image.open(src_path).convert("L")

        # NumPy 배열로 변환
        img_np = np.array(img)

        # 이진화 처리 (threshold)
        threshold = 200
        img_bin = np.where(img_np > threshold, 255, 0).astype(np.uint8)

        # 다시 이미지로 변환
        img_cleaned = Image.fromarray(img_bin, mode="L")

        # 리사이즈 (128x128)
        img_cleaned = img_cleaned.resize((128, 128), Image.Resampling.LANCZOS)

        # 저장
        dst_path = os.path.join(dst_folder, fname)
        img_cleaned.save(dst_path)
        print(f"Saved cleaned image: {dst_path}")
