from pdf2image import convert_from_path
from PIL import Image, ImageChops
import subprocess
import os

# PDF → 이미지 변환
pdf_files = ["style/Styleimg.pdf"]
output_dir = "style"
os.makedirs(output_dir, exist_ok=True)

for pdf_path in pdf_files:
    images = convert_from_path(pdf_path, dpi=300)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    if len(images) > 1:
        for i, img in enumerate(images):
            out_path = f"{output_dir}/{base_name}_p{i+1}.png"
            img.save(out_path)
            print(f"save complete: {out_path}")
    else:
        img = images[0]
        out_path = f"{output_dir}/{base_name}.png"
        img.save(out_path)
        print(f"save complete: {out_path}")

# 여백 제거 함수 정의
def trim_whitespace(path):
    img = Image.open(path)
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        trimmed = img.crop(bbox)
        trimmed.save(path)
        print(f"deleting complete: {path}")
    else:
        print(f"no whites: {path}")

# style 디렉토리 내 모든 이미지 여백 제거
raw_dir = "style"
for fname in os.listdir(raw_dir):
    if fname.lower().endswith((".png", ".jpg", ".jpeg")):
        trim_whitespace(os.path.join(raw_dir, fname))

# 모든 이미지의 DPI 300으로 재설정
for fname in os.listdir(raw_dir):
    if fname.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(raw_dir, fname)
        img = Image.open(path)
        img.save(path, dpi=(300, 300))
        print(f"300dpi save complete: {fname}")

# crop.py 실행
subprocess.run([
    "python", "style/crop.py",
    "--src_dir=style",
    "--dst_dir=style/cropped"
], check=True)
