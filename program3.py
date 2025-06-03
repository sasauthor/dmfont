import yaml
import sys

# 터미널 인자로부터 타겟 문자 받기
target_chars = sys.argv[1:]

# YAML 설정 딕셔너리 구성
cfg = {
    'style_imgs': [
        f'style_cleaned/uniAC{str(i).zfill(2)}.png' for i in range(0, 28)
    ],
    'style_chars': [
        '각', '깪', '냓', '댼', '떥', '렎', '멷', '볠', '뽉', '솲', '쐛', '욄', '죭', '쭖',
        '춣', '퀨', '튑', '퓺', '흣', '읬', '잉', '잊', '잋', '잌', '잍', '잎', '잏', '이'
    ],
    'charset_path': 'data/charset/korean11172.txt',
    'output_dir': 'output',
    'checkpoint': 'checkpoints/korean-handwriting.pth',
    'num_font_samples': 1,
    'target_chars': target_chars,
    'C': 32,
    'n_comps': 68,
    'n_comp_types': 3,
    'language': 'kor'
}

# YAML 파일로 저장
with open('configs/infer_colab.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(cfg, f, allow_unicode=True)

print("YAML 설정 파일 생성 완료: configs/infer_colab.yaml")
