# dataset settings
dataset_type = 'RPCDataset'
classes = ('1_puffed_food','2_puffed_food','3_puffed_food','4_puffed_food','5_puffed_food','6_puffed_food','7_puffed_food','8_puffed_food','9_puffed_food','10_puffed_food','11_puffed_food','12_puffed_food','13_dried_fruit','14_dried_fruit','15_dried_fruit','16_dried_fruit','17_dried_fruit','18_dried_fruit','19_dried_fruit','20_dried_fruit','21_dried_fruit','22_dried_food','23_dried_food','24_dried_food','25_dried_food','26_dried_food','27_dried_food','28_dried_food','29_dried_food','30_dried_food','31_instant_drink','32_instant_drink','33_instant_drink','34_instant_drink','35_instant_drink','36_instant_drink','37_instant_drink','38_instant_drink','39_instant_drink','40_instant_drink','41_instant_drink','42_instant_noodles','43_instant_noodles','44_instant_noodles','45_instant_noodles','46_instant_noodles','47_instant_noodles','48_instant_noodles','49_instant_noodles','50_instant_noodles','51_instant_noodles','52_instant_noodles','53_instant_noodles','54_dessert','55_dessert','56_dessert','57_dessert','58_dessert','59_dessert','60_dessert','61_dessert','62_dessert','63_dessert','64_dessert','65_dessert','66_dessert','67_dessert','68_dessert','69_dessert','70_dessert','71_drink','72_drink','73_drink','74_drink','75_drink','76_drink','77_drink','78_drink','79_alcohol','80_alcohol','81_drink','82_drink','83_drink','84_drink','85_drink','86_drink','87_drink','88_alcohol','89_alcohol','90_alcohol','91_alcohol','92_alcohol','93_alcohol','94_alcohol','95_alcohol','96_alcohol','97_milk','98_milk','99_milk','100_milk','101_milk','102_milk','103_milk','104_milk','105_milk','106_milk','107_milk','108_canned_food','109_canned_food','110_canned_food','111_canned_food','112_canned_food','113_canned_food','114_canned_food','115_canned_food','116_canned_food','117_canned_food','118_canned_food','119_canned_food','120_canned_food','121_canned_food','122_chocolate','123_chocolate','124_chocolate','125_chocolate','126_chocolate','127_chocolate','128_chocolate','129_chocolate','130_chocolate','131_chocolate','132_chocolate','133_chocolate','134_gum','135_gum','136_gum','137_gum','138_gum','139_gum','140_gum','141_gum','142_candy','143_candy','144_candy','145_candy','146_candy','147_candy','148_candy','149_candy','150_candy','151_candy','152_seasoner','153_seasoner','154_seasoner','155_seasoner','156_seasoner','157_seasoner','158_seasoner','159_seasoner','160_seasoner','161_seasoner','162_seasoner','163_seasoner','164_personal_hygiene','165_personal_hygiene','166_personal_hygiene','167_personal_hygiene','168_personal_hygiene','169_personal_hygiene','170_personal_hygiene','171_personal_hygiene','172_personal_hygiene','173_personal_hygiene','174_tissue','175_tissue','176_tissue','177_tissue','178_tissue','179_tissue','180_tissue','181_tissue','182_tissue','183_tissue','184_tissue','185_tissue','186_tissue','187_tissue','188_tissue','189_tissue','190_tissue','191_tissue','192_tissue','193_tissue','194_stationery','195_stationery','196_stationery','197_stationery','198_stationery','199_stationery','200_stationery')
data_root = '../RPC/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(800, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        ann_file=data_root + 'instances_val2019.json',
        img_prefix=data_root + 'val2019/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'instances_val2019.json',
        img_prefix=data_root + 'val2019/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'instances_test2019.json',
        img_prefix=data_root + 'test2019/',
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric='bbox')
