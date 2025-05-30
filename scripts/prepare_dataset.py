import os
import fitz  # PyMuPDF
from PIL import Image
import numpy as np

# 템플릿 기준 자소 리스트
JASO_LIST = [
    'ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ',
    'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ',
    'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ',

    'ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ',
    'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ',
    'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ',
    'ㅡ', 'ㅢ', 'ㅣ',

    'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ',
    'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ',
    'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ',
    'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ',
    'ㅌ', 'ㅍ', 'ㅎ'
]

def extract_and_save_glyphs_as_npy(
    pdf_path: str,
    out_npy_dir: str,
    grid_size=(10, 7),
    glyph_size=(112, 112),
    padding=(15, 15)
):
    os.makedirs(out_npy_dir, exist_ok=True)

    # 1. PDF 로드 및 이미지 변환
    doc = fitz.open(pdf_path)
    page = doc[0]
    pix = page.get_pixmap(dpi=300)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples).convert("L")

    width, height = img.size
    cols, rows = grid_size
    pad_x, pad_y = padding

    box_width = (width - pad_x * 2) // cols
    box_height = (height - pad_y * 2) // rows

    idx = 0
    for row in range(rows):
        for col in range(cols):
            if idx >= len(JASO_LIST):
                break
            left = pad_x + col * box_width
            top = pad_y + row * box_height
            box = (left, top, left + box_width, top + box_height)
            cropped = img.crop(box)
            resized = cropped.resize(glyph_size, Image.ANTIALIAS)
            glyph_array = np.asarray(resized, dtype=np.uint8)
            save_path = os.path.join(out_npy_dir, f"glyph_{idx:03d}.npy")
            np.save(save_path, glyph_array)
            idx += 1

    print(f"✅ {idx} glyphs extracted and saved as .npy in '{out_npy_dir}'")

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf', type=str, required=True, help='Input hand-drawn PDF file')
    parser.add_argument('--out', type=str, required=True, help='Output directory to save .npy glyphs')
    parser.add_argument('--cols', type=int, default=10, help='Number of columns in the grid')
    parser.add_argument('--rows', type=int, default=7, help='Number of rows in the grid')
    parser.add_argument('--glyph_size', type=int, default=112, help='Size (pixels) of the output glyph images')
    parser.add_argument('--pad_x', type=int, default=15, help='Horizontal padding')
    parser.add_argument('--pad_y', type=int, default=15, help='Vertical padding')

    args = parser.parse_args()

    extract_and_save_glyphs_as_npy(
        pdf_path=args.pdf,
        out_npy_dir=args.out,
        grid_size=(args.cols, args.rows),
        glyph_size=(args.glyph_size, args.glyph_size),
        padding=(args.pad_x, args.pad_y)
    )
