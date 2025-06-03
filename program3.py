import yaml

cfg = {
    'style_imgs': [
        'style_cleaned/uniAC00.png',
        'style_cleaned/uniAC01.png',
        'style_cleaned/uniAC02.png',
        'style_cleaned/uniAC03.png',
        'style_cleaned/uniAC04.png',
        'style_cleaned/uniAC05.png',
        'style_cleaned/uniAC06.png',
        'style_cleaned/uniAC07.png',
        'style_cleaned/uniAC08.png',
        'style_cleaned/uniAC09.png',
        'style_cleaned/uniAC0A.png',
        'style_cleaned/uniAC0B.png',
        'style_cleaned/uniAC0C.png',
        'style_cleaned/uniAC0D.png',
        'style_cleaned/uniAC0E.png',
        'style_cleaned/uniAC0F.png',
        'style_cleaned/uniAC10.png',
        'style_cleaned/uniAC11.png',
        'style_cleaned/uniAC12.png',
        'style_cleaned/uniAC13.png',
        'style_cleaned/uniAC14.png',
        'style_cleaned/uniAC15.png',
        'style_cleaned/uniAC16.png',
        'style_cleaned/uniAC17.png',
        'style_cleaned/uniAC18.png',
        'style_cleaned/uniAC19.png',
        'style_cleaned/uniAC1A.png',
        'style_cleaned/uniAC1B.png'
    ],
    'style_chars': ['각','깪','냓','댼','떥','렎','멷','볠','뽉','솲','쐛','욄','죭','쭖','춣','퀨','튑','퓺','흣','읬','잉','잊','잋','잌','잍','잎','잏','이'],

    'charset_path': 'data/charset/korean11172.txt',
    'output_dir': 'output',
    'checkpoint': 'checkpoints/korean-handwriting.pth',
    'num_font_samples': 1,
    'target_chars': ['가','나','다','라','마','바','사','아','자','차','카','타','파','하','\n','안','녕','하','세','요','\n','감','사','합','니','다','\n','구','름','빵',' ','먹','고','싶','다','\n','오','늘',' ','저','녁','은',' ','고','추','잡','채','밥'],

    'C': 32,
    'n_comps': 68,
    'n_comp_types': 3,
    'language': 'kor'
}

with open('configs/infer_colab.yaml', 'w') as f:
    yaml.dump(cfg, f, allow_unicode=True)
