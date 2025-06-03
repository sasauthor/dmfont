from pdf2image import convert_from_path
import os

pdf_files = [
    "style/Styleimg.pdf",
]

output_dir = "style"
os.makedirs(output_dir, exist_ok=True)

for pdf_path in pdf_files:
    images = convert_from_path(pdf_path, dpi=300)
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    if len(images) > 1:
        # 여러 페이지면 _p1, _p2 등 붙임
        for i, img in enumerate(images):
            out_path = f"{output_dir}/{base_name}_p{i+1}.png"
            img.save(out_path)
            print(f"save complete: {out_path}")
    else:
        # 한 페이지만 있으면 기본 이름으로 저장
        img = images[0]
        out_path = f"{output_dir}/{base_name}.png"
        img.save(out_path)
        print(f"save complete: {out_path}")

from PIL import Image, ImageChops

def trim_whitespace(path):
    img = Image.open(path)
    bg = Image.new(img.mode, img.size, img.getpixel((0, 0)))
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()
    if bbox:
        trimmed = img.crop(bbox)
        trimmed.save(path)  # 덮어쓰기
        print(f"deleting complete: {path}")
    else:
        print(f"no whites: {path}")

# data/raw 안의 모든 이미지 여백 제거
for fname in os.listdir("/content/dmfont/style"):
    if fname.lower().endswith((".png", ".jpg", ".jpeg")):
        trim_whitespace(f"/content/dmfont/style/{fname}")


raw_dir = "style"

for fname in os.listdir(raw_dir):
    if fname.lower().endswith((".png", ".jpg", ".jpeg")):
        path = os.path.join(raw_dir, fname)
        img = Image.open(path)
        img.save(path, dpi=(300, 300))  # 해상도만 300dpi로 설정
        print(f"300dpi save complete: {fname}")

!python style/crop.py \
  --src_dir=style \
  --dst_dir=style/cropped
